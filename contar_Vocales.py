"""Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a"
 tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra."""


def count_vocals(char):
    vocal_count = []
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    word = [letter for letter in char.lower()]
    for vocal in word:
        a += vocal.count("a")
        e += vocal.count("e")
        i += vocal.count("i")
        o += vocal.count("o")
        u += vocal.count("u")

    print(f"The word has: {a} a, {e} e, {i} i, {o} o, and {u} u. ")

count_vocals("Oil")


