#!/usr/bin/env python

# Escreva uma função que elimina os elementos repetidos de uma lista passada
# como parâmetro. Depois escreva um programa que receba os números de entrada
# todos em uma linha, usa a função para eliminar as repetições e apresenta o
# resultado.


def apaga_repetidos(numbers):
    new = []

    for i in numbers:
        if i not in new:
            new.append(i)

    return new


data = [int(i) for i in input("Dados: ").split(" ")]
print(f"Lista sem repetições = {apaga_repetidos(data)}")
