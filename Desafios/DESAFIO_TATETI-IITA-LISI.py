"""
Desafio primer caracter
1. Recrear el mitico juego TA-TE-TI, pero para jugarlo en consola. 
"""

tateti = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
turno = "X"
turnos = 0
posiciones_ganadoras = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

while True:
    print(tateti[0], "|", tateti[1], "|", tateti[2])
    print("---------")
    print(tateti[3], "|", tateti[4], "|", tateti[5])
    print("---------")
    print(tateti[6], "|", tateti[7], "|", tateti[8])
    
    print(f"Turno de {turno}")
    posicion = int(input("Ingrese un numero: "))
    
    if posicion >= 1 and posicion <= len(tateti):
        indice = posicion - 1
        if tateti[indice] != "X" and tateti[indice] != "O":
            tateti.pop(indice)
            tateti.insert(indice, turno)
            turnos = turnos + 1
            
            hay_ganador = False
            for contador in range(len(posiciones_ganadoras)):
                a = posiciones_ganadoras[contador][0]
                b = posiciones_ganadoras[contador][1]
                c = posiciones_ganadoras[contador][2]
                if tateti[a] == tateti[b] and tateti[b] == tateti[c]:
                    hay_ganador = True
                    
            if hay_ganador:
                print(tateti[0], "|", tateti[1], "|", tateti[2])
                print("---------")
                print(tateti[3], "|", tateti[4], "|", tateti[5])
                print("---------")
                print(tateti[6], "|", tateti[7], "|", tateti[8])
                print(f"Ganó {turno}")
                break
                
            if turnos == len(tateti):
                print(tateti[0], "|", tateti[1], "|", tateti[2])
                print("---------")
                print(tateti[3], "|", tateti[4], "|", tateti[5])
                print("---------")
                print(tateti[6], "|", tateti[7], "|", tateti[8])
                print("Hay empate")
                break
                
            if turno == "X":
                turno = "O"
            else:
                turno = "X"
        else:
            print("Error")
    else:
        print("Error")
