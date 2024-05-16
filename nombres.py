"""Definir una lista con un conjunto de nombres, imprimir la cantidad
que comienzan con la letra a. También se puede hacer elegir al usuario la letra a buscar.
"""

def count_letters(list, letter):
    letter_count = 0
    for l in list:
        if l[0] == letter.upper():
            letter_count += 1
    print(letter_count)

count_letters(["Ashley", "Monica", "Saki", "Rose", "Regina", "Charles", "Cindy", "Mei"], "c")
