
def execute3():
    review = """La película sigue a un grupo de astronautas que
    viajan a Marte
    en una misión de rescate. El capitán Torres lidera al equipo
    a través
    de tormentas solares y fallos en el sistema de navegación. Al
    llegar
    a Marte descubren que la base está abandonada y los
    suministros
    destruidos. Torres decide sacrificar la nave nodriza para
    salvar
    al equipo y logran volver a la Tierra en una cápsula de
    emergencia.
    El final revela que Torres sobrevivió gracias a un pasaje
    secreto."""

    setPalabrasSpoiler= (input("Ingrese las palabras spoiler (separadas por coma): ")).lower().split(",")
    setPalabrasSpoiler = set([spoiler.strip() for spoiler in setPalabrasSpoiler])
    listaCompletaDePalabras = review.split()
    reviewSinSpoilers=""
    for palabra in listaCompletaDePalabras:
        if palabra.lower() in setPalabrasSpoiler:
            reviewSinSpoilers += f"{len(palabra)*"*"} "
        else:
            reviewSinSpoilers+= f"{palabra} "
    print(reviewSinSpoilers)
    
if (__name__ == "__main__"):
    execute3()