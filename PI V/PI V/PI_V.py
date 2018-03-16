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
		vizinhos.append(distancia[x][0])#para o numero k de vizinhos, varre a lista e obtém as instancias de vizinhos
	return vizinhos

#Divisão segura para o caso ZERO
def divisaoSegura(x, y):
    return 0 if y == 0 else x / y

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


def iris():
    print('==Iris==')
    iris = carregaDados('DadosKNN\iris.csv')
    for x in range(len(iris)):
         for y in range(4):
                iris[x][y] = float(iris[x][y])

    print()
    crossValidation(iris,4,5,150,0)
    print()
    print()


def wine():
    print('==Wine==')
    wine = carregaDados('DadosKNN\wine.csv')
    for x in range (len(wine)):
        for y in range(13):
            wine[x][y] = float(wine[x][y])

    print()
    crossValidation(wine,13,13,179,0)
    print()
    print()


def wineQualityRed():
    print('==WineQualityRed==')
    wineQred = carregaDados('DadosKNN\winequalityredOutput.csv')
    for x in range (len(wineQred)):
        for y in range(11):
            wineQred[x][y] = float(wineQred[x][y])
    print()
    crossValidation(wineQred,11,13,1599,0)
    print()
    print()

def wineQualityWhite():
    print('==WineQualitywhite==')
    wineQualitywhite = carregaDados('DadosKNN\winequalitywhiteOutput.csv')
    for x in range (len(wineQualitywhite)):
        for y in range(11):
            wineQualitywhite[x][y] = float(wineQualitywhite[x][y])

    print()
    crossValidation(wineQualitywhite,11,13,4898,0)
    print()
    print()


def breastCancer():
    print('==BreastCancer==')
    breastC = carregaDados('DadosKNN\eastcancer.csv')
    for x in range (len(breastC)):
        for y in range(10):
            breastC[x][y] = float(breastC[x][y])
    
    print()
    crossValidation(breastC,10,11,569,1)
    print()
    print()

def abalone():
    print('==Abalone==')
    abalone = carregaDados('DadosKNNs\lone.csv')
    for x in range (len(abalone)):
        for y in range(8):
            abalone[x][y] = float(abalone[x][y])
    
    print()
    crossValidation(abalone,8,9,4177,0)
    print()
    print()


def adult():
    print('==Adult==')
    adult = carregaDados('DadosKNN\dult.csv')
    for x in range (len(adult)):
        for y in range(14):
            adult[x][y] = float(adult[x][y])

    print()
    crossValidation(adult,15,15,48842,1)
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
                   
def multiclasses(pontosAcertados,pontosErrados):
    precisao = acuracia = 0
    for x in (range(0,10)):
        precisao += (pontosAcertados/(pontosAcertados + pontosErrados))*10
        acuracia = precisao/10

    return acuracia



