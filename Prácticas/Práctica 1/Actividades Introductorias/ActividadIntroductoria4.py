n = int(input("Ingresa un numero N: "))
for i in range (1,n+1):
    if (i % 5 == 0):
        continue
    print(i)