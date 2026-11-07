
Estudiantes=[]
Estudiante={
    "nombre": "",
    "nota": 0.0
}

def ingresar_estudiantes():

    nombre= input("ingrese el nombre del estudiante: ")

    nota=float(input("ingresar nota: "))

    while nota < 1 or nota > 5:
        print("nota invalida.Ingrese una nota entre 1 y 5")
        nota=float(input("ingresar nota: "))

    Estudiante["nombre"] = nombre
    Estudiante["nota"] = nota
    Estudiantes.append(Estudiante.copy())

def mostrar_estudiantes():

    if len(Estudiantes)==0:
        print("no ah ingresado estudiantes")
    else:
        print("estudiantes ingresados:")
        for Estudiante in Estudiantes:
            print(f"nombre: {Estudiante['nombre']}, nota: {Estudiante['nota']}")
            if Estudiante["nota"] >= 3:

                print("aprobo")

            else:
                print("reprobo")

def estadistica_estudiantil():

    if len(Estudiantes)==0:
        
        print("no hay notas para calcular")
    else:

        suma=0
        mayor_nota=3
        menor_nota=3

        for Estudiante in Estudiantes:
            suma = suma + Estudiante["nota"]
            if Estudiante["nota"] > mayor_nota:
                mayor_nota = Estudiante["nota"]
            if Estudiante["nota"] < menor_nota:
                menor_nota = Estudiante["nota"]

    print(f"suma de notas: {suma}")
    print(f"promedio de notas: {suma/len(Estudiantes)}")
    for Estudiante in Estudiantes:
        if Estudiante["nota"] == mayor_nota:
            print(f"mayor nota: {mayor_nota}, Estudiante: {Estudiante['nombre']}")
        if Estudiante["nota"] == menor_nota:
            print(f"menor nota: {menor_nota}, Estudiante: {Estudiante['nombre']}")

while True:

    print("/////MENU/////")
    print("1.Ingresar Estudiante")
    print("2.Mostrar Estudiantes")
    print("3. Estadistica Estudiantil")
    print("4.Salir")

    opcion=int(input("Elija una opcion: "))

    match opcion:

        case 1:
            ingresar_estudiantes()
        case 2:
            mostrar_estudiantes()
        case 3:
            estadistica_estudiantil()
        case 4:
            print("saliendo del programa")
            break

        case _:
            print("opcion invalida, intente de nuevo")




        

