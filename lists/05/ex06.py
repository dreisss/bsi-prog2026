#!/usr/bin/env python

# Escreva um programa que cria uma lista de comprimento 15 composta por elementos
# inteiros gerados aleatoriamente no intervalo [1,99] e crie uma outra lista que
# corresponde ao inverso da primeira. No final apresente as duas listas.

from random import randint

list = [randint(1, 99) for _ in range(15)]
reversed = []

for i in range(15):
    reversed.append(list[14 - i])

print(list)
print(reversed)
