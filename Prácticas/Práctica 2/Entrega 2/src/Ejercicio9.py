def execute9():
    import string
    from collections import Counter
    students = [
    {"name": " Ana García ", "grade": "8", "status":
    "aprobado"},
    {"name": "pedro lópez", "grade": "4", "status":
    "DESAPROBADO"},
    {"name": "MARÍA FERNÁNDEZ", "grade": "10", "status":
    "Aprobado"},
    {"name": "ana garcía", "grade": "9", "status":
    "aprobado"},
    {"name": None, "grade": "7", "status": "aprobado"},
    {"name": "Luis Martínez ", "grade": None, "status":
    "aprobado"},
    {"name": " carlos RUIZ", "grade": "6", "status":
    "aprobado"},
    {"name": "PEDRO LÓPEZ ", "grade": "3", "status":
    "desaprobado"},
    {"name": " ", "grade": "5", "status": "aprobado"},
    {"name": "María Fernández", "grade": "7", "status":
    "APROBADO"},
    {"name": "Sofía Torres", "grade": "9", "status":
    "Aprobado"},
    {"name": " sofía torres ", "grade": "8", "status":
    "aprobado"},
    {"name": "Carlos Ruiz", "grade": "6", "status":
    "APROBADO"},
    {"name": "Roberto Díaz", "grade": "absent", "status":
    "ausente"},
    {"name": "roberto díaz", "grade": "", "status":
    "Ausente"},
    {"name": None, "grade": None, "status": None},
    {"name": "Laura Méndez", "grade": "7", "status":
    "aprobado"},
    {"name": " laura méndez", "grade": "8", "status":
    "Aprobado"},
    {"name": "GABRIELA RÍOS", "grade": "5", "status":
    "aprobado"},
    {"name": "gabriela ríos ", "grade": "4", "status":
    "Desaprobado"},
    ]

    def isInvalidName(name): #nulo, vacío o solo espacios.
        return (name == None) or (name.isspace())

    def isInvalidGrade(grade):
        return (grade == None) or (not grade.isdigit())

    def convertToTitle(student):
        student["name"] = student["name"].title().strip()
        student["status"] = student["status"].title().strip()   

    students = list(filter(lambda student: not isInvalidName(student["name"]),students)) #Borra nombre invalidos
    students = list(filter(lambda student: not isInvalidGrade(student["grade"]),students)) #Borra notas invalidas
    for student in students:
        convertToTitle(student) #Convierte nombres y estados a titulo (de esta manera los nombres de los duplicados son exactamente iguales)
    #Encontrar repetidos
    listaDeNombres = [student["name"] for student in students]
    nameAppearances = dict(Counter(listaDeNombres))
    listaDeRepetidos = [student for student, amount in nameAppearances.items() if amount > 1]
    students.sort(key = lambda student: int(student["grade"]))
    #Eliminar la primera aparicion de cada alumno repetido(están ordenadas de menor a mayor, así que se borra la más baja) 
    while(listaDeRepetidos):
        for student in students:
            if student["name"] in listaDeRepetidos:
                students.remove(student)
                listaDeRepetidos.remove(student["name"])
                break
    students.sort(key = lambda student: student["name"])
    #Imprimir tabla
    print("Registros limpios de los alumnos: ")
    print(f"{"Nombre":^16}{"Nota":^4}{"Estado":^12}")
    print("------------------------------------------")
    for student in students:
        print(f"{student["name"]:^16}{student["grade"]:^4}{student["status"]:^12}")
    print()
    print(f"Total de alumnos validos: {len(students)}")
        


