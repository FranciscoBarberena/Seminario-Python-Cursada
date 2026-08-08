n = int(input("Ingresa un numero N: "))
listaNumeros = []
listaDeMultiplosCinco = []
for i in range (1,n+1):
    if (i % 5 == 0):
        listaDeMultiplosCinco.append(i)
    else:
        listaNumeros.append(i)
print(f"Lista original: {listaNumeros}")
print(f"Lista de múltiplos de 5: {listaDeMultiplosCinco}")