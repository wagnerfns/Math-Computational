import numpy as np

def gaus(matriz, vetor):
    n = matriz[0].size # tamanho
    x = np.zeros(n)
    

    if(np.linalg.det(matriz) == 0):                         # Melhoria 2
        print("Erro determinante é ", np.linalg.det(matriz))# Melhoria 2
    else:                                                   # Melhoria 2
        
        for k in range(0, n-1): # Linha
            
            if (matriz[k,k] == 0): # Melhoria 1
                    print("erro")  # Melhoria 1
                    break          # Melhoria 1
                    
            for i in range(k+1,n): # Coluna

                if(matriz[i,k] == 0):# Melhoria 1
                    continue         # Melhoria 1
                

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

        
matriz = np.array([[3., 2., 4.], [1., 1., 2.], [4., 3., -2.] ])
vetor  = np.array( [1., 2., 3.])
gaus(matriz, vetor)