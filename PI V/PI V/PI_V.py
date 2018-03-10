import csv
import sys
import math
import random
import operator

#Carrega o arquivo CSV
def carregaDados(filename, divideConjunto, conjuntoTratado=[] , conjuntoTeste=[]):
    with open(filename, 'r') as csvfile:#Carrega como CSV File
        lines = csv.reader(csvfile)#Armazena os valores em linhas
        dataset = list(lines)#Cria uma lista

        #Passa pelos n elementos do dataset
        for x in range(len(dataset)):
            for y in range(4):#le os n elementos de cada linha
                dataset[x][y] = float(dataset[x][y])#Gera uma matriz de elementos do dataset
            if random.random() < divideConjunto:#Randomiza os valores, ve o que esta abaixo do float enviado e armazena nos conjuntos
                conjuntoTratado.append(dataset[x])
            else:
                conjuntoTeste.append(dataset[x])
        return dataset



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

def main():
    
    conjuntoTratado = []
    conjuntoTeste = []
    #carregaDados('DataCSV\iris.csv', 0.66, trainingSet, testSet)
    #print ('Train: ' + repr(len(trainingSet)))
    #print ('Test: ' + repr(len(testSet)))
    #trainSet = [[2, 2, 2, 'a'], [4, 4, 4, 'b'],[3,3,3,'a']]
    instanciaTeste = [0.78, 0.7,0.93]
    k = 8
    vizinhos = getVizinhos(carregaDados('DataCSV\iris.csv', 0.66, conjuntoTratado, conjuntoTeste), instanciaTeste, k)
    print ('Vizinhos: %s' % vizinhos)

    resultado = getResposta(vizinhos)
    
    print("Classe: %s" % resultado)

main()
