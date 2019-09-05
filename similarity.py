import gc
import numpy as np
import pandas as pd
import sqlalchemy as db
from sqlalchemy.sql import text
from pyspark.ml import Pipeline
from pyspark.conf import SparkConf
from pyspark.sql.functions import col
from pyspark.sql import SparkSession, SQLContext
from sqlalchemy import create_engine, MetaData, Table
from pyspark.ml.feature import Tokenizer, NGram, HashingTF, MinHashLSH, Normalizer, StopWordsRemover

class SimilarProducts():

    spark = SparkSession.builder.appName("similar_products").config("spark.executor.memory", '4G').config("spark.driver.memory", '4G').getOrCreate()
    sc = spark.sparkContext
    sqlctx = SQLContext(sc)
    engine = create_engine('postgresql://eunimart_user:eunimart!123!@crawler-data.cluster-ro-cqxnvh2hudf5.us-east-2.rds.amazonaws.com:5432/crawled_data')
    cursor = engine.connect()
    metadata = MetaData(engine)
    # spark.debug.maxToStringFields=100

    STOP_WORDS = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'also', 'am', 'an', 'and',
                'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below',
                'between', 'both', 'but', 'by', 'can', "can't", 'cannot', 'com', 'could', "couldn't", 'did',
                "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'else', 'ever',
                'few', 'for', 'from', 'further', 'get', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having',
                'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how',"not_available"
                "how's", 'however', 'http', 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it',
                "it's", 'its', 'itself', 'just', 'k', "let's", 'like', 'me', 'more', 'most', "mustn't", 'my', 'myself',
                'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'otherwise', 'ought', 'our', 'ours',
                'ourselves', 'out', 'over', 'own', 'r', 'same', 'shall', "shan't", 'she', "she'd", "she'll", "she's",
                'should', "shouldn't", 'since', 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs',
                'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're",
                "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't",
                'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where',
                "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't",
                'www', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves','&','!','@','#','$','%','^','*','(',')','<','>','/',"?",'-','_']

    @classmethod
    def vectorize(self, seller_data_frame):
        products = Table('products', self.metadata, autoload = True, autoload_with = self.engine)
        i = 0
        seller_data_frame['seller_title_description'] = seller_data_frame['title_description']  
        seller_spark_df = self.model(seller_data_frame, "seller_title_description")
        seller_spark_df.registerTempTable('seller')
        seller_df = self.sqlctx.sql('SELECT seller_title_description, pid, vectors from seller') 
        # seller_spark_df = seller_spark_df.select((seller_spark_df.product_title + seller_spark_df.product_description).alias("seller_title_description"), "sku_id", 'vectors', "cat_name")
        
        while(True):
            print('Entering the loop for {}th time'.format(i+1))
            try:
                products_1 = text('''SELECT pid, concat(product_title , \' \' ,description, \' \', description_list) as title_description FROM products WHERE (products.id BETWEEN {} AND {}) AND (products.product_title != \'-\')'''.format(200000*i, 200000*(i+1)))
                product_list = self.cursor.execute(products_1).fetchall()
                product_pd = pd.DataFrame(product_list,columns = ['pid', 'title_description'])
                product = self.model(product_pd, 'title_description')
                gc.collect()
                similarity_products = self.similarity_matrix(product, seller_df)
                print(similarity_products.count())
                if i == 0:
                    final_similarity = similarity_products
                else:
                    final_similarity = final_similarity.unionAll(similarity_products)
                del products_1
                del product_list
                del product_pd
                product.unpersist()
                similarity_products.unpersist()
                gc.collect()
            except Exception as e:
                # generally exception rises when we encounter the end of the database
                print("Error is ", e);
                break
            i = i + 1
            
        return final_similarity

    @classmethod
    def model(self, pandas, column):
        rdd =  self.sqlctx.createDataFrame(pandas.astype(str))
        model = Pipeline(stages=[
        Tokenizer(inputCol= column, outputCol="tokens"),
        StopWordsRemover(inputCol= 'tokens', outputCol="tokens_stop", stopWords = self.STOP_WORDS),
        HashingTF(inputCol="tokens_stop", outputCol="vectors")]).fit(rdd)
        
        db_1 = model.transform(rdd)
        db_1.cache()
        return db_1

    @classmethod
    def similarity_matrix(self, rdd1, rdd2):
        minhash = MinHashLSH(inputCol = 'vectors', outputCol = 'LSH')
        model = minhash.fit(rdd1)
        rdd1 = model.transform(rdd1)
        rdd2 = model.transform(rdd2)
        output = model.approxSimilarityJoin(rdd1,rdd2, threshold = 0.8).filter(col('distCol') > 0) \
                    .select(col('datasetB.pid').alias('sku_id_seller'), col('datasetA.pid').alias('pid'),col('distCol').alias('similarity_score'))
        print(output)
        return output  #dataframe contains five columns id_seller(seller products ID), id(our database_products id), product_seller, product_database, similarity_score

    @classmethod    
    def top_similar_products(self, seller_data_frame):
        similar_matrix = self.vectorize(seller_data_frame)
        similar_matrix = similar_matrix.sort(similar_matrix, ascending = True)
        print("--->", similar_matrix.show(), similar_matrix.count())
        pass


df = pd.read_json('data.json')
df['prod'] = df['product_title'] + ' ' + df['product_description']
df = df[['sku_id', 'prod']]
df['product_title'] = df['prod']
SimilarProducts.top_similar_products(df)