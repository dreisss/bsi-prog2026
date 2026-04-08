#!/usr/bin/env python

# Escreva um programa para mostrar todos os números divisíveis
# por 5 dentro do intervalo [0,N]. Garanta que N seja maior que 0.

n = int(input("Valor de N: "))

if n <= 0:
    print("Valor de N inválido!")
else:
    for i in range(0, n + 1):
        if i % 5 == 0:
            print(i, end=" " if i != n else "")
