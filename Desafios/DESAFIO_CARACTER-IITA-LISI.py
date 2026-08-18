"""
Desafio primer caracter
1. Encontrar el primer carácter no repetido en un string.
(no se pueden usar ciclos anidados)
"""

palabra = input("Ingrese palabra/s: ")
contador = 0

while contador < len(palabra):
    letra = palabra[contador]
    resto = palabra[0:contador] + palabra[contador + 1:len(palabra)]                #todo menos el caracter que esté en la variable letra
    
    if letra not in resto:
        print(f"El primer caracter que no se repite es: {letra}")
        break
        
    contador += 1