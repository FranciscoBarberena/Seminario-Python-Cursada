def execute7():
    import random

    conjuntoDeParticipantes = input("Ingrese los participantes (separados por coma): ").title()
    conjuntoDeParticipantes = conjuntoDeParticipantes.split(",")
    conjuntoDeParticipantes = {participante.strip() for participante in conjuntoDeParticipantes}
    conjuntoDeParticipantes = (random.sample(tuple(conjuntoDeParticipantes), len(conjuntoDeParticipantes)))
    if len(conjuntoDeParticipantes)>=3:
        sorteoExitoso = False
        while(not sorteoExitoso):
            aQuienRegala = {}
            regaladoAux = ""
            for participante in conjuntoDeParticipantes:
                regaladoAux = random.sample(conjuntoDeParticipantes,1)[0]
                listaDeLosQueQuedan = [persona for persona in conjuntoDeParticipantes if persona not in aQuienRegala.values()]
                if len (listaDeLosQueQuedan) == 1 and (listaDeLosQueQuedan[0] == participante):
                    break
                
                while (regaladoAux == participante)or(regaladoAux in aQuienRegala.values()):
                    regaladoAux = random.sample(conjuntoDeParticipantes,1)[0]
                aQuienRegala[participante] = regaladoAux
                listaDeLosQueQuedan.remove(regaladoAux)
                sorteoExitoso = (len(listaDeLosQueQuedan) == 0)

        for regalador, regalado in aQuienRegala.items():
            print(f"{regalador} -> {regalado}")
    else:
        print("Se necesitan al menos 3 personas.")

