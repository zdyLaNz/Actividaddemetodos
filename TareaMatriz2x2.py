'''Inverso de una matriz 2x2
Nombre: Dylan Imsael Jiménez Quingalombo

importamos libreria numpy'''

import numpy as np

'''En este caso el programa ya tendra dectectado las cifras ingresadas para la matriz
Se creara una variable de tipo matriz, en la que se creara la matriz.

Matriz 2x2

[[2    6]
 [8    1]]
'''
print("\n\tResolucion de una matriz 2x2")
matriz = np.array([ [2, 6],
                              [8, 1] ])  # creacion de matriz con una funcion array
print("\n\tMostrando la matriz 2x2: \n")
print(matriz) # mandamos a llamar a la variable matriz
print("\n\tMostrando la inversa de la matriz ingresada: \n")
inversa = np.linalg.inv(matriz) # funcion que permite resolver la inversa de la matriz
print(inversa) # mandamos a llamar a la variable inversa, la cual mostrara la inversa de mi matriz
