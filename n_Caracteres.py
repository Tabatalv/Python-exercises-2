"""Escribir una función filtrar_palabras()
 que tome una lista de palabras y un entero n,
 y devuelva las palabras que tengan mas de n caracteres."""

def filtrar_palabras(list, entero):
    l_words = []
    for word in list:
        if len(word) > entero:
            l_words.append(word)

    print(l_words)


filtrar_palabras(["cecilias", "pencil", "blue", "rose", "house", "microwave", "greeting"], 5)



