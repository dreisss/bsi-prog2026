#!/usr/bin/env python

# Escreva um programa que leia dois números que serão respectivamente a quantidade
# de linhas e colunas de uma matriz. Crie essa matriz e a preencha com valores
# inteiros aleatórios no intervalo [0,9]. No final apresente a matriz.

from random import randint

rows = int(input("Número de linhas: "))
columns = int(input("Número de colunas: "))


for i in range(rows):
    print("|" + " ".join([str(randint(0, 9)) for _ in range(columns)]) + "|")

print()
