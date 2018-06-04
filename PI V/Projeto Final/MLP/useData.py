import numpy
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics.scorer import make_scorer
from sklearn.metrics import recall_score
from sklearn import svm

def cross(data):
    df_x = data.iloc[:,1:] #Matriz
    df_y = data.iloc[:,10] #Classes

    clf = svm.SVC(kernel='linear', C=1) #Name: 10, Length: 3020, dtype: int64
    scores = cross_val_score(clf, df_x, df_y, cv=10)
    predicted = cross_val_predict(clf, df_x, df_y, cv=10)

    print("Cross-Validation Score: ")
    for fold in range(len(scores)):
        print(str(fold+1) + "-K Fold Precision: " + str(scores[fold]))
    
    print("Cross-Validation Predicts: ")
    print(predicted)

def predictClass(testInstance,data):
    df_x = data.iloc[:,0:10] #Matriz
    df_y = data.iloc[:,10] #Classes

    print(df_x)
    #print(df_y)

    mlp = MLPClassifier(activation='logistic', solver='sgd', hidden_layer_sizes=(10,15))
    mlp.fit(df_x,df_y)

    print(mlp.predict(testInstance))

    
def main():

    animes_pd = pd.read_csv('input\\anime.csv', encoding = "ISO-8859-1")
    testInstance = [[1,20,4,4,2,12,13,5,2,0.00]]
    #cross(animes_pd)
    predictClass(testInstance,animes_pd)



main()
