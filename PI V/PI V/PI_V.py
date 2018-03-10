import csv
import sys
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

def main():
    trainingSet=[]
    testSet=[]
    loadDataset('DataCSV\iris.csv', 0.66, trainingSet, testSet)
    print ('Train: ' + repr(len(trainingSet)))
    print ('Test: ' + repr(len(testSet)))

main()