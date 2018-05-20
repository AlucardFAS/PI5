import csv
import numpy
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

def carregaDados(filename):
    with open(filename, 'r') as csvfile:#Carrega como CSV File
        lines = csv.reader(csvfile)#Armazena os valores em linhas
        dataset = list(lines)#Cria uma lista
        return dataset

def MLP_use(data):
    df_x = data.iloc[:,1:]
    df_y = data.iloc[:,0]

    x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size = 0.2, random_state = 4)
    mlp = MLPClassifier(activation='logistic', solver='sgd', hidden_layer_sizes=(400,750), random_state=1)
    print("MLP parâmetros")
    print(mlp)
    print()
    mlp.fit(x_train, y_train)
    print("mlp 2")
    print(mlp)
    print()
    pred = mlp.predict(x_test)
    print("pred")
    print(pred)
    print()

    a = y_test.values
    print("a")
    print(a)
    print()
    count = 0

    for i in range(len(pred)):
        if pred[i] == a[i]:
            count = count+1

    print(count)
    print(len(pred))
    print(count/len(pred))

def main():

    #animes = carregaDados('input\\anime.csv')
    animes = pd.read_csv('input\\anime.csv', encoding = "ISO-8859-1")
    MLP_use(animes)




main()
