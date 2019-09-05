import pandas as pd
class Transformation:
    def __init__(self, rdd):
        self.rdd = rdd.toPandas()
    
    def convertor_none(self, list):
        rdd_pd = self.rdd
        for index,row in rdd_pd.iterrows():
            for i in list:
                if row[i] == None:
                    row[i] = None
                elif type(row[i]) == str:
                    if row[i].find('css_selector') + 1:
                        row[i] = None
        return rdd_pd
    
    def image_data(self, column):
        rdd_pd = self.rdd
        pandas = rdd_pd[column]
        for i in range(pandas.shape[0]):
            p = pandas[column].iloc[i]
            if p != None:
                pattern = r"(?:background-image:url)|\|background-image:url"
                q = re.split(pattern, p)
                q.pop(0)
                pandas[column].iloc[i] = q
        rdd_pd[column] = pandas
        return rdd_pd
    
    def convertor_row(self, column, pattern):
        rdd_pd = self.convertor_none(list(self.rdd.columns))
        pandas = pd.DataFrame(rdd_pd[column])
        for i in range(pandas.shape[0]):
            p = pandas[column].iloc[i]
            if p != None:
                pandas[column].iloc[i] = str(p).split(pattern)
        rdd_pd[column] = pandas
        return rdd_pd
    
    def Null_dict(self):
        Null_dict = {}
        pandas = self.convertor_none(list(self.rdd.columns))
        for column in list(pandas.columns):
            j = 0
            for i in range(pandas.shape[0]):
                if pandas[column].iloc[i] == None:
                    j = j + 1
            Null_dict[column] = j

        return Null_dict