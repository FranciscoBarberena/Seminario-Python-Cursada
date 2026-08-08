


def execute1():
    text = """Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!"""
    listaPorLineas = text.split("\n")
    listaPorPalabras = text.split()
    cantidadDeLineas = len(listaPorLineas)
    cantidadDePalabras = len(listaPorPalabras)
    promedioPorLinea = cantidadDePalabras / cantidadDeLineas
    listaDeLineasQueSuperanPromedio = [linea for linea in listaPorLineas if len(linea.split())>promedioPorLinea]
    print(f"Total de lineas: {cantidadDeLineas}")
    print(f"Total de palabras: {cantidadDePalabras}")
    print(f"Promedio de palabras por linea: {round(promedioPorLinea,2)}")
    print(f"Lineas por encima del promedio ({round(promedioPorLinea,2)} palabras):")
    for linea in listaDeLineasQueSuperanPromedio:
        print(f'- {linea}" ({len(linea.split())} palabras)')
    

if (__name__ == "__main__"):
    execute1()