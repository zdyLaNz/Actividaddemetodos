
'''Se importa tanto la libreria numpy como matplot'''
import numpy as np
import matplotlib.pyplot as plt
'''Se ingresa las dos dunciones tanto f(x) como g(x)
f(x)=x^2-x+1
g(x)=(2)/(x-1)'''
fx = lambda x: x**2 - x + 1
gx = lambda x: (2)/(x-1)
'''Se colocan los parametros que tendra la grafica'''
x=np.linspace(-5,5,100)
'''se calcula los valores de nuestro array'''
print(x)
a=fx(x)
b=gx(x)
print(a)
#print(b)

plt.plot(x,a,color="red") # defino el color que tendra la resultante de cada funcion
plt.plot(x,b,color="blue")

plt.show()