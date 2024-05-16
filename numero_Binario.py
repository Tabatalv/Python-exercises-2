"""Construir un pequeño programa que convierta números binarios en enteros."""

n_binario = input("Type the binary number you want to turn into an integer: ")

numbers = [int(num) for num in n_binario]
index = 0
integer = 0

for n in numbers:
    integer += n * 2 ** index
    index += 1
print(integer)

