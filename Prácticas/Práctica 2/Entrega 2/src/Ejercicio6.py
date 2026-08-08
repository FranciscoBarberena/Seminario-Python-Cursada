def execute6():
    from collections import Counter
    posts = [ #Cada post ocupa una sola linea para facilitar la lectura
    "Arrancando el lunes con energía #Motivación #NuevaSemana",
    "Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi",
    "No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
    "Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
    "Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
    "Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
    "Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
    "Finde de lluvia, maratón de series #SerieAdicta #Relax",
    "Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"
    ]

    totalHashtagApperances = []
    for post in posts:
        wordList = post.split()
        for word in wordList:
            if (word.startswith("#")):
                totalHashtagApperances.append(word)

    validHashtags = set(totalHashtagApperances)
    totalHashtags = len(validHashtags)
    hashtagCounts = dict((Counter(totalHashtagApperances)))
    trendingHashtags = [(hashtag, occurrences) for hashtag, occurrences in hashtagCounts.items() if occurrences > 1]
    trendingHashtags.sort(key = lambda tupla: tupla[1], reverse = True)
    print("Hashtags trending (mas de una aparicion): ")
    for hash in trendingHashtags:
        print(f"    {hash[0]}: {hash[1]}")
    print()
    print(f"Total de hashtags unicos: {totalHashtags}")