list=[]

for user in range (4):
    nombre=input("ingrese el nombre de la persona: ")

    nota=float(input("ingrese la nota:" ))

    while nota >5 or nota < 0:

        print("nota invalida. por favor ingrese de nuevo")
        
        nota=float(input("ingrese la nota:" ))
    
    usuario ={"nombre":nombre,"nota":nota}
    
    list.append(usuario)

print(list)
