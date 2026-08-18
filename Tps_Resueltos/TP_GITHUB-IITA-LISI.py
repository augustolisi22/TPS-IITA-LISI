registro_estudiantes = []
def nuevo_estudiante(base_datos):
    seguir = input("¿Desea agregar un alumno al sistema?: ")
    
    while seguir == "si":
        nombre= input("Ingresar nombre: ")
        apellido = input("Ingresar apellido: ")
        dni = input("Numero de documento: ")
        nacimiento = input("Fecha de nacimiento: ")
        tutor =input("Nombre del tutor responsable: ")
        
        lista_notas = []
        contador_notas = 0

        while contador_notas < 5:
            nota_ingresada = int(input(f"Nota numero {contador_notas + 1}: "))
            lista_notas.append(nota_ingresada)
            contador_notas += 1
            
        inasistencias = int(input("Faltas totales: "))
        amonestaciones_totales = int(input("Amonestaciones totales: "))

        nuevo_diccionario = {
            "Nombre": nombre,
            "Apellido": apellido,
            "DNI": dni,
            "Fecha de nacimiento": nacimiento,
            "Tutor": tutor,
            "Notas": lista_notas,
            "Faltas": inasistencias,
            "Amonestaciones": amonestaciones_totales
        }
        
        base_datos.append(nuevo_diccionario)
        seguir = input("¿Agregar otro estudiante mas?: ")

def ver_registros(base_datos):
    if len(base_datos) == 0:
        print("La lista de la escuela está vacia")
    else:
        posicion = 0
        for estudiante in base_datos:
            print(f"Estudiante: {estudiante["Apellido"]}, {estudiante["Nombre"]} - DNI: {estudiante["DNI"]}")
            print(f"Nacimiento: {estudiante["Fecha de nacimiento"]} | Tutor: {estudiante["Tutor"]}")
            print(f"Calificaciones: {estudiante["Notas"]}")
            print(f"Inasistencias: {estudiante["Faltas"]} | Amonestaciones: {estudiante["Amonestaciones"]}")
            posicion += 1

def editar_estudiante(base_datos):
    ver_registros(base_datos)
    if len(base_datos) > 0:
        indice = int(input("Escribir el ID del alumno a editar: "))
        
        if 0 <= indice < len(base_datos):
            print("¿Que vaa a cambiar?")
            print("1) Notas")
            print("2) Faltas")
            print("3) Amonestaciones")
            eleccion = input("Opcion: ")
            
            if eleccion == "1":
                nuevas_notas = []
                c = 0
                while c < 5:
                    nuevas_notas.append(int(input(f"Nueva nota {c+1}: ")))
                    c += 1
                base_datos[indice]["Notas"] = nuevas_notas
                print("Se guardaron las notas nuevas")
                
            elif eleccion == "2":
                base_datos[indice]["Faltas"] = int(input("Faltas actualizadas: "))
                print("Se actualizaron las faltas")
                
            elif eleccion == "3":
                base_datos[indice]["Amonestaciones"] = int(input("Amonestaciones actualizadas: "))
                print("Se actualizaron las amonestaciones")
                
            else:
                print("Esa opción es incorrecta.")
        else:
            print("Ese ID de alumno no existe en el registro")

def borrar_estudiante(base_datos):
    ver_registros(base_datos)
    if len(base_datos) > 0:
        indice = int(input("Escribir el ID del alumno que quiere borrar: "))
        
        if 0 <= indice < len(base_datos):
            borrado = base_datos.pop(indice)
            print(f"Se elimino a {borrado["Nombre"]} del sistema correctamente")
        else:
            print("El ID ingresado es incorrecto")


menu_activo = True

while menu_activo:
    print("1 - Cargar alumnos")
    print("2 - Ver todos los alumnos")
    print("3 - Editar datos de un alumno")
    print("4 - Eliminar un alumno")
    print("5 - Cerrar programa")
    
    opcion = input("Elegir una opcion: ")
    
    if opcion == "1":
        nuevo_estudiante(registro_estudiantes)
    elif opcion == "2":
        ver_registros(registro_estudiantes)
    elif opcion == "3":
        editar_estudiante(registro_estudiantes)
    elif opcion == "4":
        borrar_estudiante(registro_estudiantes)
    elif opcion == "5":
        print("Cerrando el sistema")
        menu_activo = False
    else:
        print("No existe esa opcion, intentar de nuevo")