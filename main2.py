"""Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga."""

def mas_larga(list):
    longest_word = ""
    for word in list:
        if len(word) > len(longest_word):
            longest_word = word
    print(longest_word)


mas_larga(["apple", "pink", "cinnamon", "window", "computer", "chair", "corporation"])
