"""
Ejercicio 1 
1. Escribir un programa que abra un archivo.
2. Lea todas sus lineas y cuente cuantas lineas existen en el mismo.
"""
"""
file = open("C:/Users/augus/OneDrive/Personas/Augusto/IITA-2026/trabajos/Tps_Resueltos/hola.txt", "r")
hola = file.readlines()
file.close()
contador=0
for i in range (len(hola)):
    contador+=1
print(f"son {contador} lineas")
"""

"""o"""
"""
file = open("C:/Users/augus/OneDrive/Personas/Augusto/IITA-2026/trabajos/Tps_Resueltos/hola.txt", "r")
hola = file.readlines()
file.close()
print(len(hola))
"""
"""
Ejercicio 2
1. Utilizar python para escribir un archivo de texto que tenga 11 lineas.
2. En cada una escribir lo que desean y cerrar el archivo.
3. Luego mostrar el contenido del archivo.
4. escribir una fincion que cuenten cuantos caracteres existen dentro del archivo.
"""
"""
def contar_caracteres(nombre_archivo):

    file = open(nombre_archivo,"r")
    contenido = file.read()
    file.close() 
    print(len(contenido))

file = open("C:/Users/augus/OneDrive/Personas/Augusto/IITA-2026/trabajos/Tps_Resueltos/escribir.txt","w")
for contador in range(11):
    file.write("hola\n")
file.close()

file = open("C:/Users/augus/OneDrive/Personas/Augusto/IITA-2026/trabajos/Tps_Resueltos/escribir.txt","r")
contenido = file.read()
file.close() 
print(contenido)

contar_caracteres("C:/Users/augus/OneDrive/Personas/Augusto/IITA-2026/trabajos/Tps_Resueltos/escribir.txt")
"""
"""
Ejercicio 3
1. Escriba un programa que ída al usuario su nombre.
2. Cuando este lo ingrese, muestre un mensaje de bienvenida en la pantalla y agregue una linea donde registre la visita del usuario.
"""
"""
nombre=input("Ingrese su nombre: ")
print(f"Bienvenido {nombre}")

file = open("C:/Users/augus/OneDrive/Personas/Augusto/IITA-2026/trabajos/Tps_Resueltos/libro_invitados.txt","a")
file.write(f"El usuario {nombre} fue registrado\n")
file.close()
"""
"""

clase 15/08

"""
"""
class Auto():
    def __init__(self, ruedas, color, puertas, velocidad):
    self.ruedas = ruedas
    self.color = color
    self.puertas = puertas
    self.velocidad = 120

    def arrancar(self):
        print("brummm")

    def acelerar(self):
        print(f"El auto {self.color} va a {self.velocidad}")

    def frenar(self):
        print(f"El auto de {self.ruedas} ruedas frena")

autito1 = Auto(4, "rojo", 1, 320)
auto_pablo = Auto(2, "verde", 5, 80)                  #instanciacion

autito1.acelerar()                               #mensaje
auto_pablo.acelerar()

"""
"""
Ejercicio
1. Crear una clase gato que contenga 5 atributos (nombre, color de pelo, color de ojos, cansancio y hambre).
2. 4 metodos (comer, dormir, jugar, acariciar).
3. Instanciar 3 objetos de la clase y utilizar sus metodos.
"""

class Gato():
    def __init__(self, nombre, color_pelo, color_ojos, cansancio, hambre):
        self.nombre = nombre
        self.color_pelo = color_pelo
        self.color_ojos = color_ojos
        self.cansancio = cansancio
        self.hambre = hambre

    def jugar(self):
        if self.cansancio == "si" or self.hambre == "si":
            print(f"El gatito {self.nombre} no quiere jugar en este momento")
        else:
            print(f"El gatito {self.nombre} se divierte contigo")
            print(f"Ahora el gatito {self.nombre} está cansado y tiene hambre")
            self.cansancio = "si"
            self.hambre = "si"


    def acariciar(self):
        print(f"El gatito {self.nombre} ronronea")

    def dormir(self):
        if self.cansancio == "si":
            print(f"El gatito {self.nombre} ya no está cansado")
        else:
            print(f"El gatito {self.nombre} no necesita dormir")

    def comer(self):
        if self.hambre == "si":
            print(f"El gatito {self.nombre} ya no tiene hambre")
        else:
            print(f"El gatito {self.nombre} no necesita comer")

gatito1 = Gato("michi", "naranja", "verdes", "no", "no")
gatito2 = Gato("pelusa", "blanco", "negros", "no", "si")
gatito3 = Gato("tobi", "negro", "marrones", "si", "no")
seguir = True

while seguir == True:
    accion = input("¿Que desea hacer con su gato?: ")
    if accion == "acariciar":
        gatito1.acariciar()
    if accion == "dormir":
        gatito1.dormir()
    if accion == "comer":
        gatito1.comer()
    if accion == "jugar":
        gatito1.jugar()

    seguir = input("¿Desea seguir del programa?: ")
    if seguir == "si":
        seguir = True
    else:
        seguir = False
        print("Programa finalizado con éxito.")





