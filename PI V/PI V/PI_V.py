import csv
import sys
import math
import random
import operator

#Carrega o arquivo CSV
def carregaDados(filename):
    with open(filename, 'r') as csvfile:#Carrega como CSV File
        lines = csv.reader(csvfile)#Armazena os valores em linhas
        dataset = list(lines)#Cria uma lista
        return dataset

def treinoDados(divisor, trainingSet, testSet):
    for x in range(len(dataset)):
            for y in range(4):#le os n elementos de cada linha
                dataset[x][y] = float(dataset[x][y])#Gera uma matriz de elementos do dataset
            if random.random() < divideConjunto:#Randomiza os valores, ve o que esta abaixo do float enviado e armazena nos conjuntos
                conjuntoTratado.append(dataset[x])
            else:
                conjuntoTeste.append(dataset[x])

#Acha vizinhos
#Recebe os conjuntos, sendo um de treino onde estão os dados com as classes, um de teste,
#onde estão as instâncias sem a classe(que você quer saber os vizinhos mais próximos),
#e o numero k de vizinhos a serem investigados.
def getVizinhos(conjuntoTratado, instanciaTeste, k):
	distancia = []
	length = len(instanciaTeste)-1#porque é um vetor

    #Fará o calculo euclidiano de distancia entre os n valores teste 
	for x in range(len(conjuntoTratado)):
		dist = distanciaEuclidiana(instanciaTeste, conjuntoTratado[x], length)
		distancia.append((conjuntoTratado[x], dist))
	distancia.sort(key=operator.itemgetter(1))#Ordena o vetor de distancia['valores', distancia] pela distancia
	vizinhos = []
	for x in range(k):
		vizinhos.append(distancia[x][0])#para o numero k de vizinhos, varre a matriz e obtém as instancias de vizinhos
	return vizinhos


#calculo de distancia eucliadiana
def distanciaEuclidiana(instancia1, instancia2, length):
	distancia = 0
	for x in range(length):
		distancia += pow((instancia1[x] - instancia2[x]), 2)
	return math.sqrt(distancia)


#Define a classe tendo como base os vizinhos
def getResposta(vizinhos):
	classeVotos = {}#Cria um Dict(Tipo um JSON)
	for x in range(len(vizinhos)):#le ate o ultimo vizinho
		resposta = vizinhos[x][-1]#armazena de cada linha o ultimo valor
		if resposta in classeVotos:#se o valor armazenado pertence a um dict, incrementa esse valor
			classeVotos[resposta] += 1
		else:#senão, cria um novo dict e define que existe 1 instancia
			classeVotos[resposta] = 1
	votosOrdenados = sorted(classeVotos.items(), key=operator.itemgetter(1), reverse=True)# Ordena os valores do maior pro menor
	return votosOrdenados[0][0]


#verifica a precisao dos dados
def getPrecisao(conjuntoTeste, previsoes):
	correto= 0
	for x in range(len(conjuntoTeste)):
		if conjuntoTeste[x][-1] is previsoes[x]: #se o test for igual a previsao, incrementa 1 aos corretos
			correto += 1
	return (correto/float(len(conjuntoTeste))) * 100.0 #divide os corretos pelo total e transforma em porcentagem

def iris():
    
    print('==Iris==')
    iris = carregaDados('DadosKNN\iris.csv')
    for x in range(len(iris)):
         for y in range(4):
                iris[x][y] = float(iris[x][y])
    instanciaTeste = []
    instanciaTeste = [0.78, 0.7,0.93]
    vizinhos = getVizinhos(iris, instanciaTeste, 1)
    vizinhos_m2 = getVizinhos(iris, instanciaTeste, 7)
    vizinhos_m10 = getVizinhos(iris, instanciaTeste, 5*10+1)
    resultado = getResposta(vizinhos)
    print('1NN: ' + resultado)
    resultado = getResposta(vizinhos_m2)
    print('(M+2)-NN: ' + resultado)
    resultado = getResposta(vizinhos_m10)
    print('(M*10 + 1)-NN: ' + resultado)

def wine():
    print('==Wine==')
    wine = carregaDados('DadosKNN\wine.csv')
    for x in range (len(wine)):
        for y in range(13):
            wine[x][y] = float(wine[x][y])
    instanciaTeste = []
    instanciaTeste = [0.19,0.38,0.83,0.48,0.36,0.27,0.36,0.89,0.2,0.22,0.61,0.45,0.23]
    vizinhos = getVizinhos(wine, instanciaTeste, 1)
    vizinhos_m2 = getVizinhos(wine, instanciaTeste, 16)
    vizinhos_m10 = getVizinhos(wine, instanciaTeste, 14*10+1)
    resultado = getResposta(vizinhos)
    print('1NN: ' + resultado)
    resultado = getResposta(vizinhos_m2)
    print('(M+2)-NN: ' + resultado)
    resultado = getResposta(vizinhos_m10)
    print('(M*10 + 1)-NN: ' + resultado)


