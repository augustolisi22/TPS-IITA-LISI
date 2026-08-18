"""
Ejercicio 1:
1. Escribir un programa que pregunte al usuario su edad. 
2. Muestre por pantalla si es mayor de edad o no.
"""
""""
edad_usuario = int(input("Ingrese su edad: "))
if edad_usuario >= 18:
    print("El usuario es mayor de edad")
else:
    print("El usuario es menor de edad")
"""
"""
Ejercicio 2
1. Escribir un programa que almacene la cadena de caracteres contraseña en una variable. 
2. pregunte al usuario por la contraseña. 
3. imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""
"""
contraseña = "hola123"
contraseña_u = (input("Ingrese la contraseña: ")).lower()
if contraseña_u == contraseña:
    print("La contraseña coincide correctamente")
else:
    print("La contraseña no coincide")
"""
"""
Ejercicio 3
1. Escribir un programa que pida al usuario dos números.
2. Muestre por pantalla su división. 
3. Si el divisor es cero el programa debe mostrar un error.
"""
"""
num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))
div = (num_1/num_2)
if div != 0:
    print("La division es: ",div)
else:
    print("Error")
"""
"""
Ejercicio 4
1. Escribir un programa que pida al usuario un número entero.
2. Muestre por pantalla si es par o impar.
"""
"""
num_entero = int(input("Ingrese un numero entero: "))
if num_entero%2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
"""
"""
Ejercicio 5
1. Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales.
2. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales. 
3. Muestre por pantalla si el usuario tiene que tributar o no.
"""
"""
edad_u = int(input("Ingrese su edad: "))
ingresos_u = int(input("Ingrese sus ingresos mensuales: "))
if edad_u > 16 and ingresos_u >= 1000:
    print("El usuario puede tributar")
else:
    print("El usuario no puede tributar")
"""
"""
Ejercicio 6
1. Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
2. Escribir un programa que pregunte al usuario su nombre y sexo.
3. Muestre por pantalla el grupo que le corresponde.
"""

nombre_alumno = input("Ingrese su nombre: ")
sexo_alumno = input("Ingrese su sexo: ")


