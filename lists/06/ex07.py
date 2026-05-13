#!/usr/bin/env python

# Escreva uma funcao chamada eh_primo() que recebe um número inteiro como parâmetro
# e retorna True se esse número for primo e False caso contrário. Depois escreva
# um programa que usa essa função para identificar se um número dado pelo usuário
# é ou não primo.


def eh_primo(number):
    if number <= 0:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


number = int(input("Digite um número: "))
is_prime = eh_primo(number)

if is_prime:
    print("Número primo")
else:
    print("Não é primo")
