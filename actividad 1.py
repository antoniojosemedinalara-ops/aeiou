x= int(input("ingrese la cantidad de personas que desea ingresar: "))

for i in range(x):
   nombre = input("Ingrese su nombre: ")
   edad = int(input("por favor " + nombre + " ingrese su edad: "))

   while edad>=120 or edad <= 0:
      print("la edad que registro no es valida", nombre, "por favor ingrese una edad valida")
      edad = int(input("por favor " + nombre + " ingrese su edad: "))
   if edad >= 18:
      print("Acceso permitido un gusto " + nombre + "!")
   else:
      print("Acceso denegado", nombre, "usted es menor de edad")
      