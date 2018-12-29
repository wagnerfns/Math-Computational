import numpy as np


def gaussSeidelMethod(A, b, x0, iteracoes, limite):
    n = len(A)
    k = 1
    
    while(k <= iteracoes):
        x = np.zeros(n)
        for i in range(n):
            s = 0.0
            
            for j in range(i):
                s += A[i,j] * x[j]
                
            for j in range(i+1, n):
                s += A[i,j] * x0[j]
                
            x[i] = (b[i] - s)/A[i,i]
            
            print("\nValor de x: {}".format(x))
            
            if(np.linalg.norm(x-x0) < limite):
                return(x, k)
            
            k+=1
            
            x0 = np.copy(x)
    
    return(x0, k)


A = np.array([[10,-1,2,0 ],
              [-1,11,-1,3],
              [2,-1,10,-1],
              [0,3,-1, 8]])

b = np.array([6,25,-11,15])

x0 = np.zeros(len(A))

limite = 0.0000001 # limite de erro

iteracoes = 25 # Quantidade de iteracoes

print("\n\n\ngaussSeidelMethod\n")
x, n = gaussSeidelMethod(A, b, x0, iteracoes, limite)

print("\n\nValor de x pelo metodo de Seidel: {} em {} iterações".format(x, n))