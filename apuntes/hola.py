n=int(input("ingresar N: "))
Suma=0
Inv=0
Cont=0
while n>0:
    digito=n%10
    Inv=Inv*10+digito
    n=n//10
    Cont=Cont+1
    if Cont==16:
        for i in range (1,17):
            digito= Inv%10
            if i%2==0:
                digito=digito * 2
                if digito > 9:
                    digito=digito-9
                    Suma=Suma+digito
                else:
                    Suma=Suma+digito
                Inv=Inv//10
        if Suma%10==0:
            print("la tarjeta es valida")
        else:
            print("la tarjeta no es valida")