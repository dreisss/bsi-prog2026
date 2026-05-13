#!/usr/bin/env python

# Escreva uma função chamada mdc() que recebe dois números inteiros como parâmetros
# e retorna um inteiro que corresponde ao maior divisor comum desses números. Depois
# escreva um programa que calcular o MDC de dois números dados pelo usuários.


def mdc(n1, n2):
    # algoritmo de euclides

    while n2 != 0:
        r = n1 % n2
        n1 = n2
        n2 = r

    return n1


n1 = int(input("1o número: "))
n2 = int(input("2o número: "))
print(f"mdc({n1}, {n2}) = {mdc(n1, n2)}")
