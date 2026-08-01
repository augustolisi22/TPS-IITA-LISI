numero_alumno = int(input("Ingrese el numero de lista del alumno: "))
dicc = [{"nombre": "carlos", "apellido": "zapata", "DNI": "48.106.542", "notas": [7,9,4,1,10]}, 
{"nombre": "maría", "apellido": "reina", "DNI": "47.950.373", "notas": [8,5,7,6,8]},
{"nombre": "miguel", "apellido": "martinez", "DNI": "48.050.010", "notas": [3,2,5,6,3]}]
print(f"Los datos del alumno son: {dicc[numero_alumno]}")
