#!/usr/bin/env python

# Escreva uma função chamada mmc() que recebe dois números inteiros como parâmetros
# e retorna o mínimo múltiplo comum desses números. Depois escreva um programa para
# calcular o MMC de dois números dados pelo usuário. Você pode calcular o MMC a
# partir do MDC, fazendo MMC(a,b)=(a∗b) / MDC(a,b).


def mdc(n1, n2):
    while n2 != 0:
        r = n1 % n2
        n1 = n2
        n2 = r

    return n1


def mmc(n1, n2):
    return n1 * n2 // mdc(n1, n2)


n1 = int(input("1o número: "))
n2 = int(input("2o número: "))
print(f"mmc({n1}, {n2}) = {mmc(n1, n2)}")
