import numpy as np
import matplotlib.pyplot as plt


def iteracao_Divergente(new_array):
    x = new_array
    new_x= np.zeros(2)
    
    new_x[0] = -3 + (3 * x[1])
    new_x[1] =(3 - new_x[0])
    
    return(new_x)

def eq1_Divergente():
    limite = np.arange(-20, 30)
    eq1 = np.array([], dtype=float)
    for i in limite:
        aux = 3 - i
        eq1 = np.append(eq1, aux)
    return(eq1)

def eq2_Divergente():
    limite = np.arange(-20, 30)
    eq2 = np.array([], dtype=float)
    for i in limite:
        aux = (3 + i)/3
        eq2 = np.append(eq2, aux)
    return(eq2)

def plot_reta_Divergente():
    limite = np.arange(-20, 30)
    plt.plot(limite, eq1, "k-") #plota a reta
    plt.plot(limite, eq2, "k-") #plota a reta

def plot_ponto_Divergente():
    plt.plot(x0[0], x0[1], "r.", label="x0")
    plt.plot(x1[0], x1[1], "b.", label="x1")
    plt.plot(x2[0], x2[1], "g.", label="x2")
 
    plt.legend()
    plt.grid()
    
    plt.xlim([-20,30])
    plt.ylim([-20,30])
    
    plt.show()

print("\nx0 = {}".format(x0))

x1 = iteracao_Divergente(x0)
print("\nx1 = {}".format(x1))

x2 = iteracao_Divergente(x1)
print("\nx2 = {}".format(x2))

eq1 = eq1_Divergente() # Para construir as linhas

eq2 = eq2_Divergente()

plot_reta_Divergente()
plot_ponto_Divergente()