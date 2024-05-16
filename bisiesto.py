"""Escriba una función es_bisiesto() que determine si un año determinado es un año
bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400"""

def is_leap_year(year):
    if year % 4 == 0 and year % 100 == 0:
        print("Leap year.")
    else:
        print("Not a leap year.")


is_leap_year(2020)
