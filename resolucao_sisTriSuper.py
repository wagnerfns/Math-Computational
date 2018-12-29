import numpy as np

matriz = np.array([[3,2,4], [0,1/3,2/3], [0,0,-8]])
vetor = np.array([1,5/3,0])

def sis_tria_super(a, b):
    n = b.size
    x = np.zeros(n)
    
    x[-1] = vetor[-1]/matriz[-1][-1]
    for i in range(n-1,-1,-1):
        s = 0
        for j in range(i+1, n):
            s = s + matriz[i][j] * x[j]
            x[i] = (vetor[i] - s)/matriz[i][i] 
            
    return(x)
print('def soluçao do sistema triangular superior: ', sis_tria_super(matriz, vetor))

print('soluçao do sistema triangular superior: ', np.linalg.solve(matriz,vetor))
