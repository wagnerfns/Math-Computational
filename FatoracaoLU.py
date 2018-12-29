import numpy as np

def factorLU(A):  
    U = np.copy(A) # Copia pra U 
    n = np.shape(U)[0]  # Recebe o tamanho
    L = np.eye(n) # Cria uma matriz com 1 na diagonal principal e zero nos outros pontos
    identidade = np.eye(n)
    for j in np.arange(n-1): # 0, 1  
        for i in np.arange(j+1,n): # 1, 2 | 2 
            L[i,j] = U[i,j]/U[j,j]  # divide o elemento abaixo do pivo pelo pivo, vai adicionar os multiplicadores em L
            for k in np.arange(j+1,n): # multiplica U pelos multiplicadores 
                U[i,k] = U[i,k] - L[i,j]*U[j,k] # 1,2 | 1,2 | 2
            U[i,j] = 0 # Adiciona zero abaixo do pivo
    return(L, U)

def solvingL(L, b):
    n = len(A)
    for i in np.arange(n):
        pivo = b[i]

        for j in np.arange(n):
            if(j > i):
                b[j] = b[j] + round((L[j,i]*-1),2) * pivo # Multiplica L *multiplicadores* com o pivo e soma com b

    return(np.copy(b))

def solvingU(A, b):
    n = len(A)
    x = np.zeros(n)
    x[n-1] = b[n-1]/A[n-1, n-1]

    for k in range(n-1, -1, -1): # Linha
        soma = 0
        for j in range(0,n): # coluna
            soma = soma + A[k,j] * x[j]
        x[k]=(b[k] - soma)/A[k,k]
    
    return(x)

def rounding(x):
    for i in np.arange(len(x)):
        x[i] = round(x[i], 0)


A = np.matrix([[3,2,4],[1,1,2],[4,3,2]], dtype=float)
b = np.array([1,2,3], dtype=float)
print("Solução nutella: {}".format(np.linalg.solve(A, b)))
L, U = factorLU(A)
# i) Ly = b
y = solvingL(L, b)
# ii) Ux = y
x = solvingU(U,y)
rounding(x)
print("Solução raiz: {}".format(x))