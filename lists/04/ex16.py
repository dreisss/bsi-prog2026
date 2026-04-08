#!/usr/bin/env python

# Escreva um programa para simular um jogo de adivinhação. Nesse caso, o computador irá sortear um número (pesquise
# sobre o módulo random e a sua função randint) de zero a cem e o usuário terá que acertá-lo. A cada tentativa o computador
# acumula o número de tentativas e dá dicas. A dica consiste em dizer se o palpite é maior ou menor que o número secreto.
# Ao final o programa mostra o número de tentativas utilizadas até descobrir o número. Deixe a semente do random no valor padrão.

from random import randint

number = randint(0, 100)
guess = -10
i = 1

while guess != number:
    guess = int(input(f"Dê seu {i}o palpite: "))

    if guess > number:
        print("O valor é menor")
    elif guess < number:
        print("O valor é maior")

    i += 1

print(f"Acertou com {i-1} tentativa(s)")
