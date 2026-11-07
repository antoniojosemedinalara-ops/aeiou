N=[14,25,42,31,19,8,50,73,11,22]

N_pares=[]
N_impares=[]

for N in N:
    if N%2!=0:
        N_impares.append(N)
    else:
        N_pares.append(N)

print("lista de numeros pares:",N_pares)
print("cantidad de pares:",len(N_pares))
print("lista de nuemros impares:",N_impares)
print("cantidad de impares:",len(N_impares))







