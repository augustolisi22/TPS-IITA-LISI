"""
Ejercicio 1
1. Meter los números del 1 al 20 en una lista y mostrarla en pantalla. 
2. Hacer lo mismo para un rango de números indicado por un usuario. 
"""
"""
limite_inferior = int(input("Ingrese el limite inferior: "))
limite_superior = int(input("Ingrese el limite superior: "))
lista2 = []
for contador in range(limite_inferior,limite_superior):
    lista2.append(contador)
print(f"La lista es: {lista2}")
"""
"""
Ejercicio 2
1. Pide un número y guarda en una lista su tabla de multiplicar hasta el 10.
"""
"""
numero = int(input("Ingrese un numero: "))
lista = []
for contador in range(1,11):
    lista.append(numero*contador)
print(f"La tabla de multiplicar del numero {numero} hasta el 10 es: {lista}")
"""
"""
Ejercicio 3
1. Pide una cadena (string) por teclado.
2. Mete los caracteres en una lista sin repetir caracteres. 
"""
"""
lista = []
palabra = input("Ingrese una palabra: ")
for contador in range(len(palabra)):
    if not palabra[contador] in lista:
        lista.append(palabra[contador])
print(lista)
"""
"""
Ejercicio 4
1. Pide una cadena (string) por teclado.
2. Mete los caracteres en una lista sin espacios. 
"""
"""
lista = []
palabra = input("Ingrese una palabra: ")
for contador in range(len(palabra)):
    if palabra[contador] != " ":
        lista.append(palabra[contador])
print(lista)
"""
"""
Ejercicio 5
1. Crea una tupla con números.
2. Pide un numero por teclado.
3. Indica cuantas veces se repite. 
"""
"""
numeros = (1,2,1,4,5,4,5,3,4)
contador1 = 0
numero = int(input("Ingrese un numero: "))
for contador2 in range(len(numeros)):
    if numeros[contador2] == numero:
        contador1 += 1
print(contador1)
"""
"""
Ejercicio 6
1. Crea una tupla con los meses del año, pedir números al usuario.  
2. Si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.
3. El programa termina cuando el usuario introduce un cero.
"""
"""
meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
while True:
    numero = int(input("Ingrese un numero: "))
    if numero >= 1 and numero <= len(meses):
        print(meses[numero - 1])
    else:
        print("Error")     
    salir = int(input("Escriba 0 si desea salir del programa: "))
    if salir == 0:
        break        
"""
"""
Ejercicio 7
1. Crea una tupla con números.
2. Indica el número con mayor valor y el que menor tenga.
"""
"""
numeros = (1,2,3,4,5,6)
mayor = numeros[0]
menor = numeros[0]
for contador in range(len(numeros)):
    if numeros[contador] > mayor:
        mayor = numeros[contador]
    if numeros[contador] < menor:
        menor = numeros[contador]
print(f"El numero mayor es: {mayor}")
print(f"El numero menor es: {menor}")
"""