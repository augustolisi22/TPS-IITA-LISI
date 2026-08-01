dicc = [{"nombre": "carlos", "apellido": "zapata", "DNI": "48.106.542", "notas": [7,9,4,1,10]}, 
{"nombre": "maría", "apellido": "reina", "DNI": "47.950.373", "notas": [8,5,7,6,8]},
{"nombre": "miguel", "apellido": "martinez", "DNI": "48.050.010", "notas": [3,2,5,6,3]}]

agregar=input("¿Desea agregar alumnos?: ")
while agregar != "no":
    nombre=input("Nombre del alumno: ")
    apellido=input("Apellido del alumno: ")
    documento=int(input("Documento del alumno: "))
    notas=[]
    contador=0
    while contador<5:
        notas_al=int(input("ingresar notas del alumno: "))
        contador+=1
        notas.append(notas_al)
    dicc.append({"nombre": nombre, "apellido": apellido, "DNI": documento, "notas": notas})
    salir=input("¿Desea dejar de agregar?:")
    if salir == "si":
        break
    
numero_alumno = int(input("Ingrese el numero de lista del alumno: "))
print(f"Los datos del alumno son: {dicc[numero_alumno]}")
