from ast import literal_eval
import pandas as pd
import re


def specs(pandas):	
	for i, row in pandas.iterrows():
         	specific = {}
    	    if type(row['specifications']) == str:
			if str(row['specifications']).find('[{') != -1:
		    		p = literal_eval(row['specifications'])
				for i in range(len(p)):
				        l = list(p[i].values())
				        if l[0].find('css_selector') + 1:
				            l[0] = ' '
				        if l[1].find('css_selector') + 1:
				            l[1] = ' '
			        specific[l[0]] = l[1]

			elif str(row['specifications']).find('css_selector') + 1:
			    row['specifications'] = None
		    row['specifications'] = specific
	return pandas


def convertor_row(pandas, column, pattern):
	for i, row in pandas.iterrows():    
	    p = pandas[column]
	    if p != None:
	        pandas[column] = p.split(pattern)
    return pandas


def convertor_none(rdd_pd, list):
    for index,row in rdd_pd.iterrows():
        for i in list:
            if row[i] == None:
                row[i] = None
            elif str(row[i]).find('css_selector') + 1:
                row[i] = None
    return rdd_pd


def image_data(pandas):
    for i, row in pandas.iterrows():
        p = row['images']
        if p != None:
            pattern = r"(?:background-image:url)|\|background-image:url"
            q = re.split(pattern, p)
            q.pop(0)
            row['images'] = q
    return pandas

def Null_dict(pandas):
    Null_dict = {}
    pandas = convertor_none(pandas, list(pandas.columns))
    for column in list(pandas.columns):
        j = 0
        for i in range(pandas.shape[0]):
            if pandas[column].iloc[i] == None:
                j = j + 1
        Null_dict[column] = j
    return Null_dict



