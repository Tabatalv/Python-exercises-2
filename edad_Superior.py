"""Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
"""


def ages(list):
    age_above_20 = 0
    for age in list:
        if age >= 20:
            age_above_20 += 1
    print(age_above_20)


ages([20, 40, 11, 1, 87, 17])


