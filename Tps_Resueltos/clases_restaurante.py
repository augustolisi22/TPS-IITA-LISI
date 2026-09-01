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
        # Llamamos al constructor de la clase padre (Restaurante)
        super().__init__(nom_local, cat_gastronomica)
        self.sabores = lista_gustos

    def mostrar_sabores(self):
        print("Nuestra cartelera de sabores disponibles:")
        for gusto in self.sabores:
            print(f" - {gusto}")
