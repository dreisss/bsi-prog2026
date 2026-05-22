#!/usr/bin/env python

# A sequência de Fibonacci é uma sequência numérica em que cada termo, a partir
# do terceiro, é obtido pela soma dos dois termos anteriores. Ela começa assim:
# 1,1,2,3,5,8,13,.... Isso quer dizer que a sequência de Fibonacci tem uma forma
# recursiva, sendo F(1)=1, F(2)=1 e F(n)=F(n−1)+F(n−2), para todo n>2. Escreva
# uma função chamada fibonacci() que tem como parâmetro um inteiro positivo i e
# retorna o i-ésimo número da sequência de Fibonacci calculado de forma recursiva.
# Depois escreva um programa que lê um número que representa uma posição e apresenta
# o elemento da sequência de Fibonacci dessa posição.


def fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Diga a posição: "))
print(f"O {n}o número da sequência de Fibonacci é {fibonacci(n)}")
