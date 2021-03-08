'''
Douglas Pizac and Gabriela Huelgas

Created imputation functions for missing and categorical data
'''

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import seaborn as sns
def ordinal_scale(Series):
    '''Returns a pandas Series where quality scores are converted to integers
    
    Args:
    
    Series: a pandas Series of categorical quality scores'''
    return Series.replace({'Po':0,'Fa':1,'TA':2,'Gd':3,'Ex':4})

def fillna_cats(Series):
    '''
    Returns a categorical pandas series replacing null values with DNE (Does Not Exist).
    
    Args:
    
    Series: str, column name in the pandas dataframe.
    '''
    Series.fillna('DNE',inplace = True)
    return Series

def impute_by_neighborhood(df,Series,method):
    '''Returns series with missing values imputed by specifed method.
    
    Args:
    
    df: pd.Dataframe, Dataframe to pass in
    Series: str, column name in df
    method: str, Central tendency method by which to impute (examples: "mean","median")
    '''
    
    if not isinstance(df, pd.DataFrame):
        raise TypeError('df argument must be of type pd.DataFrame')
        
    if not isinstance(Series, str):
        raise TypeError('Series but be the column name as a string')
    return df[Series].fillna(df.groupby('Neighborhood')[Series].transform(method))


def switch_ordinals(df, Series):
    '''
    Returns a pandas series replacing null values with DNE (Does Not Exist) so they can be imputed.
    
    Args:
    
    df: pd.Dataframe, Dataframe to pass in
    Series: str, column name in the pandas dataframe.
    '''
    if df[Series].isnull().sum()==0:
        df[Series].replace({'Po':None,'Fa':1,'TA':2,'Gd':3,'Ex':4},inplace = True)
    else:
        df[Series].fillna('DNE',inplace = True)
        df[Series].replace({'Po':None,'DNE':1,'Fa':2,'TA':3,'Gd':4,'Ex':5},inplace = True)
    return df[Series]