#!/usr/bin/env python

# Dado um intervalo 1<a<=b, escreva um programa que verifica se o intervalo é válido e procura e imprime todos os números primos no intervalo [a,b].

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))

if 1 < a <= b:
    print("Primos:", end="")

    for n in range(a, b):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print("", n, end="")

else:
    print("Intervalo inválido!")
