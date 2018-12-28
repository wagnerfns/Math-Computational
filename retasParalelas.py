import numpy as np
import matplotlib.pyplot as plt

pontos = np.linspace(0,100,10)
x = np.linspace(0,100,10)
y = np.linspace(10,110,10)

plt.title('Questao 02: Retas paralelas')
plt.plot(pontos,x)
plt.plot(pontos,y)
plt.show()