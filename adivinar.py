import random
secreto= random.randint(1,10)
inten= 3


print("tienes", inten ,"intentos")

user= int(input("adivina el numero entre 1 a 10: "))

while user > 10 or user < 1:

    print("solo puede ingresar numero de 1 a 10")

    user= int(input("adivina el numero entre 1 a 10: "))

    while user != secreto:

        for vida in range(inten):

            if user < secreto:
                print("el numero es mayor",secreto)
                inten = inten - 1
                print("te quedan",inten)
            else:
                print(" el numero es menor")
                inten = inten - 1
                print("te quedan",inten)

            user= int( input("adivina de nuevo: "))


        



if user : secreto
print ("felicidades el numero es",secreto)