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

def predictClass(testInstance,data):
    df_x = data.iloc[:,2:11] #Matriz
    df_y = data.iloc[:,11] #Classes

    matrix = df_x.values.T.tolist()

    third = matrix.pop(7)
    second = matrix.pop(6)
    first = matrix.pop(5)

    genresList = []

    #for x in range(0, len(first)):
        
        #genres = []

        #if re.search('[a-zA-Z]', first[x]) is None:
         #   genres.append(int(first[x]))
        #if re.search('[a-zA-Z]', second[x]) is None:
        #    genres.append(int(second[x]))
       # if re.search('[a-zA-Z]', third[x]) is None:
        #    genres.append(int(third[x]))

       # genresList.append(genres)

    
    df_x.drop(df_x.columns[[5,4,3]], axis=1, inplace=True)
    #print(genres)
    print(df_x)

    #series = pd.Series(genresList)
    #df_x['genres'] = series.values 

    #print(df_x)

    mlp = MLPClassifier(activation='logistic', solver='sgd', hidden_layer_sizes=(10,15))
    mlp.fit(df_x,df_y)

    print(mlp.predict(testInstance))

    
def main():

    animes_pd = pd.read_csv('input\\anime.csv', encoding = "ISO-8859-1")
    testInstance = [[1,1,1,4,1,1]]
    #cross(animes_pd)
    predictClass(testInstance,animes_pd)




main()
