# hash chave % 100

'''
ex :
chave = 106
conta sobra 6
vai no endereço 6 e coloca o 106 la
chave = 102
conta sobra 2
vai no endereço 6 e coloca o 102 la
chave = 202
conta sobra 2
vai no endereço 6 e -> 202 

TO DO 
1 -> inserir chaves (chave % 100)
2 -> mostrar tabela hash criada
3 -> buscar uma chave

vetor com 99 posições todo zerado com null
End | Chave | Prox
0   |   1   |  ->
1   |   2   |
2   |  102  |  -> | 202 | -> 302 -> null

P.O Aula 6, 7, 8, 9, 10, 11
''' 
import pandas as pd
import numpy as np

#PEGAR O INPUT

op = 500
ok = False
df = pd.DataFrame([],columns=['Endereco', 'Chave'])
df.index = df['Endereco']
firstItem = 0
while (op != 0) :
    print("---------- Menu -------------")
    print("1 - Ver tabela")
    print("2 - Inserir na tabela")
    print("3 - Buscar na tabela")
    print("0 - Go Out")
    op = int(input("Digite a opcao:"))

    if (ok != False):
         del df['Endereco']
         ok = True
         
    if op == 1 :
        print(df)
    elif op == 2 :
        inputKey = int(input("Digite a chave a ser inserida:"))
        address = inputKey % 100
        if (address in df.index):
            i = df.index.get_loc(address)
            value = int(df.iloc[i]['Chave'])
            
            if (inputKey != value):
                columnsNumber = len(df.columns)
                founded = 0
                while (int(columnsNumber) >= 1):
                    nextField = "Proximo" + str(columnsNumber)
                    if nextField in df.columns:
                        if (np.isnan(df.iloc[i][nextField]) == False) :
                            value = int(df.iloc[i][nextField])
                            if (inputKey == value) :
                                founded = 1
                            else :
                                columnsNumber -= 1
                        else :
                            columnsNumber -= 1
                    else :
                        columnsNumber -= 1
                    
                if (founded == 0):
                    columnsNumber1 = len(df.columns) - 1
                    nextColumn = "Proximo" + str(columnsNumber1)
                    print("tem que ir pra row: ", i)
                    df.loc[address, nextColumn] = float(inputKey)
                    print("Numero inserido com sucesso")
            else :
                print("Numero ja inserido")
        else:
            print("aquie")
            df1 = pd.DataFrame([(address, int(inputKey))],columns=['Endereco', 'Chave'])
            df1.index = df1['Endereco']
            del df1['Endereco']
            df = df.append(df1, sort=False)
            if (firstItem == 0) :
                del df['Endereco']
                firstItem = 1
            print("Numero inserido com sucesso")
    elif op == 3 :
        #pegar uma linha do dataset, verificar se tem outro 
        inputKey = int(input("Digite a chave a ser buscada:"))
        address = inputKey % 100
        i = df.index.get_loc(address)
        toPrint = df.iloc[i:i+1]
        print(toPrint)
