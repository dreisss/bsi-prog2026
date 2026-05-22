#!/usr/bin/env python

# A multiplicação de dois números inteiros não negativos pode ser entendida como
# uma soma repetida. Por exemplo: 3×5=3+3+3+3+3. Pensando recursivamente, esse
# mesmo exemplo pode ser entendido como 3×5=3+(3×4). Escreva uma funcao recursiva
# chamada multiplicacao() que tem dois números inteiros não negativos como
# parâmetros e retorna a multiplicação desses dois números. A ideia aqui é
# exercitar a definição recursiva da multiplicação, portanto implemente esse
# método recursivamente. Depois escreva um programa que leia dois números do
# usuário e usa a função para mostrar a multiplicação deles.


def multiplicacao(a, b):
    if 0 in [a, b]:
        return 0
    elif a == 1:
        return b
    elif b == 1:
        return a
    else:
        return a + multiplicacao(a, b - 1)


a = int(input("1o número: "))
b = int(input("2o número: "))

print(f"{a}*{b}={multiplicacao(a, b)}")
