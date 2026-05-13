#!/usr/bin/env python

# Escreva uma função chamada primoem() que recebe como parâmetro um inteiro
# positivo i e retorna o i-ésimo número primo. Depois escreva um programa que
# usa essa função para retornar os números primos que estão nas posições dentro
# do intervalo [n,m], sendo 0<n≤m definido pelo usuário.


def eh_primo(number):
    if number <= 0:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def primo_em(i):
    counter = 0
    current = 1

    while counter < i:
        current += 1

        if eh_primo(current):
            counter += 1

    return current


start = int(input("Início do intervalo: "))
finish = int(input("Fim do intervalo: "))

for i in range(start, finish + 1):
    print(f"{i}o = {primo_em(i)}")
