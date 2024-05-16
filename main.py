"""La función max() del ejercicio 1 (primera parte) y la función max_de_tres()
 del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números.
  Supongamos que tenemos mas de 3 números o no sabemos cuantos números son.
 Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande."""

def max_in_list(list):
    highest_number = 0
    for number in list:
        if number > highest_number:
            highest_number = number
    print(highest_number)


max_in_list([30, 200, 450, 1, 22])
