#!/usr/bin/env python

# Elabore um programa que cria uma lista com 10 números inteiros aleatórios dentro
# do intervalo [0,99]. Uma vez que a lista estiver pronta, procure nela pelo maior
# e menor valor que ela contém. No final apresente a lista, o maior valor e o
# menor valor.

from random import randint

list = []

for i in range(10):
    list.append(randint(0, 99))


print(list)

list.sort()

print(f"Maior = {list[9]}")
print(f"Menor = {list[0]}")
