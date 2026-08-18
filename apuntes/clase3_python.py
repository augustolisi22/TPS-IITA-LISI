"""
#punto 01
contador=100
while contador<200:
    contador= contador+1
    print(contador)


x=5
c=6
suma=x+c
print(suma)



con while final


while True:
    nombre = input("ingrese un nombre: ")
    print("Hola", nombre)

    if nombre == "*":
        break




c = 99

while True: 
  
    c += 1
    print(c)

    if c == 200:
        break
        



while True:
    print("Hola")


c=1

while True: 
    c +=1
    print(c)
    salir = input("¿Desea salir del programa?: ")
    
    if salir == "si":
        break



for contador in range (1,11,2):
    print(contador)


numero = int(input("ingrese un numero: "))

for tabla in range (1,11):
    multiplicacion = numero * tabla
    print (multiplicacion)
    print(f"{numero} X {contador} = {numero * contador})

for bucle in range (100,201):
    print(bucle)
"""
"""
Desafio 01
1. Solicitar al usuario el ingreso de 1000 números. 
2. Luego mostrar el mayor, el menor y el promedio de todos los números ingresados.
"""
"""
c=0
mayor=int(input("ingrese un numero: "))
menor=mayor
suma=0
while c < 4 :
    numeros = int(input("Ingrese 1000 numeros: "))
    if numeros > mayor:
        mayor = numeros
    elif numeros < mayor:
        numeros=menor
    suma += numeros
    c += 1
promedio = suma/4
print(promedio)
print(mayor)
print(menor)


"""
"""
linea = ""
for contador in range(1,10):
    linea = linea + " " + str(contador)
print(linea)


for contador1 in range(1,101,10):
    linea1= ""
    for contador in range(contador,contador+10):
        linea1 = linea1 + " " + str(contador)
    print(linea)


linea2 = ""
for contador2 in range(1,101):
    linea2 = linea2 + " " + str(contador2)
    if contador2 % 10 == 0:
        print(linea2)
        linea2 = ""
"""
"""
lista_perros = ["Uma", "Pelusa", "Messi"]
print(lista_perros[0])
print(len(lista_perros))


mi_lista=["A","E","I","O","U"]
print(mi_lista[0:3])


lista_ejemplo1 = ["A","B","C","D","E"]
lista_ejemplo1.append("F")
print(lista_ejemplo1)


lista_ejemplo2 = ["A","B","C","D","E"]
lista_ejemplo2.insert(2,"hola")
print(lista_ejemplo2)


lista_ejemplo3 = ["A","B","C","D","E"]
lista_ejemplo4 =  ["F","G"]
lista_ejemplo3.extend(lista_ejemplo4)
print(lista_ejemplo3)

lista = [["a","b"],[1,2]]
print(lista[0][1])


listinha=["Augusto","Octavio","Francesca"]
while "Octavio" in listinha:
    listinha.remove("Octavio")
print(listinha)


listarda=["Javier","Miguel","Roberto"]
listarda.pop()
print(listarda)
"""
"""
lista=[]
contador=1
while contador<36:
    lista.append(contador)
    contador+=1
print(lista)


limite_inferior=int(input("ingrese el limite inferior: ))
limite_superior=int(input("ingrese el limite superior: ))
lista=[]
for contador in range(limite_inferior,limite_superior)
    lista.append(contador)
print(lista)
"""
"""
lista2=[1,2,3]
for contador in range(len(lista2)):
    print(lista2[contador])
"""
"""
palabra = input("Ingrese una palabra: ")
lista = []
for contador in range(len(palabra)):
    lista.append(palabra[contador])
print(lista)
"""
"""
palabra = input("Ingrese una palabra: ")
numero_a = 0
for contador in range(len(palabra)):
    if palabra[contador] == "a" or "A":
        numero_a = numero_a + 1
print(f"La letra A aparece {numero_a} veces")
"""
"""
tupla = (1,2,3,4,5,6,7,8,9,10)
indice = int(input("Elija un valor: "))
print(f"El valor es: {tupla[indice]}")
"""
"""
tupla = ("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
indice = int(input("Elija un mes: "))
print(f"El valor es: {tupla[indice]}")
"""
"""
mes = input("Ingrese el mes: ")
dicc = {"enero": 31,"febrero": 28,"marzo": 31,"abril": 30,"mayo": 31,"junio": 30,"julio": 31,"agosto": 30,"septiembre": 31,"octubre": 30,"noviembre": 31,"diciembre": 30}
print(f"el mes tiene {dicc[mes]} dias")
"""
"""
def sumar():
    numero1 = 1
    numero2 = 5
    print(numero1 + numero2)

sumar()
"""
"""
def sumar(numero1, numero2):
    resultado = numero1 + numero2
    print(resultado)

sumar(1, 2)
sumar(19, 20)
numero = int(input("Ingrese su edad: "))
sumar(numero, 5)
"""
"""
def mail_valido(email):
    if "@" in email:
        print("La direccion es valida")
    else:
        print("La direccion es invalida")
email=input("Ingrese su mail: ")
mail_valido(email)
"""
"""
def calculo_fact(numero):
    acumulador = 1
    for contador in range(1, numero + 1):
        acumulador = acumulador * contador
    print (acumulador)

numero = int(input("Ingrese un numero: "))
calculo_fact(numero)
"""
def es_primo(numero):
    divisor=0
    for contador2 in range(1,numero+1):
        if numero%contador2 == 0:
            divisor+=1
    if divisor>2:
        print("el numero no es primo")
    else:
        print("el numero es primo")
numero = int(input("Ingrese un numero: "))
es_primo(numero)



"""
  |  | 
--+--+--
  |  | 
--+--+--
  |  | 
"""
""""
necesito un archivo main que sea cortito con un par de lineas nomas porq se mezcla todo el codigo ahi (solo en la carpeta principal)
no meter imports dentro de funciones porque sino se hace lento
flet es la mejor para interfaz porque es mas versatil
"""
