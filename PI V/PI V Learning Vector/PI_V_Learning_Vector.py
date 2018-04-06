import csv
import sys
import math
import random 
import operator

#Enunciado https://docs.google.com/document/d/1Ikjw-XMH9Qz8V06GALQcGtT3nzZ7nK4rT0gO-ZlIXZw/edit 
#Ajuda para desenvolver o algoritmmo https://machinelearningmastery.com/implement-learning-vector-quantization-scratch-python/ 





#Carrega o arquivo CSV
def iris():
    print('==Iris==')
    iris = carrega_csv('Dados\iris.csv')
    irisLVQ = validacao_LVQ(iris,learning_vector_quantization,10,20,0.3,15,1)
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


def carrega_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = csv.reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

def cross_validation(dataset, n_folds):
	dataset_cross = list()
	dataset_copia = list(dataset)
	tamanhoFold = int(len(dataset) / n_folds)
	for i in range(n_folds):
		fold = list()
		while len(fold) < tamanhoFold:
			index = random.randrange(len(dataset_copia))
			fold.append(dataset_copia.pop(index))
		dataset_cross.append(fold)
	return dataset_cross

# Calculate accuracy percentage
def acuracia(atual, previsão):
	correto = 0
	for i in range(len(atual)):
		if atual[i] == previsão[i]:
			correto += 1
	return correto / float(len(atual)) * 100.0

# Validando o LVQ com o cross validation
def validacao_LVQ(dataset, algoritmo, n_folds, *args):
	folds = cross_validation(dataset, n_folds)#roda o cross com folds parametrizadas
	acertos = list()
	for fold in folds:
        #criando um conjunto e separando o tratamento do teste
		conjunto_tratamento = list(folds)
		conjunto_tratamento.remove(fold)
		conjunto_tratamento = sum(conjunto_tratamento, [])
		conjunto_teste = list()
		for linha in fold:#lista do conjunto teste
			linhaL = list(linha)
			conjunto_teste.append(linhaL)
			linhaL[-1] = None
		prever = algoritmo(conjunto_tratamento, conjunto_teste, *args)#chama o LVQ para a realização das previsões
		atual = [linha[-1] for linha in fold]
		acuracia = acuracia(atual, prever)#calculo para o Multiclasses
		acertos.append(acuracia)
	return acertos

#calculo de distancia eucliadiana
def distanciaEuclidiana(instancia1, instancia2):
	distancia = 0.0
	for x in range(len(instancia1)-1):
		distancia += (instancia1[x] - instancia2[x])**2
	return math.sqrt(distancia)  

#calculo para achar a melhor unidade do conjunto tratado
def getMelhoresUnidades(blocoCodigos, instanciaTeste, k):
    distancias = list()
    for tratamento in blocoCodigos:#transforma o TRATAMENTO em um bloco e calcula a distancia euclidiana do conjunto
        dist = distanciaEuclidiana(blocoCodigos, instanciaTeste)
        distancias.append((blocoCodigos, dist))#cria a uma lista de distancias com o conjunto tratado e sua respectiva distancia
    distancias.sort(Key=lambda tup: tup[1])#ordena a lista da menor distancia pra maior
    vizinhos = []
    for x in range(int(k)):
        vizinhos.append(distancia[x][0])#para o numero k de vizinhos, varre a lista e obtém as instancias de vizinhos
    return vizinhos

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

def prever(blocoCodigos, linhaTeste, k):
    mu = getMelhoresUnidades(blocoCodigos, linhaTeste, k)
    resposta = getResposta(mu)
    return resposta[-1]

#Função para 'criar' ou 'encontrar' uma linha do bloco de códigos
def linhaTratada_Aleatoria(tratar):
    nRegistros = len(tratar)#tamanho dos registros
    nCaracteristicas = len(tratar[0])#tamanho de um registro
    linhaTratada = [tratar[random.randrange(nRegistros)][i] for i in range(nCaracteristicas)]#armazena a linha com a função randrange(gerar aleatórios inteiros)
    return linhaTratada

#Trata o bloco de códigos a partir das linhas 
def tratar_BlocoCodigos(conjunto, numBlocoCodigos, taxaLVQ, etapas, k):#etapas é Constante do decaimento da função taxa
    blocoCodigos = [linhaTratada_Aleatoria(conjunto) for i in range(numBlocoCodigos)]#atribui à variavel blocoCodigos as linha tratadas na quantidade de blocos(numBlocoCodigos)
    for etapa in range(etapas):
        taxa = taxaLVQ * (1.0 - (etapa / float(etapas)))#taxa de aprendizado
        sErro=0.0
        for linha in conjunto:
            mu = getMelhoresUnidades(blocoCodigos, linha, k)
            resposta = getResposta(mu)
            for i in range(len(linha)-1):
                erro = linha[i] - resposta[i]
                sErro += erro ** 2
                if resposta[-1] == linha[-1]:
                    resposta[i] += taxa * erro
                else:
                    resposta[i] -= taxa * erro
    return blocoCodigos

#Função apenas compara se o LVQ acertou as classes
def learning_vector_quantization(conjunto, teste, numBlocoCodigos, taxaLVQ, etapas , k):
	blocoCodigos = tratar_BlocoCodigos(conjunto, numBlocoCodigos, taxaLVQ, etapas, k)
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
        '''wine()
        wineQualityRed()
        wineQualityWhite()
        breastCancer()
        abalone()
        adult()'''

        print('Processo encerrado')
    elif(confirmacao == 'n'):
        print('Fim')
    else:
        print()
        print('Comando inválido')
        print('xxxCloseOperation')

main()

