"""
Ejercicio 1
1. Pida un número al usuario.
2. Determine si es par o impar.

numero = int(input("Ingrese un numero: "))
if numero%2 == 0:
    print("El numero es par")                     #si dividimos un numero por 2 y el resto es igual a 0, entonces el numero es par
else:
    print("El numero es impar") 
"""


"""
Ejercicio 2
1. Escriba una cadena if-elif-else que determine el estado de vida de una persona.
2. Si la persona tiene menos de 2 años, muestre un mensaje que diga que es un bebe.             
3. Si tiene al menos 2 años, pero menos de 4, muestre que es un infante.
4. Si tiene al menos 4, pero menos de 12, muestre que es un niño.
5. Si tiene al menos 13, pero menos de 20, muestre que es un adolescente.
6. Si tiene al menos 20 pero menos de 65, muestre que es un adulto.
7. Si tiene 65 o más, muestre que es un anciano.

edad_persona = int(input("Inserte la edad de la persona: "))
if edad_persona < 2 and edad_persona >= 0:                                    
    print("Estado de vida: Es un bebé")
elif edad_persona >= 2 and edad_persona < 4:
    print("Estado de vida: Es un infante")
elif edad_persona >= 4 and edad_persona < 12:
    print("Estado de vida: Es un niño")
elif edad_persona >= 13 and edad_persona < 20:
    print("Estado de vida: Es un adolescente")
elif edad_persona >= 20 and edad_persona < 65:
    print("Estado de vida: Es un adulto")
else:
    print("Estado de vida: Es un anciano")
"""


"""
Ejercicio 3
1. Cree un ciclo que nunca termine y ejecútelo. 
2. Puede probarlo haciendo que muestre algo en pantalla por cada pasada del ciclo.
3. Para finalizarlo, presione Ctrl-C o el comando para detener la ejecución correspondiente a su editor.

while True:
    print("Hola")
"""


"""
Ejercicio 4
1.Escriba un programa utilizando ciclos for que muestre los enteros del 1 al 100.
2. diez números por línea, como se muestra abajo:
1 2 3 4 5 6 7 8 9 10
11 12 13 14 15 16 17 18 19 20
21 22 23 24 25 26 27 28 29 30
. . 91 92 93 94 95 96 97 98 99 100

for i in range(1, 101, 10):
    print(i, i+1, i+2, i+3, i+4, i+5, i+6, i+7, i+8, i+9)                     #1, 1+1, 1+2..etc  /   como se hace de 10 en 10, al hacer otra vuelta i pasa a ser 10 entonces queda 10+1, 10+2...etc
"""


"""
Ejercicio 5
1. Escriba un programa utilizando ciclos while que pida su nombre al usuario.
2. Muestrele un saludo personalizado hasta que ingrese la palabra “salir.

while True:
    nombre = input("ingrese su nombre: ")
    print("Buen día", nombre)
    salir = input("¿Desea salir del programa?: ")
    
    if salir == "salir":
        break
"""