#!/usr/bin/env python

# Escreva uma função maior(a,b) que recebe dois números inteiros como parâmetros
# e retorna o maior deles. Depois disso escreva um programa que leia dois números
# inteiros pelo teclado e use a função para determinar qual deles é o maior.


def maior(a, b):
    if a > b:
        return a
    else:
        return b


n1 = int(input("1o número: "))
n2 = int(input("2o número: "))

print(f"Maior = {maior(n1, n2)}")
