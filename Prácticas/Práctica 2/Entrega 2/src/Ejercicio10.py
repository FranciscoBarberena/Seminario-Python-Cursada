rounds = [
    {
    'theme': 'Entrada',
    'scores': {
    'Valentina': {'judge_1': 8, 'judge_2': 7,
    'judge_3': 9},
    'Mateo': {'judge_1': 7, 'judge_2': 8,
    'judge_3': 7},
    'Camila': {'judge_1': 9, 'judge_2': 9,
    'judge_3': 8},
    'Santiago': {'judge_1': 6, 'judge_2': 7,
    'judge_3': 6},
    'Lucía': {'judge_1': 8, 'judge_2': 8,
    'judge_3': 8},
    }
    },
    {
    'theme': 'Plato principal',
    'scores': {
    'Valentina': {'judge_1': 9, 'judge_2': 9,
    'judge_3': 8},
    'Mateo': {'judge_1': 8, 'judge_2': 7,
    'judge_3': 9},
    'Camila': {'judge_1': 7, 'judge_2': 6,
    'judge_3': 7},
    'Santiago': {'judge_1': 9, 'judge_2': 8,
    'judge_3': 8},
    'Lucía': {'judge_1': 7, 'judge_2': 8,
    'judge_3': 7},
    }
    },
    {
    'theme': 'Postre',
    'scores': {
    'Valentina': {'judge_1': 7, 'judge_2': 8,
    'judge_3': 7},
    'Mateo': {'judge_1': 9, 'judge_2': 9,
    'judge_3': 8},
    'Camila': {'judge_1': 8, 'judge_2': 7,
    'judge_3': 9},
    'Santiago': {'judge_1': 7, 'judge_2': 7,
    'judge_3': 6},
    'Lucía': {'judge_1': 9, 'judge_2': 9,
    'judge_3': 9},
    }
    },
    {
    'theme': 'Cocina internacional',
    'scores': {
    'Valentina': {'judge_1': 8, 'judge_2': 9,
    'judge_3': 9},
    'Mateo': {'judge_1': 7, 'judge_2': 6,
    'judge_3': 7},
    'Camila': {'judge_1': 9, 'judge_2': 8,
    'judge_3': 8},
    'Santiago': {'judge_1': 8, 'judge_2': 9,
    'judge_3': 7},
    'Lucía': {'judge_1': 7, 'judge_2': 7,
    'judge_3': 8},
    }
    },
    {
    'theme': 'Final libre',
    'scores': {
    'Valentina': {'judge_1': 9, 'judge_2': 8,
    'judge_3': 9},
    'Mateo': {'judge_1': 8, 'judge_2': 9,
    'judge_3': 8},
    'Camila': {'judge_1': 7, 'judge_2': 7,
    'judge_3': 7},
    'Santiago': {'judge_1': 9, 'judge_2': 9,
    'judge_3': 9},
    'Lucía': {'judge_1': 8, 'judge_2': 8,
    'judge_3': 7},
    }
    }
    ]


def execute10():
    
    def updateMaxRound(score,maxRounds,name):
        if score > maxRounds[name]:
            maxRounds[name] = score

    def getOrderedRound(scores, orderedRound,wonRounds,maxRounds):
        for name in scores:
            orderedRound[name] += sum(scores[name].values())
            updateMaxRound(sum(scores[name].values()), maxRounds,name)
        orderedRound = dict(sorted(orderedRound.items(), key = lambda round: round[1],reverse=True) )#Ordena por score  [(valentina, 30),(juancito, 24)]
        return list(orderedRound.items())

    wonRounds = {"Valentina": 0, "Mateo": 0, 
    "Camila": 0,"Santiago": 0, "Lucía": 0}
    totalPoints = wonRounds.copy()
    maxRounds = wonRounds.copy()

    for round in rounds:
        print(f"Ronda {rounds.index(round)+1} - {round["theme"]}")
        orderedRound = {"Valentina": 0, "Mateo": 0, 
    "Camila": 0, "Santiago": 0, "Lucía": 0} 
        orderedRound = getOrderedRound(round["scores"],orderedRound,wonRounds,maxRounds)
        wonRounds[orderedRound[0][0]] += 1
        
        print(f"Ganador/a: {orderedRound[0][0]} ({orderedRound[0][1]} pts)")
        print("--- TABLA DE POSICIONES ---")
        for pair in orderedRound:
            print(f"    {orderedRound.index(pair)+1}. {pair[0]} ({pair[1]} pts)")
            totalPoints[pair[0]] += pair[1]
        print("---------------------------")


    print("Tabla de posiciones final")
    print(f"{"Cocinero":<10}{"Puntaje":<8}{"Rondas ganadas":<16}{"Mejor ronda":<14}{"Promedio":<10}")
    totalPoints = dict(sorted(totalPoints.items(), key = lambda round: round[1],reverse=True))
    print("---------------------------------------------------------")

    for competitor, score in totalPoints.items():
        print(f"{competitor:<10}{score:<8}{wonRounds[competitor]:<16}{maxRounds[competitor]:<14}{score/len(rounds):<10}")

    print("---------------------------------------------------------")
        


if (__name__ == "__main__"):
    execute10()