def crossValidation(dataset,coluna,m,linhas,tipoclasse):
    myfile = open('result.txt','a')

    amostra = int(linhas/10)
    amostraInicial = amostra
    trainingSet = []
    testSet = []
    acerto = erro = acertom2 = errom2 = acertom10 = errom10 = acertoqnn = erroqnn = erroCruzadov1nn = mediav1nn = erroCruzadom2 = erroCruzadom10 = erroCruzadoqnn = 0
    acuracia = acuraciam2 = acuraciam10 = acuraciaqnn = tp = fp = tn = fn = tp2 = fp2 = tn2 = fn2 = tp10 = fp10 = tn10 = fn10 = tpnn = fpnn = tnnn = fnnn = sensibilidade = especificidade = precisaoBinaria = revocacao = 0
    sensibilidade2 = especificidade2 = precisaoBinaria2 = revocacao2 = sensibilidade10 = especificidade10 = precisaoBinaria10 = revocacao10 = sensibilidadenn = especificidadenn = precisaoBinariann = revocacaonn = 0
    i = 0
    for x in (range(0,10)):
       i+=1
       preparaDataset(dataset,trainingSet,testSet,amostra,amostraInicial,coluna)
       amostra+=amostraInicial   

       for y in (range(0,len(testSet))):
           
           #v1nn
           v1nn = getVizinhos(trainingSet,testSet[y],1)
           result = (getResposta(v1nn))
           atual = (testSet[y][-1])

           #binario TP TN FP FN
           if tipoclasse is 1:
                if 0 is result:
                    if result is atual:
                        tn+=1
                    else:
                        fn+=1
                else:
                    if result is atual:
                        tp+=1
                    else:
                        fp+=1

           if result is atual:
               acerto+=1
           else:
               erro+=1

           #m2nn
           m2nn = getVizinhos(trainingSet,testSet[y],m+2)
           resultm2 = getResposta(m2nn)
           atualm2 = testSet[y][-1]

           # binario TP TN FP FN
           if tipoclasse is 1:
               if 0 is resultm2:
                   if resultm2 is atualm2:
                       tn2 += 1
                   else:
                       fn2 += 1
               else:
                   if resultm2 is atualm2:
                       tp2 += 1
                   else:
                       fp2 += 1

           if resultm2 is atualm2:
               acertom2+=1
           else:
               errom2+=1


           #m10nn
           m10 = getVizinhos(trainingSet,testSet[y],m*10+1)
           resultm10 = getResposta(m2nn)
           atualm10 = testSet[y][-1]

           # binario TP TN FP FN
           if tipoclasse is 1:
               if 0 is resultm10:
                   if resultm10 is atualm10:
                       tn10 += 1
                   else:
                       fn10 += 1
               else:
                   if resultm10 is atualm10:
                       tp10 += 1
                   else:
                       fp10 += 1

           if resultm10 is atualm10:
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

           #print(resultqnn)
           # binario TP TN FP FN
           if tipoclasse is 1:
               if 0 is resultqnn:
                   if resultqnn is atualqnn:
                       tnnn += 1
                   else:
                       fnnn += 1
               else:
                   if resultqnn is atualqnn:
                       tpnn += 1
                   else:
                       fpnn += 1

           if resultqnn is atualqnn:
               acertoqnn+=1
           else:
               erroqnn+=1


       #Função clear para realizar um novo kFold
       del trainingSet[0:len(trainingSet)] 
       del testSet[0:len(testSet)]

       if tipoclasse is 0:
           acuracia += multiclasses(acerto,erro)
           acuraciam2 += multiclasses(acertom2,errom2)
           acuraciam10 += multiclasses(acertom10,errom10)
           acuraciaqnn += multiclasses(acertoqnn,erroqnn)



       
       #Calculos de Erro Amostral, Erro d Validação Cruzado e Acurácia
           #v1nn
       erroAmostral = (erro/(linhas-amostraInicial))*100
       erroCruzadov1nn += erroAmostral
       mediav1nn = erroCruzadov1nn/10
       
           #m2
       erroAmostralm2 = (errom2/(linhas-amostraInicial))*100
       erroCruzadom2 += erroAmostralm2
       mediam2 = erroCruzadom2/10
       
       
           #m10
       erroAmostralm10 = (errom10/(linhas-amostraInicial))*100
       erroCruzadom10 += erroAmostralm10
       mediam10 = erroCruzadom10/10
       
       print("k %d de Fold\n" % i)
           #qnn
       erroAmostralqnn = (erroqnn/(linhas-amostraInicial))*100
       erroCruzadoqnn += erroAmostralqnn
       mediaqnn = erroCruzadoqnn/10
       myfile.write("k %d Fold\n" %i)
       myfile.write("Erro Amostral v1nn: %f  Erro Amostral m2: %f  Erro Amostral m10: %f  Erro Amostral qnn: %f\n" % (erroAmostral,erroAmostralm2,erroAmostralm10,erroAmostralqnn))
       myfile.write("\n")
    myfile.write("Validação Cruzada\n")
    myfile.write("Erro de Validação Cruzada v1nn: %f  Erro de Validação Cruzada m2: %f  Erro de Validação Cruzada m10: %f  Erro de Validação Cruzada qnn: %f\n" % (mediav1nn,mediam2,mediam10,mediaqnn))

    if tipoclasse is 0:
        myfile.write("Precisão\n")
        myfile.write("Precisão v1nn: %f  Precisão m2: %f  Precisão m10: %f  Precisão qnn: %f\n" % (acuracia,acuraciam2,acuraciam10,acuraciaqnn))
        myfile.write("\n")

    if tipoclasse is 1:
        sensibilidade = divisaoSegura(tp ,(tp + fn))
        especificidade = divisaoSegura(tn , (tn + fp))
        precisaoBinaria = divisaoSegura(tp , (tp + fp))
        revocacao = divisaoSegura(tn , (tn + fn))
        sensibilidade2 = divisaoSegura(tp2 , (tp2 + fn2))
        especificidade2 = divisaoSegura(tn2 , (tn2 + fp2))
        precisaoBinaria2 = divisaoSegura(tp2 , (tp2 + fp2))
        revocacao2 = divisaoSegura(tn2 , (tn2 + fn2))
        sensibilidade10 = divisaoSegura(tp10 , (tp10 + fn10))
        especificidade10 = divisaoSegura(tn10 , (tn10 + fp10))
        precisaoBinaria10 = divisaoSegura(tp10 , (tp10 + fp10))
        revocacao10 = divisaoSegura(tn10 , (tn10 + fn10))
        sensibilidadenn = divisaoSegura(tpnn , (tpnn + fnnn))
        especificidadenn = divisaoSegura(tnnn , (tnnn + fpnn))
        precisaoBinariann = divisaoSegura(tpnn , (tpnn + fpnn))
        revocacaonn = divisaoSegura(tnnn , (tnnn + fnnn))
        myfile.write("Acertos: %f Erros: %f\n" % (acerto, erro))
        myfile.write("Matriz Confusão\n")
        myfile.write("v1nn: TP: %f - TN: %f - FP: %f - FN: %f\n" % (tp, tn, fp, fn))
        myfile.write("m2: TP: %f - TN: %f - FP: %f - FN: %f\n" % (tp2, tn2, fp2, fn2))
        myfile.write("m10: TP: %f - TN: %f - FP: %f - FN: %f\n" % (tp10, tn10, fp10, fn10))
        myfile.write("qnn: TP: %f - TN: %f - FP: %f - FN: %f\n" % (tpnn, tnnn, fpnn, fnnn))
        myfile.write("Sensibilidade v1nn: %f  Sensibilidade m2: %f  Sensibilidade m10: %f  Sensibilidade qnn: %f\n" % (
            sensibilidade, sensibilidade2, sensibilidade10, sensibilidadenn))
        myfile.write(
            "Especificidade v1nn: %f  Especificidade m2: %f  Especificidade m10: %f  Especificidade qnn: %f\n" % (
                especificidade, especificidade2, especificidade10, especificidadenn))
        myfile.write("Precisão v1nn: %f  Precisão m2: %f  Precisão m10: %f  Precisão qnn: %f\n" % (
            precisaoBinaria, precisaoBinaria2, precisaoBinaria10, precisaoBinariann))
        myfile.write("Revocação v1nn: %f  Revocação m2: %f  Revocação m10: %f  Revocação qnn: %f\n" % (
            revocacao, revocacao2, revocacao10, revocacaonn))
        myfile.write("\n")

    myfile.close()   



       
       
def main():
    
    
    print('O teste a seguir pode demorar.')
    confirmacao = input('Deseja continuar? (s/n)    ')

    if(confirmacao == 's'):
        print()
        print()
        print('REALIZANDO CROSS VALIDATION DE TODOS OS DADOS')
        print()
        print()
        #iris()
        #wine()
        #wineQualityRed()
        #wineQualityWhite()
        #breastCancer()
        #abalone()
        adult()
    if(confirmacao == 'n'):
        print('Fim')
    else:
        print()
        print('Comando inválido')
        print('xxxCloseOperation')

main()
