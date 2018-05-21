import numpy
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

def MLP_use(data):
    df_x = data.iloc[:,1:] #Matriz
    df_y = data.iloc[:,10] #Classes

    x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size = 0.2, random_state = 4)
    mlp = MLPClassifier(activation='logistic', solver='sgd', hidden_layer_sizes=(10,15), random_state=1)
    mlp.fit(x_train, y_train)
    pred = mlp.predict(x_test)

    a = y_test.values
    count = 0

    for i in range(len(pred)):
        if pred[i] == a[i]:
            count = count+1

    print('Acertos: ')
    print(count)
    print('Quantidade de testes: ')
    print(len(pred))
    print('Precisão: ')
    print((100*(count/len(pred))))
    
def main():

    animes_pd = pd.read_csv('input\\anime.csv', encoding = "ISO-8859-1")
    MLP_use(animes_pd)



main()
