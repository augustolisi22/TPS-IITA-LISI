"""
#punto 01:
1. Solicitar al usuario un número de cliente. 
2. Si el número es el 1000, imprimir "Ganaste un premio"
"""
"""
num_cliente = int(input("Ingrese su numero de cliente: "))
if num_cliente == 1000:
    print("Ganaste un premio")
else:
    print("No ganste un premio")
"""
"""
#punto 02:
1. Solicitar al usuario que ingresedos números 
2. Mostrar cuál de los dos es menor. 
3. No considerar el caso en que ambos números son iguales.
"""
"""
num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))
if num_1 > num_2:
    print("El mayor es:", num_1)
else:
    print("El mayor es:", num_2)
"""
"""
#punto 03:
1. Solicitar al usuario que ingresedos números.
2. Mostrar cuál de los dos es menor. 
3. Considerar el caso en que ambos números son iguales.
"""
"""
numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))
if numero_1 == numero_2:
    print("Los numeros son iguales")
elif numero_1 > numero_2:
    print("El mayor es:", numero_1)
else:
    print("El mayor es:", numero_2)
"""
c=150
while c>0:
    numero=int(input("Ingrese un numero: "))
    if numero == 1000:
        print("Ganaste un premio")
        c=-1
    else:
        print("No ganste un premio")
else:
    print("No se admiten mas usuarios")