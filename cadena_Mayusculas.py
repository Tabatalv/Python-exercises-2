"""Escribir un programa que le diga al usuario que ingrese una cadena.
 El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene."""

m_number = 0
char = input("Type a word: ")
letter_list = [letter for letter in char]

for m in letter_list:
    if m == m.upper():
        m_number += 1
print(f"The word has: {m_number} upper letters.")



