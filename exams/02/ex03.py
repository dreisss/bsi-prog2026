# Escreva uma função recursiva chamada soma_naturais() que receba um número
# inteiro positivo n e retorne a soma dos números naturais de 1 até n. Depois
# escreva um programa que leia um número natural e apresente o resultado da
# função dando a ela o número lido.


def soma_naturais(n):
    if n == 0:
        return 0
    else:
        return n + soma_naturais(n - 1)


n = int(input("Digite um número natural: "))

if n < 0:
    print(f"{n} não é um número natural")
else:
    print(f"Somatório de 0 até {n} = {soma_naturais(n)}")
