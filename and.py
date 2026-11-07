
logica = True

while True:

    parcial1= float(input("Ingrese nota de parcial1: "))
    parcial2= float(input("Ingrese nota de parcial2: "))

    if parcial1 < 0 or parcial1 > 5 or parcial2 < 0 or parcial2 >5:
        print("NOTA INVALIDA.ingrese de nuevo las notas")
        parcial1 = float(input("Ingrese nota de parcial1: "))
        parcial2 = float(input("Ingrese nota de parcial2: "))
    elif parcial1 >=3 and parcial2>=3:
        print("no hace parcial 3")
        break
    else:
        print("hace parcial 3")
        break


