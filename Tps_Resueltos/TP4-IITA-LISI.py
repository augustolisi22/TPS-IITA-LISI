"""
Ejercicio 1
1. Diseña una función que tome como parámetro 2 números.
2. Que devuelva una lista que contenga TODOS los números enteros entre estos 2 incluyendo AMBOS parámetros.
"""
"""
def enteros(numero1,numero2):
    lista=[]
    lista.append(numero1)
    for contador in range(numero1, numero2+1):
        if contador != numero1 and contador != numero2:
         lista.append(contador)
    lista.append(numero2)
    return lista
print(enteros(1,10))
"""
"""
Ejercicio 2
1. Escribir una función que tome como parámetro 2 números.
2. Retorne una lista con todos los números pares entre estos, EXCLUYENDO a los parámetros.
"""
"""
def pares(numero1,numero2):
    lista=[]
    for contador in range(numero1, numero2 + 1):
        if contador != numero1 and contador != numero2:
            if contador % 2 == 0:
                lista.append(contador)
    return lista
print(pares(1,10))
"""
"""
Ejercicio 3
1. Escribir una función que tome 2 parámetros, el primero que reciba una cadena, y el segundo que reciba un carácter.
2. La función tendrá que retornar la cantidad de veces que aparece ese carácter en esa cadena.
"""
"""
def contar_caracter(cadena,caracter):
    contador=0
    for indice in range(len(cadena)):
        if cadena[indice] == caracter:
            contador += 1
    return contador
"""
"""
Ejercicio 4
1. Elaborar una función que tome como parámetro 2 números.
2. Retorne una lista con todos los números primos entre ese rango de números.
"""
"""
def primos(numero1,numero2):
    primos=0
    lista=[]
    for contador in range(numero1,numero2+1):
        if contador > 1:
            primo = True
            for divisor in range(2, contador):
                if contador % divisor == 0:
                    primo = False
                    break
            if primo:
                lista.append(contador)
    return lista
print(primos(1,10))
"""
"""
Ejercicio 5
1. Elaborar una función que tome como parámetro una lista.
2. Devuelva un bool que diga si en esa lista TODOS sus números son pares. 
"""
"""
def pares(lista):
    for numero in lista:
        if numero % 2 != 0:
            return False
    return True
print(pares([12, 37, 9]))
"""
"""
Ejercicio 6
1. Elaborar una función que tome como parámetro una lista.
2. Devuelva un bool que diga si en esa lista TODOS sus números son primos.
"""
"""
def son_primos(lista):
    for numero in lista:
        if numero <= 1:
            return False
        for divisor in range(2, numero):
            if numero % divisor == 0:
                return False 
    return True
print(son_primos([15, 13, 3]))
"""