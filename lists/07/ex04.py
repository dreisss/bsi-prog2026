#!/usr/bin/env python

# A potenciação de dois números inteiros não negativos pode ser entendida como
# uma multiplicação repetida. Por exemplo: 34=3×3×3×3=81. Pensando recursivamente,
# esse mesmo exemplo pode ser entendido como: 34=3×(33)=81. Por definição a0=1,
# para qualquer a≠0. Escreva uma função recursiva chamada potencia() que tem dois
# números inteiros não negativos como parâmetros (base e expoente) e retorna o
# resultado da potenciação entre esses dois números. Depois escreva um programa
# que leia dois números do usuário e usa a função para mostrar o resultado da
# potenciação.


def potencia(b, e):
    if e == 0:
        return 1
    elif b == 0:
        return 0
    else:
        return b * potencia(b, e - 1)


b = int(input("Base: "))
e = int(input("Expoente: "))

print(f"{b}^{e}={potencia(b, e)}")
