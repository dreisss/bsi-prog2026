#!/usr/bin/env python

# Escreva uma função chamada tabuada() que recebe um número inteiro como parâmetro
# e retorna uma string de 10 linhas que corresponde à tabuada de multiplicação
# desse número. Depois disso escreva um programa que usa essa função para imprimir
# a tabuada de um número dado pelo usuário.


def tabuada(number):
    result = f"{'*'*4} Tabuada de {number} {'*'*4}\n"

    for i in range(10):
        result += f"{number} * {i + 1} = {number * (i + 1)}\n"

    result += f"{'*'*22}\n"
    return result


number = int(input("Digite o número: "))
print(tabuada(number))
