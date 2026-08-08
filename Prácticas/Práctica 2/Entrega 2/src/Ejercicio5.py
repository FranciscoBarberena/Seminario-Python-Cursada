def execute5(): 
    def getPrice(zone, weight):
        match weight:
            case weight if 0<weight<=1:
                return pricesTable[zone][0]
            case weight if 1<weight<=5:
                return pricesTable[zone][1]
            case weight if weight>5:
                return pricesTable[zone][2]


    pricesTable =  {"local" : (500,1000,2000), "regional": (1000,2500,5000), "nacional": (2000,4500,8000)}
    validZones = ("local","regional","nacional")
    package = {"weight": 0,"zone": ""}
    package["weight"] = float(input("Ingrese el peso del paquete en kg (0 para terminar): "))
    while(package["weight"] != 0):
        package["zone"] = input("Ingrese la zona de destino (local/regional/nacional): ").lower()
        while not(package["zone"] in validZones):
            print("Zona no valida. Las zonas disponibles son: local, regional, nacional.")
            package["zone"] = input("Ingrese la zona de destino (local/regional/nacional): ").lower()
        print(f"Costo de envio: ${getPrice(package["zone"],package["weight"])}")
        package["weight"] = float(input("Ingrese el peso del paquete en kg (0 para terminar): "))
