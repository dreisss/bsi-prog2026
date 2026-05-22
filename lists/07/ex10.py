#!/usr/bin/env python

# Implemente uma função recursiva chamada conta_digito() que tem como parâmetros
# um número inteiro não nulo e um dígito e retorna quantas vezes esse dígito aparece
# nesse número inteiro. Depois implemente um programa que leia um inteiro e um dígito
# para mostrar quantas vezes esse dígito aparece no inteiro usando essa função.


def conta_digito(n, d):
    if n == 0:
        return 0
    elif n % 10 == d:
        return 1 + conta_digito(n // 10, d)
    else:
        return conta_digito(n // 10, d)


n = int(input("Número: "))
d = int(input("Dígito: "))

print(f"O dígito {d} aparece {conta_digito(n, d)} vez(es) no número {n}")
