import string
def execute8():
    def cypher(message, difference):
        newMessage=""
        for letter in message:
            if letter.isupper():
                pos = (string.ascii_uppercase.index(letter) + difference) % 26
                newCharacter = string.ascii_uppercase[pos]
            elif letter.islower():
                pos = (string.ascii_lowercase.index(letter) + difference) % 26
                newCharacter = string.ascii_lowercase[pos]
            else:
                newCharacter = letter
            newMessage+=newCharacter
        return newMessage

    def decipher (message, difference):
        oldMessage=""
        for letter in message:
            if letter.isupper():
                pos = (string.ascii_uppercase.index(letter) - difference) % 26
                newCharacter = string.ascii_uppercase[pos]
            elif letter.islower():
                pos = (string.ascii_lowercase.index(letter) - difference) % 26
                newCharacter = string.ascii_lowercase[pos]
            else:
                newCharacter = letter
            oldMessage+=newCharacter
        return oldMessage


    message = input("Ingrese un mensaje: ")
    difference = int(input("Ingrese el desplazamiento: "))
    encryprtedMessage = cypher(message,difference)
    print(f"Mensaje cifrado: {cypher(message,difference)}")
    print(f"Mensaje descifrado: {decipher(encryprtedMessage,difference)}")