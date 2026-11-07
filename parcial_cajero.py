saldo_inicial= 500000

print("//////CAJERO AUTOMATICO//////")
print("1.Consultar saldo")
print("2.Depositar")
print("3.Retirar dinero")
print("4.salir")

opcion=int(input("que desea realizar: "))

while opcion>4 or opcion<1:
    print("opcion invalida. porfavor ingrese de nuevo")
    opcion=int(input("que desea realizar: "))
match opcion:

    case 1:
        print ("su saldo es de:", saldo_inicial,"$")
    case 2:
        print("cunto desea depositar?")
        suma= int(input("valor a ingresar: "))
        saldo_final= saldo_inicial + suma
        print("su saldo final es de: ", saldo_final,"$")

    case 3:
        print("cuanto desea retirar?")
        retiro= int(input("valor a retirar: "))

        while retiro > saldo_inicial:
            print("opcion no valida, no cuenta con saldo suficiente para ese retiro")
            retiro= int(input("valor a retirar: "))
        saldo_final1= saldo_inicial - retiro
        print("su saldo resultante es:",saldo_final1,"$")

    case 4:
        print("Tenga buen dia =D")
    
