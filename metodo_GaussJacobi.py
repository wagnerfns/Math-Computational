import numpy as np

def jacobiMethod(A, b, x0, iteracoes, limite):
    n = len(A) # tamanho da matriz
    it = 1 # iteracao
    
    while(it <= iteracoes):
        x = np.zeros(n)
        
        for i in range(n):
            for j in range(i):
                x[i] -= A[i,j]*x0[j]
                
            for j in range(i+1, n):
                x[i] -= A[i,j] * x0[j]
                
                
            x[i] = (x[i] + b[i])/A[i,i]
            
            print("\nValor de x: {}".format(x))
            
        if(np.linalg.norm(x-x0) < limite): #Verificar limite de erro
            return(x,it)
        
        it+=1
        x0 = np.copy(x)
        
        
    return x0, it


A = np.array([[10,-1,2,0 ],
              [-1,11,-1,3],
              [2,-1,10,-1],
              [0,3,-1, 8]])

b = np.array([6,25,-11,15])

x0 = np.zeros(len(A))

limite = 0.0000001 # limite de erro

iteracoes = 25 # Quantidade de iteracoes

print("\njacobiMethod\n")
x, n = jacobiMethod(A, b, x0, iteracoes, limite)
print("\n\nValor de x pelo metodo de Jacobi: {} em {} iterações".format(x, n))