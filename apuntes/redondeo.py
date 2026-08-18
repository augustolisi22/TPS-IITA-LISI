def redondear(numero):
    entero = int(numero)
    if numero-entero >= 0.5:
        return entero + 1
    else:
        return entero