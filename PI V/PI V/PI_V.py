import csv
import sys
import math
import random
import operator

#Carrega o arquivo CSV
def loadDataset(filename, divide_set, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:#Carrega como CSV File
	    lines = csv.reader(csvfile)#Armazena os valores em linhas
	    dataset = list(lines)#Cria uma lista

        #Passa pelos n elementos do dataset
	    for x in range(len(dataset)):
	        for y in range(4):#le os n elementos de cada linha
	            dataset[x][y] = float(dataset[x][y])#Gera uma matriz de elementos do dataset
	        if random.random() < divide_set:#Randomiza os valores, ve o que esta abaixo do float enviado e armazena nos conjuntos
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])
	    return dataset



#Acha vizinhos
#Recebe os conjuntos, sendo um de treino onde estão os dados com as classes, um de teste,
#onde estão as instâncias sem a classe(que você quer saber os vizinhos mais próximos),
#e o numero k de vizinhos a serem investigados.
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1#porque é um vetor


    #Fará o calculo euclidiano de distancia entre os n valores teste 
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))#Ordena o vetor de distancia['valores', distancia] pela distancia
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])#para o numero k de vizinhos, varre a matriz e obtém as instancias de vizinhos
	return neighbors


#calculo de distancia eucliadiana
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)


#Define a classe tendo como base os vizinhos
def getResponse(neighbors):
	classVotes = {}#Cria um Dict(Tipo um JSON)
	for x in range(len(neighbors)):#le ate o ultimo vizinho
		response = neighbors[x][-1]#armazena de cada linha o ultimo valor
		if response in classVotes:#se o valor armazenado pertence a um dict, incrementa esse valor
			classVotes[response] += 1
		else:#senão, cria um novo dict e define que existe 1 instancia
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)# Ordena os valores do maior pro menor
	return sortedVotes[0][0]


#verifica a precisao dos dados
def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] is predictions[x]: #se o test for igual a previsao, incrementa 1 aos corretos
			correct += 1
	return (correct/float(len(testSet))) * 100.0 #divide os corretos pelo total e transforma em porcentagem

def main():
    classVotes = {}
    trainingSet=[]
    testSet=[]
    loadDataset('DataCSV\iris.csv', 0.66, trainingSet, testSet)
    print ('Train: ' + repr(len(trainingSet)))
    print ('Test: ' + repr(len(testSet)))

    #trainSet = [[2, 2, 2, 'a'], [4, 4, 4, 'b'],[3,3,3,'a']]
    testInstance = [0.78, 0.7,0.93]
    k = 8
    neighbors = getNeighbors(loadDataset('DataCSV\iris.csv', 0.66, trainingSet, testSet), testInstance, k)
    print(neighbors)

    nyan = getResponse(neighbors)

    print(nyan)


main()