suma=0
x=3


for i in range(x):
    nota= float(input("ingrese nota: "))

    if nota >5 or nota <1:
        print("excede el rango de notas")
        x=x+1
    else:
        suma= suma+nota
    
promedio=suma/3

print("el promedio es: ", promedio)

if promedio >= 3:
    print ("aprobado")
else:
    print ("reprobo")
