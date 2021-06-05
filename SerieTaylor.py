
'''Importamos libreria math'''
import math

a = float(input("\n\tIngrese el dato que desea resolver en grados:  "))
'''Metodo para transformar el dato ingresado en grados a radianes'''
b = math.radians(a)
print("")
n= int(input("\tDato con el que truncara a la serie:  "))

senx= 0.0
print("{:^2} {:^10}{:^16}".format("\tT","n","sen(x)"))
'''con este ciclo se podra acumular los terminos'''
for k in range(n) :
    '''Math permite representar el factorial de algun termino o valor'''
    senx= senx + (-1)**k * b**(2*k+1) / math.factorial((2*k+1))
    print("\n\t{:^2} {:^10}{:^16}".format(  k+1,   k  ,  senx))