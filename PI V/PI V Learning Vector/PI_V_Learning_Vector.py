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

def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for i in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split
 
# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0
 
# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = algorithm(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		scores.append(accuracy)
	return scores

#calculo de distancia eucliadiana
def distanciaEuclidiana(instancia1, instancia2):
	distancia = 0.0
	for x in range(len(instancia1)-1):
		distancia += pow((instancia1[x] - instancia2[x]), 2)
	return math.sqrt(distancia)  

#calculo para achar a melhor unidade do conjunto tratado
def getMelhorUnidade(blocoCodigos, instaciaTeste):
    distancias = list()
    for tratamento in blocoCodigos:#transforma o TRATAMENTO em um bloco e calcula a distancia euclidiana do conjunto
        dist = distanciaEuclidiana(linhatratada, instancia2)
        distancias.append((blocoCodigos, dist))#cria a uma lista de distancias com o conjunto tratado e sua respectiva distancia
    distancias.sort(Key=lambda tup: tup[1])#ordena a lista da menor distancia pra maior
    return distancias[0][0]#retorna a menor distancia

def prever(blocoCodigos, linhaTeste):
	mu = getMelhorUnidade(blocoCodigos, linhaTeste)
	return mu[-1]

#Função para 'criar' ou 'encontrar' uma linha do bloco de códigos
def linhaTratada_Aleatoria(tratar):
    nRegistros = len(tratar)#tamanho dos registros
    nCaracteristicas = len(tratar[0])#tamanho de um registro
    linhaTratada = [tratar[randrange(nRegistros)][i] for i in range(nCaracteristicas)]#armazena a linha com a função randrange(gerar aleatórios inteiros)
    return linhaTratada

#Trata o bloco de códigos a partir das linhas 
def tratar_BlocoCodigos(conjunto, numBlocoCodigos, taxaLVQ, etapas):#etapas é Constante do decaimento da função taxa
    blocoCodigos = [linhaTratada_Aleatoria(conjunto) for i in range(numBlocoCodigos)]#atribui à variavel blocoCodigos as linha tratadas na quantidade de blocos(numBlocoCodigos)
    for etapa in range(etapas):
        taxa = taxaLQV * (1.0 - (etapa / float(etapas)))#taxa de aprendizado
        sErro=0.0
        for linha in conjunto:
            mu = getMelhorUnidade(blocoCodigos, linha)
            for i in range(len(linha)-1):
                erro = linha[i] - mu[i]
                sErro += erro ** 2
                if mu[-1] == linha[-1]:
                    mu[i] += taxa * erro
                else:
                    mu[i] -= taxa * erro
    return blocoCodigos

def learning_vector_quantization(conjunto, teste, numBlocoCodigos, taxaLVQ, etapas):
	blocoCodigos = tratar_BlocoCodigos(cconjunto, numBlocoCodigos, taxaLVQ, etapas)
	previsoes = list()
	for linha in teste:
		saida = prever(blocoCodigos, linha)
		previsoes.append(saida)
	return(previsoes)



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

