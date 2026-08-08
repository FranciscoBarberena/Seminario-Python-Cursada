palabrasValidas = []
print("Ingresá 5 palabras")
for i in range(5):
    palabra = input()
    if len(palabra) > 3:
        palabrasValidas.append(palabra)
oracion = ""
for pal in palabrasValidas:
    oracion += f"{pal} "
print(oracion)

# Existe una funcion join que hace esto 