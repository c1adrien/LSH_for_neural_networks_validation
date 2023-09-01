#---------------------------------------------------------------#
#------------ SAX and CUMSUM algorithm ------------------------------------#
#---------------------------------------------------------------#
import numpy as np 
import pandas as pd 
import numpy.random as rd 



def getDates(dataset,h):
    posDates,negDates = [],[]
    pos_sum,neg_sum = 0,0
    dataset["Differences"] = dataset["Close"].diff()
    
    for i,r in dataset[1:].iterrows():
        pos_sum = max(0,pos_sum + r["Differences"])
        neg_sum = min(0, neg_sum + r["Differences"])
        if pos_sum > h:
            pos_sum = 0 #Reset
            posDates.append(r["Date"])
        elif neg_sum < -h:
            neg_sum = 0 #Reset
            negDates.append(r["Date"])
    return posDates,negDates

#dataset should have columns ['Date','Close']
def getting_approximation(data,h):
    #directly calibrate the SAX serie to have exactly the same number of points on it. 
    posDates,negDates = getDates(data,h)
    events = sorted(posDates+negDates) 
    
    #we first start by giving the values of CUMSUM 
    last =0
    data["approx_CUMSUM"] = 0
    for e in events:
        data.iloc[last:int(e),3] = data.iloc[last:int(e),:]["Close"].mean()
        last =int(e)
    data.iloc[last:,3] = data.iloc[last:,:]["Close"].mean() #dernier point de données
    
    data["approx_SAX"] = 0    
    events_sax = np.arange(0,len(data),int(len(data)/len(events)))
    for e in events_sax:
        data.iloc[last:int(e),4] = data.iloc[last:int(e),:]["Close"].mean()
        last =int(e)
    data.iloc[last:,4] = data.iloc[last:,:]["Close"].mean() #dernier point de données
    
    return data,events,events_sax




def find_smallest_number(numbers, x):
    sorted_numbers = sorted(numbers)
    for number in reversed(sorted_numbers):
        if number < x:
            return number
    return None


def getting_SAX_notation(data,h):
    numbers = [-float('inf'), -1.28, -0.76, -0.84, -0.43, -0.52, -0.14, -0.25,
           0.14, 0, 0.43, 0.25, 0.76, 0.52, 1.22, 0.84, 1.28, float('inf')]
    #directly calibrate the SAX serie to have exactly the same number of points on it. 
    posDates,negDates = getDates(data,h)
    events = sorted(posDates+negDates) 
    
    #we first start by giving the values of CUMSUM 
    last =0
    out = []
    for e in events:
        val = data.iloc[last:int(e),:]["Close"].mean()
        out.append(str(find_smallest_number(numbers, val))) #on lui associe le "nombre" le plus proche
        last =int(e)
    out.append(str(find_smallest_number(numbers, data.iloc[last:,:]["Close"].mean()))) #dernier point de données
    
    
    return out,events

def from_SAX_to_data(sax_notations):
    sax_notations = np.array(sax_notations).astype(float)
    n = int(100/len(sax_notations))  # Change this to the number of times you want to repeat each number
    new_list = []
    for num in sax_notations:
        new_list.extend([num]*n)

    return new_list
    
    
    
def analyse_of_a_time_series_generator(generator):
    code_database = []
    numero_serie = []
    differentes_series = []
    events_base =[]
    for i in range(400):
    
        data1 = pd.DataFrame()
        data1["Close"] = np.cumsum(np.random.normal(0,1,100))
        m,sig = data1["Close"].mean(),np.var(data1["Close"])
   
        data1["Close"] = (data1["Close"]-data1["Close"].mean())/data1["Close"].var()
        data1["Date"] = data1.index
    
        #differentes_series.append(data1["Close"]*sig+m)
        differentes_series.append(data1["Close"])
    

        notation_sax,events =getting_SAX_notation(data1,0.2)
        code_database+= notation_sax#concatenate the code of the 2 lists 
        events_base.append(events)
        numero_serie+=len(notation_sax)*[i]
    return code_database ,numero_serie,events_base,differentes_series