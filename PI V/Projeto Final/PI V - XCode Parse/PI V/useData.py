import re
import numpy
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics.scorer import make_scorer
from sklearn.metrics import recall_score
from sklearn import svm

def predictClass(testInstance,mlp,df_x,df_y):
    
    df_x.drop(df_x.columns[[5,4,3]], axis=1, inplace=True)
    mlp.fit(df_x,df_y)
    
    prevision = mlp.predict(testInstance)
    
    return prevision

def main():
    
    mlp = MLPClassifier(hidden_layer_sizes=(10,15), solver='sgd',max_iter=600, random_state=1)
    animes_pd = pd.read_csv('anime.csv', encoding = "ISO-8859-1")
    
    df_x = animes_pd.iloc[:,2:11] #Matriz
    df_y = animes_pd.iloc[:,11] #Classes
    
    #id,current,producer,studio,font,generos[3],duracao,classificacao,n ep
    #test recebe = producer,studio,font,duracao,classificacao,n ep
    testInstance = [[20,4,12,1,4,4]]
    
    print('Resposta da instancia teste:')
    print(predictClass(testInstance,mlp,df_x,df_y))
    print('Precisao media nos dados e rotulos de teste fornecidos')
    print(mlp.score(df_x,df_y))
    print('Estimativas de probabilidade de cada classe:')
    proba = mlp.predict_proba(df_x)
    print(proba[11])



main()

