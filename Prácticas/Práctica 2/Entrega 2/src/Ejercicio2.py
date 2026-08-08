

def obtenerDuracionSegundos(cancion):
    minYSeg = cancion["duration"].split(":")
    return ((int(minYSeg[0])*60) + int(minYSeg[1]))

def convertirParaImpresion(duracionSegundos):
    duracionMinutos = duracionSegundos // 60
    duracionSegundos = duracionSegundos % 60
    if (len(str(duracionSegundos))) == 1:
        duracionSegundos =f"0{duracionSegundos}"
    return f"{duracionMinutos}:{duracionSegundos}"

def execute2():
    playlist = [
    {"title": "Bohemian Rhapsody", "duration": "5:55"},
    {"title": "Hotel California", "duration": "6:30"},
    {"title": "Stairway to Heaven", "duration": "8:02"},
    {"title": "Imagine", "duration": "3:07"},
    {"title": "Smells Like Teen Spirit", "duration": "5:01"},
    {"title": "Billie Jean", "duration": "4:54"},
    {"title": "Hey Jude", "duration": "7:11"},
    {"title": "Like a Rolling Stone", "duration": "6:13"},
    ]
    maxSegundos = 0
    minSegundos = 99999999999
    duracionTotalSegundos = 0
    for song in playlist:
        longitudSegundos = obtenerDuracionSegundos(song)
        if longitudSegundos >maxSegundos:
            maxSegundos = longitudSegundos
            maxCancion = song["title"]
        if longitudSegundos < minSegundos:
            minSegundos = longitudSegundos
            minCancion = song["title"]
        duracionTotalSegundos += longitudSegundos
    
    print (f"Duracion total: {convertirParaImpresion(duracionTotalSegundos)}") #Para facilitar, los minutos y segundos siempre se imprimen con el mismo formato
    print(f'Canción más larga: "{maxCancion}" ({convertirParaImpresion(maxSegundos)})')
    print(f'Cancion mas corta: "{minCancion}" ({convertirParaImpresion(minSegundos)})')
if (__name__ == "__main__"):
    execute2()