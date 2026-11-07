
cliente= int(input("ingrese l categoria del cliente(para A:1),(para B:2),(para C:3): "))

while cliente>3 or cliente<1:
    print ("numero invalido porfavor ingrese nuevamente")

    cliente= int(input("ingrese l categoria del cliente(para A:1),(para B:2),(para C:3): "))
match cliente:

    case 1:

        ingresoA = int(input("valor de compra:"))

        if ingresoA > 100000:
            descontado= ingresoA*20/100
            descuento= ingresoA - descontado
            print("descuento  aplicado: 20%")
            print(" el valor a pagar es:",descuento,"$")
        elif ingresoA <= 100000:
            descontado1= ingresoA*10/100
            descuento1= ingresoA - descontado1
            print("descuento  aplicado: 10%")
            print("el valor a pagar es:",descuento1,"$")

    case 2:

        ingresoB = int(input("valor de compra:"))

        if ingresoB > 100000:
            descontado2= ingresoB*15/100
            descuento2= ingresoB - descontado2
            print("descuento  aplicado: 15%")
            print("el valor a pagar es:",descuento2,"$")
        elif ingresoB <= 100000:
            descontado3= ingresoB*5/100
            descuento3= ingresoB - descontado3
            print("descuento  aplicado: 5%")
            print("elvalor a pagar es:",descuento3,"$")

    case 3:

        ingresoC= int(input("valor de compra:"))

        descontado4=ingresoC*5/100

        descuento4= ingresoC - descontado4

        print("descuento  aplicado: 5%")

        print("elvalor a pagar es:",descuento4,"$")





            

