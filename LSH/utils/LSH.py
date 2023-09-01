#---------------------------------------------------------------#
#------------ LSH algorithm ------------------------------------#
#---------------------------------------------------------------#
import random as rd 
import pandas as pd 


def getHashFunc(d,k):
    """d is the len of the sequence : looking for d-mers
    return a list of indices bwtn 1 and d"""
    return [rd.randint(0,d-1) for i in range(k)] 
    
    
def getHashCode(f,s1):
    """return the hash code of a sequence where s1 is a Serie and return a string"""
    return s1.iloc[f].values.sum()
    
def getAllDMers(serie,d,k):
    """takes d the len of the d-mers, k the number of random sample 
    f the hasging function
    takes the serie we want d mers
    return the tuples we want in a dataframe
    the index must be a number !! no datetime here"""
    f,n =getHashFunc(d,k),len(serie)
    out = pd.DataFrame()
    for index, row in serie.iteritems():
        if index<= n-d: 
            dmers = serie.iloc[index:index+d].reset_index(drop=True)
            out.loc[index,'code'] = getHashCode(f,dmers);out.loc[index,'index_value']=index
    return out
    
    
def getIndicesOfSameMers(serie,d,k):
    """return all indices with same mers, usually we use this function"""
    allMers = getAllDMers(serie,d,k)
    out = pd.DataFrame(index=allMers.index)
    result = allMers.groupby(['code'])
    out['nb'] = result.count().reset_index()['index_value']
    out['idx'] = result['index_value'].unique().reset_index()['index_value']
    out['code'] = result['index_value'].unique().reset_index()['code']
    
    return out[out['nb']>1]
    
    
    
  