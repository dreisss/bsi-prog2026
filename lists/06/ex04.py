#!/usr/bin/env python

# Escreva uma função chamada fatorial() que recebe como parâmetro um número inteiro
# não negativo e retorna como resultado o fatorial desse número. Depois escreva um
# programa que usa essa função para calcular o fatorial de um número dado pelo usuário.


def fatorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


number = int(input("Digite um número: "))
print(f"Fatorial = {fatorial(number)}")
