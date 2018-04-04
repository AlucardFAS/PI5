import csv
import sys
import math
import random
import operator

#Enunciado https://docs.google.com/document/d/1Ikjw-XMH9Qz8V06GALQcGtT3nzZ7nK4rT0gO-ZlIXZw/edit 
#Ajuda para desenvolver o algoritmmo https://machinelearningmastery.com/implement-learning-vector-quantization-scratch-python/ 





#Carrega o arquivo CSV
def carregaDados(filename):
    with open(filename, 'r') as csvfile:#Carrega como CSV File
        lines = csv.reader(csvfile)#Armazena os valores em linhas
        dataset = list(lines)#Cria uma lista
        print('Dados carregados')
        return dataset

def iris():
    print('==Iris==')
    iris = carregaDados('Dados\iris.csv')
    for x in range(len(iris)):
         for y in range(4):
                iris[x][y] = float(iris[x][y])

    print('Dados passados para matriz')
    print()
    print()

def wine():
    print('==Wine==')
    wine = carregaDados('Dados\wine.csv')
    for x in range (len(wine)):
        for y in range(13):
            wine[x][y] = float(wine[x][y])

    print('Dados passados para matriz')
    print()
    print()

def wineQualityRed():
    print('==WineQualityRed==')
    wineQred = carregaDados('Dados\winequalityredOutput.csv')
    for x in range (len(wineQred)):
        for y in range(11):
            wineQred[x][y] = float(wineQred[x][y])
    print('Dados passados para matriz')
    print()
    print()

def wineQualityWhite():
    print('==WineQualitywhite==')
    wineQualitywhite = carregaDados('Dados\winequalitywhiteOutput.csv')
    for x in range (len(wineQualitywhite)):
        for y in range(11):
            wineQualitywhite[x][y] = float(wineQualitywhite[x][y])

    print('Dados passados para matriz')
    print()
    print()

def breastCancer():
    print('==BreastCancer==')
    breastC = carregaDados('Dados\eastcancer.csv')
    for x in range (len(breastC)):
        for y in range(10):
            breastC[x][y] = float(breastC[x][y])
    
    print('Dados passados para matriz')
    print()
    print()

def abalone():
    print('==Abalone==')
    abalone = carregaDados('Dados\lone.csv')
    for x in range (len(abalone)):
        for y in range(8):
            abalone[x][y] = float(abalone[x][y])
    
    print('Dados passados para matriz')
    print()
    print()

def adult():
    print('==Adult==')
    adult = carregaDados('Dados\dult.csv')
    for x in range (len(adult)):
        for y in range(14):
            adult[x][y] = float(adult[x][y])

    print('Dados passados para matriz')
    print()
    print()

#calculo de distancia eucliadiana
def distanciaEuclidiana(instancia1, instancia2):
	distancia = 0.0
	for x in range(len(instancia1)-1):
		distancia += pow((instancia1[x] - instancia2[x]), 2)
	return math.sqrt(distancia)  

#calculo para achar a melhor unidade do conjunto tratado
def getMelhorUnidade(conjuntoTratado, instaciaTeste):
    distancias = list()
    for tratamento in conjuntoTratado:#transforma o TRATAMENTO em um conjunto tratado e calcula a distancia euclidiana do conjunto
        dist = distanciaEuclidiana(linhatratada, instancia2)
        distancias.append((conjuntoTratado, dist))#cria a uma lista de distancias com o conjunto tratado e sua respectiva distancia
    distancias.sort(Key=lambda tup: tup[1])#ordena a lista da menor distancia pra maior
    return distancias[0][0]#retorna a menor distancia

def linhaTratada_Aleatoria(tratar):
    nRegistros = len(tratar)
    nCaracteristicas = len(tratar[0])
    linhaTratada = [tratar[randrange(nRegistros)][i] for i in range(nCaracteristicas)]


def main():
    
    
    print('O teste a seguir pode demorar.')
    confirmacao = input('Deseja continuar? (s/n)    ')

    if(confirmacao == 's'):
        print()
        print()
        print()
        print()
        print()
        iris()
        wine()
        wineQualityRed()
        wineQualityWhite()
        breastCancer()
        abalone()
        adult()

        print('Processo encerrado')
    elif(confirmacao == 'n'):
        print('Fim')
    else:
        print()
        print('Comando inválido')
        print('xxxCloseOperation')

main()

