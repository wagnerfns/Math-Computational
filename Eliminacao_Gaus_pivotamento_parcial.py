import numpy as np


def troca_linha(A, b, linha_atual, linha_troca):
    # Numero de colunas
    # Troca as linhas da matriz
    
    c = A.shape[1] # Pega a quantidade de linhas
    
    primeira = A[linha_atual, 0:c].copy() # Copia a linha em questao
    
    # Troca as linhas da matriz
    A[linha_atual] = A[linha_troca]
    print("Nova linha ", linha_atual, ': ', A[linha_atual])
    
    A[linha_troca] = primeira
    print("Nova linha ", linha_troca, ': ', A[linha_troca])
    
    # Troca as linhas do vetor
    primeira = b[linha_atual].copy()
    b[linha_atual] = b[linha_troca]  
    b[linha_troca] = primeira

def analisa_pivo(A, b, linha_atual, coluna_atual):   
    maior = A[linha_atual, coluna_atual] # Primeiro elemento
    linha_troca = linha_atual
    for i in range(linha_atual, len(A)): # Procura um elemento maior naquela coluna
        
        print('i: ',i, ' -- elemento da matriz',i,'.',coluna_atual,':', abs(A[i, coluna_atual]), ' > pivo: ', abs(maior))
        
        if(abs(A[i, coluna_atual]) > abs(maior)):
            maior = A[i, coluna_atual]
            linha_troca = i
    troca_linha(A, b, linha_atual, linha_troca)

def pivot_gaus(matriz, vetor):
    n = matriz[0].size # tamanho
    x = np.zeros(n)
    
    if(np.linalg.det(matriz) == 0):                         # Melhoria 2
        print("Erro determinante é ", np.linalg.det(matriz))# Melhoria 2
    else:                                                   # Melhoria 2
              
        for k in range(0, n-1): # Linha
            
            analisa_pivo(matriz, vetor, k, k)
    
            print("\nColuna ", k)
            print("\nMatriz:\n", matriz)
            print("\nVetor: \n", vetor)
            print("\n\n")
            
            for i in range(k+1,n): # Coluna
                
                m = (matriz[i,k]/matriz[k,k])

                matriz[i,k] = 0

                for j in range(k+1, n):
                    matriz[i,j] = matriz[i,j] - (m * matriz[k,j])
                vetor[i] = vetor[i] - (m * vetor[k])          

        x[n-1] = vetor[n-1]/matriz[n-1, n-1]

        for k in range(n-1, -1, -1): # Linha
            soma = 0
            for j in range(0,n): # coluna
                soma = soma + matriz[k,j] * x[j]
                x[k]=(vetor[k] - soma)/matriz[k,k]
        
        print('Matriz')
        print(matriz)
        
        print("\n\nVetor")
        print(vetor)
        

        
matriz = np.array([[3,2,4,-1], [0,1,0,3], [0,-3,-5,7], [0,2,4,0]])
vetor  = np.array([5,6,7,15])


print("\nMatriz:\n", matriz)
print("\nVetor: \n", vetor)
print("\n\n")
pivot_gaus(matriz, vetor)