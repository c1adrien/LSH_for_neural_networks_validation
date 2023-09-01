#---------------------------------------------------------------#
#------------ Plotting results------------------------------------#
#---------------------------------------------------------------#

#The purpose of this code is to create a plot displaying two trajectories from our time series data that have been recognized as being similar.
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from utils.SAX import getting_SAX_notation,from_SAX_to_data

def trouver_ind_debut(lst1,lst2):
    ind=0
    for i in range(len(lst2)):
        if lst2[i:i+len(lst1)]==list(lst1):
            ind=i
    return ind,ind+len(lst1)
    
    
def show_similitudes(s1,index1,index2,numero_serie,events_base,differentes_series,k):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    val1 = pd.DataFrame(differentes_series[numero_serie[index1]])
    val1["Date"]=val1.index
    val1_notation,events_1 = getting_SAX_notation(val1,0.2)
    
    
    #
    
    val2 = pd.DataFrame(differentes_series[numero_serie[index2]])
    val2["Date"]=val2.index
    val2_notation,events_2 = getting_SAX_notation(val2,0.2)
    
    debut_1,fin_1 = trouver_ind_debut(s1.iloc[index1:index1+k].values,val1_notation)
    debut_2,fin_2 = trouver_ind_debut(s1.iloc[index2:index2+k].values,val2_notation)



    ax1.plot(differentes_series[numero_serie[index1]][0:int(events_base[numero_serie[index1]][debut_1:fin_1][0])+1],color="black")
    ax1.plot(differentes_series[numero_serie[index1]][int(events_base[numero_serie[index1]][debut_1:fin_1][0]):],color="black")

    #deuxieme serie, que l'on met aussi encouleur 
    ax1.plot(differentes_series[numero_serie[index2]][0:int(events_base[numero_serie[index2]][debut_2:fin_2][0])+1],color="black")
    ax1.plot(differentes_series[numero_serie[index2]][int(events_base[numero_serie[index2]][debut_2:fin_2][0]):],color="black")


    #les raccords

    ax1.plot(differentes_series[numero_serie[index1]][int(events_base[numero_serie[index1]][debut_1:fin_1][0]):int(events_base[numero_serie[index1]][debut_1:fin_1][-1])],color="orange",linewidth=6,label="Area of interest in the first trajectory")
    ax1.plot(differentes_series[numero_serie[index2]][int(events_base[numero_serie[index2]][debut_2:fin_2][0]):int(events_base[numero_serie[index2]][debut_2:fin_2][-1])],color="blue",linewidth=6,label="Area of interest in the second trajectory")
    ax1.legend()
    
    ax2.plot(from_SAX_to_data(s1.iloc[index1-k:index1+k].values),label="Reconstruction from the SAX code of the first serie") #+/-10
    ax2.plot(from_SAX_to_data(s1.iloc[index2-k:index2+k].values),label="reconstruction from the SAX code of the second serie") #+/-10
    ax2.legend()
    
    return debut_1,debut_2,fin_1,fin_2