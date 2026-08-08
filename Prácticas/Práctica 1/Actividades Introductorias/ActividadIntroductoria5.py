total = 0
while True:
    precio= float(input("Ingresa un precio: $"))
    if (precio == 0):
        break
    total+=precio
print(f"El total fue ${total}")