def wineQualityRed():
    print('==WineQualityRed==')
    wineQred = carregaDados('DadosKNN\winequalityredOutput.csv')
    for x in range (len(wineQred)):
        for y in range(11):
            wineQred[x][y] = float(wineQred[x][y])
    instanciaTeste = []
    instanciaTeste = [0.25,0.4,0,0.07,0.11,0.14,0.1,0.78,0.61,0.14,0.15]
    vizinhos = getVizinhos(wineQred, instanciaTeste, 1)
    vizinhos_m2 = getVizinhos(wineQred, instanciaTeste, 15)
    vizinhos_m10 = getVizinhos(wineQred, instanciaTeste, 13*10+1)
    resultado = getResposta(vizinhos)
    print('1NN: ' + resultado)
    resultado = getResposta(vizinhos_m2)
    print('(M+2)-NN: ' + resultado)
    resultado = getResposta(vizinhos_m10)
    print('(M*10 + 1)-NN: ' + resultado)


def wineQualityWhite():
    print('==WineQualitywhite==')
    wineQualitywhite = carregaDados('DadosKNN\winequalitywhiteOutput.csv')
    for x in range (len(wineQualitywhite)):
        for y in range(11):
            wineQualitywhite[x][y] = float(wineQualitywhite[x][y])
    instanciaTeste = []
    instanciaTeste = [0.31,0.19,0.22,0.31,0.1,0.15,0.37,0.21,0.25,0.27,0.13]
    vizinhos = getVizinhos(wineQualitywhite, instanciaTeste, 1)
    vizinhos_m2 = getVizinhos(wineQualitywhite, instanciaTeste, 15)
    vizinhos_m10 = getVizinhos(wineQualitywhite, instanciaTeste, 13*10+1)
    resultado = getResposta(vizinhos)
    print('1NN: ' + resultado)
    resultado = getResposta(vizinhos_m2)
    print('(M+2)-NN: ' + resultado)
    resultado = getResposta(vizinhos_m10)
    print('(M*10 + 1)-NN: ' + resultado)


def breastCancer():
    print('==BreastCancer==')
    breastC = carregaDados('DadosKNN\eastcancer.csv')
    for x in range (len(breastC)):
        for y in range(10):
            breastC[x][y] = float(breastC[x][y])
    instanciaTeste = []
    instanciaTeste = [18,1.00,0.67,0.67,0.56,0.33,1.00,0.33,0,0.11]
    vizinhos = getVizinhos(breastC, instanciaTeste, 1)
    vizinhos_m2 = getVizinhos(breastC, instanciaTeste, 13)
    vizinhos_m10 = getVizinhos(breastC, instanciaTeste, 11*10+1)
    resultado = getResposta(vizinhos)
    print('1NN: ' + resultado)
    resultado = getResposta(vizinhos_m2)
    print('(M+2)-NN: ' + resultado)
    resultado = getResposta(vizinhos_m10)
    print('(M*10 + 1)-NN: ' + resultado)

def abalone():
    print('==Abalone==')
    abalone = carregaDados('DadosKNN\lone.csv')
    for x in range (len(abalone)):
        for y in range(8):
            abalone[x][y] = float(abalone[x][y])
    instanciaTeste = []
    instanciaTeste = [0.52,0.52,0.08,0.18,0.15,0.13,0.15,0.50]
    vizinhos = getVizinhos(abalone, instanciaTeste, 1)
    vizinhos_m2 = getVizinhos(abalone, instanciaTeste, 11)
    vizinhos_m10 = getVizinhos(abalone, instanciaTeste, 9*10+1)
    resultado = getResposta(vizinhos)
    print('1NN: ' + resultado)
    resultado = getResposta(vizinhos_m2)
    print('(M+2)-NN: ' + resultado)
    resultado = getResposta(vizinhos_m10)
    print('(M*10 + 1)-NN: ' + resultado)

#def abalone():#TODO






def main():
    
    
    iris()

    wine()
    
    wineQualityRed()

    wineQualityWhite()

    breastCancer()

    abalone()
    #TODO
    '''
    adult()
    
    
    
    '''

main()