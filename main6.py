"""Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla."""

year = int(input("Type the year you are in: "))
names = []
births = []
ages = []
for _ in range(3):
    name = input("Type your name: ")
    names.append(name)
    birth = int(input("Type your birth date: "))
    births.append(birth)


for n in births:
    age = 0
    for num in range(n, year):
        age += 1
    ages.append(age)

for pos in range(3):
    print(f"{names[pos]} is {ages[pos]}.")





