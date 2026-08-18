"""
Desafio 01
1. Solicitar al usuario el ingreso de 1000 números. 
2. Luego mostrar el mayor, el menor y el promedio de todos los números ingresados.
"""

numero_1 = int(input("ingrese un numero: "))

mayor = numero_1
menor = numero_1
suma = numero_1
contador = 0

while contador < 999 :
    numeros_restantes = int(input("Ingrese los numeros restantes: "))

    if numeros_restantes > mayor:
        mayor = numeros_restantes

    elif numeros_restantes < menor:
        menor = numeros_restantes

    suma += numeros_restantes
    contador += 1

promedio = suma/1000

print(mayor)
print(menor)
print(promedio)