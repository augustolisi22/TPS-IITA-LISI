"""
Ejercicio 1
1. Crear una clase Rectángulo con atributos para la medida de la base y la altura.
2.Escribir un método que calcule y devuelva el área de ese rectángulo.
"""
"""
class Rectangulo:
    def __init__(self, medida_base, medida_altura):
        self.ancho = medida_base
        self.alto = medida_altura

    def calcular_area(self):
        return self.ancho * self.alto
"""
"""
Ejercicio 2
1. Crear una clase Mate con atributos para las cebadas restantes, el estado actual (lleno o vacío) y el tope máximo de cebadas.
2. Hacer un método cebar que llene el mate. Si ya estaba lleno, debe frenar y lanzar una excepción advirtiendo que te quemaste.
3. Hacer un método beber que vacíe el mate y reste una cebada disponible. Si estaba vacío, debe lanzar una excepción.
4. Armar la lógica para que, si las cebadas llegan a cero, el programa no tire error (excepción) al seguir tomando, sino que simplemente imprima una advertencia de que el mate está lavado.
"""
"""
class Mate:
    def __init__(self, limite_cebadas):
        self.n = limite_cebadas  
        self.cebadas_restantes = limite_cebadas
        self.contiene_agua = False 

    def cebar(self):
        if self.contiene_agua:
            raise Exception("¡Cuidado! ¡Te quemaste!")
        self.contiene_agua = True

    def beber(self):
        if not self.contiene_agua:
            raise Exception("¡El mate está vacío!")

        self.contiene_agua = False

        if self.cebadas_restantes > 0:
            self.cebadas_restantes -= 1
        else:
            print("Advertencia: el mate está lavado.")
"""
"""
Ejercicio 3
1. Armar una clase Corcho que guarde el nombre de la bodega de origen.
2. Armar una clase Botella que tenga referenciado a un objeto corcho (o esté en None si está destapada).
3. Crear la clase Sacacorchos con un método destapar que le quite el corcho a una botella y se lo guarde adentro. Debe lanzar excepciones si la botella ya venía destapada o si el sacacorchos ya tenía un corcho trabado de antes.
4. Sumarle al sacacorchos un método limpiar para sacarle el corcho viejo, o lanzar una excepción si intentás limpiarlo y ya estaba vacío.
"""
"""
class Corcho:
    def __init__(self, origen_bodega):
        self.bodega = origen_bodega

class Botella:
    def __init__(self, tapon_inicial):
        self.corcho = tapon_inicial 

class Sacacorchos:
    def __init__(self):
        self._corcho_extraido = None 

    def destapar(self, envase):
        if envase.corcho is None:
            raise Exception("Error: La botella ya se encuentra destapada.")
        if self._corcho_extraido is not None:
            raise Exception("Error: El sacacorchos ya tiene un corcho incrustado.")

        self._corcho_extraido = envase.corcho
        envase.corcho = None

    def limpiar(self):
        if self._corcho_extraido is None:
            raise Exception("Error: No hay ningún corcho para limpiar en la herramienta.")
        self._corcho_extraido = None
"""
"""
Ejercicio 4
1. Crear la clase padre Restaurante que guarde nombre y tipo de comida en su inicializador.
2. Sumarle métodos para mostrar la información del local y para avisar que abrió sus puertas.
3. Crear una clase hija llamada Heladeria que herede todo de Restaurante.
4. Agregarle a la heladería un atributo nuevo que sea una lista con los gustos disponibles y un método para imprimirlos en pantalla.
5. Crear una instancia de tu heladería y llamar a todos los métodos para probarlos.
"""
"""
class Restaurante:
    def __init__(self, nom_local, cat_gastronomica):
        self.restaurante_nombre = nom_local
        self.tipo_comida = cat_gastronomica

    def describir_restaurante(self):
        print(f"Establecimiento: {self.restaurante_nombre} | Especialidad: {self.tipo_comida}")

    def abrir_restaurante(self):
        print(f"El restaurante {self.restaurante_nombre} ahora está abierto al público.")

class Heladeria(Restaurante):
    def __init__(self, nom_local, cat_gastronomica, lista_gustos):
        super().__init__(nom_local, cat_gastronomica)
        self.sabores = lista_gustos

    def mostrar_sabores(self):
        print("Nuestra cartelera de sabores disponibles:")
        for gusto in self.sabores:
            print(f" - {gusto}")

mi_heladeria = Heladeria("Helados del Valle", "Postres Helados", ["Dulce de Leche", "Granizado", "Limón"])
mi_heladeria.describir_restaurante()
mi_heladeria.abrir_restaurante()
mi_heladeria.mostrar_sabores()
"""
"""
Ejercicio 5
1. Escribir la clase padre Personaje con atributos de vida, posición y velocidad.
2. Darle a los personajes métodos para moverse y para recibir daño (si la vida cae a cero o menos, debe lanzar una excepción).
3. Crear una clase hija Soldado que sume daño de ataque y un método específico para atacar y restarle vida a otro personaje.
4. Crear una clase hija Campesino que sume capacidad de cosecha y un método para recolectar.
"""
"""
class Personaje:
    def __init__(self, hp_inicial, ubicacion_x, vel_movimiento):
        self.puntos_vida = hp_inicial
        self.coordenada = ubicacion_x
        self.rapidez = vel_movimiento

    def recibir_ataque(self, danio_recibido):
        self.puntos_vida -= danio_recibido
        if self.puntos_vida <= 0:
            raise Exception("El personaje ha sido eliminado (HP llegó a 0 o menos).")

    def mover(self, sentido_direccion):
        print(f"Moviéndose hacia {sentido_direccion} a {self.rapidez} unidades por turno.")

        
class Soldado(Personaje):
    def __init__(self, hp_inicial, ubicacion_x, vel_movimiento, poder_fuego):
        super().__init__(hp_inicial, ubicacion_x, vel_movimiento)
        self.poder_fuego = poder_fuego

    def atacar(self, objetivo):
        print(f"Atacando al objetivo y causando {self.poder_fuego} de daño.")
        objetivo.recibir_ataque(self.poder_fuego)

class Campesino(Personaje):
    def __init__(self, hp_inicial, ubicacion_x, vel_movimiento, capacidad_recoleccion):
        super().__init__(hp_inicial, ubicacion_x, vel_movimiento)
        self.capacidad_recoleccion = capacidad_recoleccion

    def cosechar(self):
        print(f"Recolectando recursos...")
        return self.capacidad_recoleccion
"""
"""
Ejercicio 6
1. Armar la clase Usuario con nombre, apellido y un par de atributos extra típicos de un perfil (ej. mail, edad).
2. Escribir un método para imprimir el resumen de la cuenta y otro para mostrar un mensaje de saludo usando el nombre del usuario.
3. Crear un par de perfiles distintos (instancias) y usar los dos métodos en cada uno.
"""
"""
class Usuario:
    def __init__(self, nom, ape, nickname, nivel_cuenta, juegos_favoritos):
        self.nombre = nom
        self.apellido = ape
        self.nickname = nickname
        self.nivel = nivel_cuenta
        self.juegos = juegos_favoritos

    def describir_usuario(self):
        print(f"--- Perfil de {self.nickname} ---")
        print(f"Nombre real: {self.nombre} {self.apellido}")
        print(f"Nivel de perfil: {self.nivel}")
        print(f"Títulos más jugados: {', '.join(self.juegos)}\n")

    def saludar_usuario(self):
        print(f"¡Qué onda {self.nickname}! Bienvenido de nuevo al server.\n")

user_1 = Usuario("Augusto", "Lisi", "AuguMaster", 42, ["Counter-Strike 2", "Minecraft"])
user_2 = Usuario("Tomás", "García", "TomiTWD", 15, ["The Walking Dead", "Left 4 Dead 2"])
user_3 = Usuario("Sofia", "Martínez", "SofiCraft", 28, ["Minecraft", "Roblox"])

for usr in [user_1, user_2, user_3]:
    usr.saludar_usuario()
    usr.describir_usuario()
"""  
"""
Ejercicio 7
1. Crear una clase Admin que herede de la clase Usuario del punto anterior.
2. Sumarle un atributo extra que almacene una lista de textos con los permisos que tiene (ej: "banear", "borrar").
3. Escribir un método para mostrar esos privilegios en pantalla, crear un usuario administrador y probarlo.
"""
"""
class Admin(Usuario):
    def __init__(self, nom, ape, nickname, nivel_cuenta, juegos_favoritos):
        super().__init__(nom, ape, nickname, nivel_cuenta, juegos_favoritos)
        self.privilegios = [
            "puede kickear jugadores",
            "puede banear temporalmente",
            "puede cambiar el mapa del server",
            "puede mutear el chat de voz"
        ]

    def mostrar_privilegios(self):
        print(f"Permisos especiales del admin '{self.nickname}':")
        for permiso in self.privilegios:
            print(f" > {permiso}")

mi_admin = Admin("Marcos", "Ruiz", "Moderador_Marcos", 99, ["CS2"])
mi_admin.mostrar_privilegios()
"""
"""
Ejercicio 8
1. Crear una clase completamente nueva llamada Privilegios que se encargue de guardar la lista de permisos y de mostrarlos.
2. Modificar la clase Admin para que, en lugar de guardar la lista suelta, guarde como atributo un objeto entero de esta nueva clase Privilegios.
3. Crear un nuevo administrador y mostrar sus permisos llamando al método a través de la clase que tiene adentro.
"""
"""
class Privilegios:
    def __init__(self, lista_permisos):
        self.privilegios = lista_permisos

    def mostrar_privilegios(self):
        print("Listado de autorizaciones activas:")
        for p in self.privilegios:
            print(f" - {p}")

class Admin(Usuario):
    def __init__(self, nom, ape, nickname, nivel_cuenta, juegos_favoritos):
        super().__init__(nom, ape, nickname, nivel_cuenta, juegos_favoritos)

        permisos_base = ["acceso a la consola", "borrar mensajes", "suspender usuarios"]
        self.mis_permisos = Privilegios(permisos_base)

super_admin = Admin("Lucas", "Vega", "AdminSupremo", 100, ["Assetto Corsa"])

super_admin.mis_permisos.mostrar_privilegios()
"""
"""
Ejercicio 9
1. Crear un archivo Python nuevo.
2. Importar la clase Restaurante desde el archivo.
3. Instanciar un local y probar sus métodos para certificar que la importación funciona.
"""
"""
from clases_restaurante import Restaurante

local_comida = Restaurante("La Pizzería del Barrio", "Pizzas y Empanadas")
local_comida.abrir_restaurante()
local_comida.describir_restaurante()
"""