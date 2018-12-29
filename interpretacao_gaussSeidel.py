import numpy as np
import matplotlib.pyplot as plt

def iteracao_GaussSeidel(new_array):
    x = new_array
    new_x= np.zeros(2)
    
    new_x[0] = 3 - x[1]
    new_x[1] =(3 + new_x[0])/3
    
    return(new_x)

def eq1_Seidel():
    limite = np.arange(-5, 6)
    eq1 = np.array([], dtype=float)
    for i in limite:
        aux = 3 -i
        eq1 = np.append(eq1, aux)
    return(eq1)

def eq2_Seidel():
    limite = np.arange(-5, 6)
    eq2 = np.array([], dtype=float)
    for i in limite:
        aux = (3 + i)/3
        eq2 = np.append(eq2, aux)
    return(eq2)

# Novo plot pq a quantidade de pontos é menor
def plot_ponto_Seidel():
    plt.plot(x0[0], x0[1], "r.", label="x0")
    plt.plot(x1[0], x1[1], "b.", label="x1")
    plt.plot(x2[0], x2[1], "g.", label="x2")
    plt.plot(x3[0], x3[1], "y.", label="x3")
 
    plt.legend()
    plt.grid()
    
    plt.xlim([-5,5])
    plt.ylim([-5,5])
    
    plt.show()


# Interpretação para o método Gauss-Seidel

print("\nx0 = {}".format(x0))

x1 = iteracao_GaussSeidel(x0)
print("\nx1 = {}".format(x1))

x2 = iteracao_GaussSeidel(x1)
print("\nx2 = {}".format(x2))

x3 = iteracao_GaussSeidel(x2)
print("\nx3 = {}".format(x3))



eq1 = eq1_Seidel()# Para construir as linhas

eq2 = eq2_Seidel()

plot_reta()
plot_ponto_Seidel()