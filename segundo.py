nombre=input("deme su nombre: ")

n1=float(input("ingrese la nota: "))
n2=float(input("ingrese la nota: "))
n3=float(input("ingrese la nota: "))

nota=float((n1+n2+n3)/3)

if nota > 5 or nota < 1:

    print(" la nota no puede ser mayor que 5 y menor que 0 ")

elif nota >= 3:

    print("el promedio de",nombre,"es:",nota)
    print("gano")
else:
    
    print("el promedio de",nombre,"es:",nota)
    print("perdio")
   






