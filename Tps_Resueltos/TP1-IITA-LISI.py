"""
#punto 1
color = "verde"
print("Su color es:",color)
color = "rojo"
print("Su nuevo color es:",color)
print("-------------------------------")   #puse estos guiones al final de cada punto para poder diferenciarlos 
"""
"""
#punto 2
nombre = input("Ingresa tu nombre: ")
print("Hola", nombre + ", ¿cómo estás?")
print("-------------------------------")
"""
"""
#punto 3
print(5+3)
print(9-1)
print(4*2)
print(int(24/3))   #en esta linea puse el int al inicio para que me de el resultado sin decimales (sino tendria que usar div. entera //)
print("-------------------------------")
"""


"""
#punto 4
mi_entero = 5
mi_decimal = 5.0
mi_string = "5"
mi_booleano = True

print(type(mi_entero))
print(type(mi_decimal))
print(type(mi_string))
print(type(mi_booleano))
"""




"""
#punto 5
num_decimal = float(input("Ingrese un numero decimal: "))
print(("Su parte entera es:"),int(num_decimal))
print("-------------------------------")

#punto 6
nombre = input("Ingrese su nombre: ")
f_nacimiento = int(input("Ingrese su fecha de nacimiento: "))
f_cien = f_nacimiento + 100
print("Cumplirá cien años en el año",f_cien)
print("-------------------------------")

#punto 6
celsius = float(input("Ingrese grados celsius: "))     #puse de tipo de variable float porque en quimica se usan grados con decimales 
fahrenheit = (9.0/5.0)*celsius+32
print("La conversion a fahrenheit es igual a:",fahrenheit)
"""

import turtle
import time
import random

# Variables de configuración
retraso = 0.1
puntuacion = 0
alta_puntuacion = 0

# 1. Configuración de la pantalla
pantalla = turtle.Screen()
pantalla.title("Juego de Snake")
pantalla.bgcolor("black")
pantalla.setup(width=600, height=600)
pantalla.tracer(0) # Desactiva las actualizaciones automáticas para que vaya fluido

# 2. Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direccion = "stop"

# 3. Comida de la serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

# Lista para guardar el cuerpo (segmentos) de la serpiente
segmentos = []

# 4. Marcador de puntos
marcador = turtle.Turtle()
marcador.speed(0)
marcador.shape("square")
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write("Puntos: 0  Récord: 0", align="center", font=("Courier", 24, "normal"))

# 5. Funciones para cambiar la dirección
def arriba():
    if cabeza.direccion != "down": # Evita que se devuelva sobre sí misma
        cabeza.direccion = "up"

def abajo():
    if cabeza.direccion != "up":
        cabeza.direccion = "down"

def izquierda():
    if cabeza.direccion != "right":
        cabeza.direccion = "left"

def derecha():
    if cabeza.direccion != "left":
        cabeza.direccion = "right"

# Función para aplicar el movimiento
def mover():
    if cabeza.direccion == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direccion == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direccion == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direccion == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# 6. Conectar el teclado
pantalla.listen()
pantalla.onkeypress(arriba, "Up")
pantalla.onkeypress(abajo, "Down")
pantalla.onkeypress(izquierda, "Left")
pantalla.onkeypress(derecha, "Right")

# 7. Bucle principal del juego
while True:
    pantalla.update()

    # A. Comprobar colisión con los bordes
    if cabeza.xcor() > 290 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direccion = "stop"

        # Esconder los segmentos muertos fuera de la pantalla
        for segmento in segmentos:
            segmento.goto(1000, 1000)
        segmentos.clear()
        
        # Reiniciar puntos
        puntuacion = 0
        marcador.clear()
        marcador.write(f"Puntos: {puntuacion}  Récord: {alta_puntuacion}", align="center", font=("Courier", 24, "normal"))

    # B. Comprobar colisión con la comida
    if cabeza.distance(comida) < 20:
        # Mover la comida a un lugar aleatorio
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        # Añadir un nuevo segmento al cuerpo
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("lightgreen")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
        
        # Aumentar puntos
        puntuacion += 10
        if puntuacion > alta_puntuacion:
            alta_puntuacion = puntuacion
        marcador.clear()
        marcador.write(f"Puntos: {puntuacion}  Récord: {alta_puntuacion}", align="center", font=("Courier", 24, "normal"))

    # C. Mover el cuerpo de la serpiente (de atrás hacia adelante)
    total_segmentos = len(segmentos)
    for index in range(total_segmentos - 1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    # Mover el segmento 0 a donde está la cabeza
    if total_segmentos > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mover()

    # D. Comprobar colisión con su propio cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direccion = "stop"
            
            for segmento_oculto in segmentos:
                segmento_oculto.goto(1000, 1000)
            segmentos.clear()
            
            puntuacion = 0
            marcador.clear()
            marcador.write(f"Puntos: {puntuacion}  Récord: {alta_puntuacion}", align="center", font=("Courier", 24, "normal"))

    time.sleep(retraso)