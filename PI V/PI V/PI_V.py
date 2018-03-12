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

def treinoDadosRandom(divisor, trainingSet, testSet):
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
	for x in range(int(k)):
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

    print()
    crossValidation(iris,4,5,150)
    print()
    print()


def wine():
    print('==Wine==')
    wine = carregaDados('DadosKNN\wine.csv')
    for x in range (len(wine)):
        for y in range(13):
            wine[x][y] = float(wine[x][y])

    print()
    crossValidation(wine,13,13,178)
    print()
    print()


def wineQualityRed():
    print('==WineQualityRed==')
    wineQred = carregaDados('DadosKNN\winequalityredOutput.csv')
    for x in range (len(wineQred)):
        for y in range(11):
            wineQred[x][y] = float(wineQred[x][y])
    print()
    crossValidation(wineQualityRed,13,13,1599)
    print()
    print()

def wineQualityWhite():
    print('==WineQualitywhite==')
    wineQualitywhite = carregaDados('DadosKNN\winequalitywhiteOutput.csv')
    for x in range (len(wineQualitywhite)):
        for y in range(11):
            wineQualitywhite[x][y] = float(wineQualitywhite[x][y])

    print()
    crossValidation(wineQualityWhite,12,13,4898)
    print()
    print()


def breastCancer():
    print('==BreastCancer==')
    breastC = carregaDados('DadosKNN\eastcancer.csv')
    for x in range (len(breastC)):
        for y in range(10):
            breastC[x][y] = float(breastC[x][y])
    
    print()
    crossValidation(breastC,11,11,569)
    print()
    print()

def abalone():
    print('==Abalone==')
    abalone = carregaDados('DadosKNN\lone.csv')
    for x in range (len(abalone)):
        for y in range(8):
            abalone[x][y] = float(abalone[x][y])
    
    print()
    crossValidation(abalone,9,9,4177)
    print()
    print()


def adult():#TODO
    print('==Adult==')
    adult = carregaDados('DadosKNN\dult.csv')
    for x in range (len(adult)):
        for y in range(14):
            adult[x][y] = float(adult[x][y])

    print()
    crossValidation(adult,15,15,48842)
    print()
    print()

def preparaDataset(dataset, conjuntoTratado, conjuntoTeste,amostra,amostraInicial,coluna):


    for x in range(len(dataset)):
            for y in range(coluna):#le os n elementos de cada linha
                dataset[x][y] = float(dataset[x][y])#Gera uma matriz de elementos do dataset

            if (x >= (amostra - amostraInicial)) & (x < amostra):
                    conjuntoTeste.append(dataset[x])
            else:
                    conjuntoTratado.append(dataset[x])
                   

def crossValidation(dataset,coluna,m,linhas):
    amostra = int(linhas/10)
    amostraInicial = amostra
    trainingSet = []
    testSet = []
    acerto = erro = acertom2 = errom2 = acertom10 = errom10 = acertoq = erroq = erroCruzadov1nn = mediav1nn = erroCruzadom2 = erroCruzadom10 = erroCruzadoqnn = acertoqnn = erroqnn = 0
    

    for x in (range(0,10)):
       
       preparaDataset(dataset,trainingSet,testSet,amostra,amostraInicial,coluna)
       amostra+=amostraInicial   

       for y in (range(0,len(testSet))):
           
           #v1nn
           v1nn = getVizinhos(trainingSet,testSet[y],1)
           result = (getResposta(v1nn))
           atual = (testSet[y][-1])
           
           if result in atual:
               acerto+=1
           else:
               erro+=1

           #m2nn
           m2nn = getVizinhos(trainingSet,testSet[y],m+2)
           resultm2 = getResposta(m2nn)
           atualm2 = testSet[y][-1]

           if resultm2 in atualm2:
               acertom2+=1
           else:
               errom2+=1

           #m10nn
           m10 = getVizinhos(trainingSet,testSet[y],m*10+1)
           resultm10 = getResposta(m2nn)
           atualm10 = testSet[y][-1]

           if resultm10 in atualm10:
               acertom10+=1
           else:
               errom10+=1

           #qnn
           if ((int(trainingSet.index(trainingSet[-1]))/2)%2) == 0:
               qnn = getVizinhos(trainingSet,testSet[y],(trainingSet.index(trainingSet[-1])/2)+1)
           else:
               qnn = getVizinhos(trainingSet,testSet[y],int(trainingSet.index(trainingSet[-1])/2))

           resultqnn = getResposta(qnn)
           atualqnn = testSet[y][-1]

           if resultqnn in atualqnn:
               acertoqnn+=1
           else:
               erroqnn+=1


       
       del trainingSet[0:len(trainingSet)] 
       del testSet[0:len(testSet)]

       erroAmostral = (erro/(linhas-amostraInicial))*100
       erroCruzadov1nn += erroAmostral
       mediav1nn = erroCruzadov1nn/10

       erroAmostralm2 = (erro/(linhas-amostraInicial))*100
       erroCruzadom2 += erroAmostral
       mediam2 = erroCruzadom2/10

       erroAmostralm10 = (erro/(linhas-amostraInicial))*100
       erroCruzadom10 += erroAmostral
       mediam10 = erroCruzadom10/10

       erroAmostralqnn = (erro/(linhas-amostraInicial))*100
       erroCruzadoqnn += erroAmostral
       mediaqnn = erroCruzadom10/10


       print('Erro Amostral v1nn: %s' %erroAmostral)
       print('Erro Amostral m2: %s' %erroAmostralm2)
       print('Erro Amostral m10: %s' %erroAmostralm10)
       print('Erro Amostral qnn: %s' %erroAmostralqnn)
    print('Erro de Validação Cruzada v1nn: %s' %mediav1nn)
    print('Erro de Validação Cruzada m2: %s' %mediam2)
    print('Erro de Validação Cruzada m10: %s' %mediam10)
    print('Erro de Validação Cruzada qnn: %s' %mediaqnn)
       
def main():
    
    
    print('O teste a seguir pode demorar.')
    confirmacao = input('Deseja continuar? (s/n)    ')

    if(confirmacao == 's'):
        print()
        print()
        print('REALIZANDO CROSS VALIDATION DE TODOS OS DADOS')
        print()
        print()
        iris()
        wine()    
        wineQualityRed()
        wineQualityWhite()
        breastCancer()
        abalone()
        #adult()
    if(confirmacao == 'n'):
        print('Fim')
    else:
        print()
        print('Comando inválido')
        print('xxxCloseOperation')

main()