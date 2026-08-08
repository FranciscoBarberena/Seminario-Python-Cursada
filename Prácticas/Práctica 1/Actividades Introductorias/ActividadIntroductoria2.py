cantidadDeSegundos = int(input("Ingrese una cantidad de segundos: "))
cantidadDeHoras = cantidadDeSegundos//3600
segundosRestantes = cantidadDeSegundos - cantidadDeHoras*3600
cantidadDeMinutos = segundosRestantes//60
segundosRestantes -= cantidadDeMinutos*60
print(f"{cantidadDeSegundos} segundos son {cantidadDeHoras} horas, {cantidadDeMinutos} minutos y {segundosRestantes} segundos")