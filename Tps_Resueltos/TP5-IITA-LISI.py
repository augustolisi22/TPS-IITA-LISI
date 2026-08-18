"""
Ejercicio 1
1. Escriba una función redondear() que permita redondear un número decimal.
2. Si la parte decimal es mayor a 0.5, devolver el entero siguiente.
3. Si no devolver el entero inmediatamente anterior.
"""
"""
def redondear(numero):
    entero = int(numero)
    if numero-entero >= 0.5:
        return entero + 1
    else:
        return entero
"""
"""
Ejercicio 2
1. Coloque el módulo del ejercicio anterior dentro de un paquete. 
2. En un módulo que esté fuera de ese paquete, cree una función de suma de decimales que redondee el resultado 
3. Haga uso de la función redondear() del paquete recién creado.
"""
"""
from apuntes import redondeo
def sumar_decimales(num1, num2):
    resultado_suma = num1 + num2
    resultado_redondeado = redondeo.redondear(resultado_suma)
    return resultado_redondeado
"""
"""
Ejercicio 3
1. Usando el módulo datetime, escribe un programa que muestre la fecha y hora actuales del sistema.
"""
"""
import datetime
fecha_hora_actual = datetime.datetime.now()
print(f"fecha y hora actuales del sistema:{fecha_hora_actual}")
"""
"""
Ejercicio 4
1. Escriba un programa que devuelva un número par al azar entre 2 y 10.
"""
"""
import random
def generar_par_aleatorio():
    return random.randrange(2, 11, 2)
while True:
    numero = generar_par_aleatorio()
    print(numero)
"""
"""
Ejercicio 5
1. Escriba un programa que devuelva un número par al azar entre 2 y 10.
"""
"""
import random
def bola_magica(pregunta=""):
    respuestas = [
        "Es seguro que sí",
        "Las chances son buenas",
        "Puedes contar con ello",
        "Pregúntame de nuevo más tarde",
        "Concéntrate y pregunta de nuevo",
        "No veo con claridad, intenta de nuevo",
        "Mi respuesta es no",
        "Mis fuentes me dicen que no"
    ]
    if pregunta:
        print(f"Tu pregunta: {pregunta}")
    return random.choice(respuestas)
print(bola_magica(input("preguntale algo a la bola mágica: ")))
"""
"""
Ejercicio 6
1.  Encuentre el tiempo de ejecución de los programas de los ejercicios anteriores.
"""
"""
#---------------------------------
import time
def redondear(numero):
    entero = int(numero)
    if numero - entero >= 0.5:
        return entero + 1
    else:
        return entero
inicio = time.time()
resultado = redondear(10.7)
print(f"Resultado del redondeo: {resultado}")
fin = time.time()
print(f"Tiempo de ejecución (Ejercicio 1): {fin - inicio} segundos\n")  #los \n son para salto de linea
import time
#---------------------------------
import time
from apuntes import redondeo
def redondear(numero):
    entero = int(numero)
    if numero - entero >= 0.5:
        return entero + 1
    else:
        return entero
def sumar_decimales(num1, num2):
    resultado_suma = num1 + num2
    resultado_redondeado = redondear(resultado_suma)
    return resultado_redondeado
inicio = time.time()
resultado = sumar_decimales(2.4, 3.2)
print(f"Resultado de la suma redondeada: {resultado}")
fin = time.time()
print(f"Tiempo de ejecución (Ejercicio 2): {fin - inicio} segundos\n")
#---------------------------------
import time
import datetime
inicio = time.time()
fecha_hora_actual = datetime.datetime.now()
print(f"Fecha y hora actuales del sistema: {fecha_hora_actual}")
fin = time.time()
print(f"Tiempo de ejecución (Ejercicio 3): {fin - inicio} segundos\n")
#---------------------------------
import time
import random
def generar_par_aleatorio():
    return random.randrange(2, 11, 2)
inicio = time.time()
for _ in range(5):
    numero = generar_par_aleatorio()
    print(f"Número par generado: {numero}")
fin = time.time()
print(f"Tiempo de ejecución (Ejercicio 4): {fin - inicio} segundos\n")
#---------------------------------
import time
import random
def bola_magica(pregunta=""):
    respuestas = [
        "Es seguro que sí",
        "Las chances son buenas",
        "Puedes contar con ello",
        "Pregúntame de nuevo más tarde",
        "Concéntrate y pregunta de nuevo",
        "No veo con claridad, intenta de nuevo",
        "Mi respuesta es no",
        "Mis fuentes me dicen que no"
    ]
    if pregunta:
        print(f"\npregunta: {pregunta}")
    return random.choice(respuestas)
pregunta_usuario = input("Pregúntale algo a la bola mágica: ")
inicio = time.time()
respuesta = bola_magica(pregunta_usuario)
print(f"La bola dice: {respuesta}")
fin = time.time()
print(f"Tiempo de ejecución (Ejercicio 5): {fin - inicio} segundos")
"""
"""
Ejercicio 7
1.  Escriba un programa que simule un sorteo donde toman uno o más papeles al azar de un pozo para elegir los ganadores.
"""
"""
import random
import time
def realizar_sorteo(pozo, cantidad_ganadores):
    if cantidad_ganadores > len(pozo):
        return "Error: No puedes sacar más papeles de los que hay en el pozo."
    ganadores = random.sample(pozo, cantidad_ganadores)
    return ganadores
"""
"""
Ejercicio 8
1.  Escriba una función que pida al usuario ingresar su fecha de nacimiento.
2.  Sea capaz de devolver la cantidad de días desde su nacimiento hasta hoy.
"""
"""
from datetime import datetime, date
def dias_desde_nacimiento():
    fecha_texto = input("Ingresa tu fecha de nacimiento (DD/MM/AAAA): ")
    fecha_nacimiento = datetime.strptime(fecha_texto, "%d/%m/%Y").date()
    hoy = date.today()
    diferencia = hoy - fecha_nacimiento
    dias_totales = diferencia.days
    print(f"Han pasado {dias_totales} días desde que naciste")
    return dias_totales
"""
"""
Ejercicio 9
1.  Implemente el programa del ejercicio 6 usando un diccionario.
"""
"""
import time
import datetime
import random
def ej1_redondear():
    numero = 9.6
    entero = int(numero)
    if numero - entero >= 0.5:
        return entero + 1
    else:
        return entero
def ej2_sumar_decimales():
    resultado_suma = 2.4 + 3.9
    return ej1_redondear()
def ej3_fecha_hora():
    return datetime.datetime.now()
def ej4_pares_aleatorios():
    for _ in range(5):
        random.randrange(2, 11, 2)
def ej5_bola_magica():
    respuestas = ["Es seguro que sí", "Mi respuesta es no", "Las chances son buenas"]
    return random.choice(respuestas)
ejercicios = {
    "Ejercicio 1 (Redondeo)": ej1_redondear,
    "Ejercicio 2 (Suma módulo)": ej2_sumar_decimales,
    "Ejercicio 3 (Fecha actual)": ej3_fecha_hora,
    "Ejercicio 4 (Pares al azar)": ej4_pares_aleatorios,
    "Ejercicio 5 (Bola mágica)": ej5_bola_magica
}
tiempos_ejecucion = {}
print("Midiendo tiempos de ejecución...\n")
for nombre, funcion in ejercicios.items():
    inicio = time.time()
    funcion()
    fin = time.time()
    tiempos_ejecucion[nombre] = fin - inicio
for nombre, tiempo in tiempos_ejecucion.items():
    print(f"{nombre}: {tiempo} segundos")
"""