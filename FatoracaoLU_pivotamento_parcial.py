import numpy as np

# auxiliar de transformacao
def factorizationLU_with_partialPivoting(A,b):
    
    print("Matriz A: \n{}".format(A))
    
    n = np.shape(A)[0]
    #m = np.zeros(n)
    m = float
    p = []
    r = int
    
    
    for i in range(0, n): # Cria um vetor para auxiliar a troca de linhas da matriz identidade
        p.append(i)
    
    print("\nCriando P: {}".format(p))
    
    for k in range(0, n-1):
        pv = abs(A[k,k])
        r = k
        
        for i in range(k+1, n):
            print("\nProcurando um elemento maior que {} na coluna".format(A[k,k]))
            
            if(abs(A[i,k]) > pv):
                pv = abs(A[i,k])
                r = i
                print("\nO elemento maior encontrado foi {}".format(A[i,k]))

        if(pv == 0):
            print("A matriz A é singular")
            break
        elif(r != k):
            aux  = p[k]
            p[k] = p[r]
            p[r] = aux 
            
            # Faz isso para saber quais linhas foram trocadas - P faz papel de "ontrolador"
            print("\nNova ordem de P: {}".format(p))
            
            for j in range(0, n):
                # Troca da matriz principal
                aux    = A[k,j]
                A[k,j] = A[r,j]
                A[r,j] = aux
            print("\nTroca de elementos da matriz principal\n{} \n".format(r,k,A))
              
        for i in range(k+1, n):
            m = A[i,k]/A[k,k]
            A[i,k] = m
            for j in range(k+1, n):
                A[i,j] = A[i,j] - (m * A[k,j])
                
        print("Nova versão da matriz: \n{}".format(A))
        

    # Resolução dos sistemas triangulares
    
    
    # Reordena b para as mudanças que ocorreram no controlador p, salvando tudo em uma novo vetor c
    c = []
    for i in range(n): # c = pb
        r   = p[i]
        c.append(b[r])
  
    print("\nVetor c criado: {}".format(c))
    
    
    # Resolução de Ly = c
    y = np.copy(b)
    for i in range(n):
        soma = 0
        for j in range(0, i-1):
            soma = soma + (A[j,i] * y[j])
        y[i]= c[i] - soma

     

    # Resolução de Ux = y
    x = np.zeros(n)
    x[n-1] = b[n-1]/A[n-1, n-1]
    
    for i in range(n-1, -1, -1):
        soma = 0
        
        for j in range(i+1,n):
            soma = soma + A[i,j]*x[j]
        x[i]= (y[i] - soma)/A[i,i]
    
    
    print("\n\nY: {}".format(y))
    print("\n\nX: {}".format(x))




A = np.matrix([[3,1,4],[1,5,9],[2,6,5]])
b = np.array([9,3,-2])

factorizationLU_with_partialPivoting(A,b)