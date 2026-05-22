#!/usr/bin/env python

# O fatorial de um número natural n (representado por n!) é o produto de todos
# os inteiros positivos de 1 até n. Ou seja, 5!=5×4×3×2×1=120. Também é possível
# definir o fatorial recursivamente, pois 5!=5×4!=120. Por definição 0!=1.

# Escreva uma função chamada fatorial() que tem como parâmetro um inteiro natural
# e retorna o fatorial desse número calculado de forma recursiva. Depois escreva
# um programa que lê um número e apresenta o seu fatorial usando a função.


def fatorial(n):
    if n in [0, 1]:
        return 1
    else:
        return n * fatorial(n - 1)


n = int(input("Digite o número: "))
print(f"{n}! = {fatorial(n)}")
