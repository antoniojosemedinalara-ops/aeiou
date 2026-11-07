def suma(n1,n2):
    x= n1 + n2

    match x:

        case 15:
            print(" el numero es 15")
        case 10:
            print("el numero es 10")
        case _:
            print("el numero no es ni 15 ni 10")

    return x



print(suma(3,7))
print(suma(9,6))