def execute4(): 
    def hasDotAfterAt(mail):
        return ('.' in mail.split("@")[1])

    def startAndEndConditions(mail):
        return (not mail.startswith(("@","."))) and not (mail.endswith(("@",".")))

    def validDomain(mail):
        return len(mail.split(".")[-1]) >= 2

    def hasOnlyOneAt(mail):
        return (mail.count("@")==1)

    def isValid(mail: str):
        return (hasOnlyOneAt(mail)) and (hasDotAfterAt(mail)) and (startAndEndConditions(mail)) and (validDomain(mail))

    email = input("Ingrese un email (fin para terminar): ")
    while (email != "fin"):
        if isValid(email):
            print("El email es valido.")
        else:
            print ("El email no es valido.")
        email = input("Ingrese un email (fin para terminar): ")