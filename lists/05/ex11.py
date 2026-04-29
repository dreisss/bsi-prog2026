#!/usr/bin/env python

# Escreva um programa que fica lendo números inteiros não-negativos pelo teclado,
# essa leitura só termina quando um número negativo é lido. À medida que os números
# são lidos, eles são  inseridos em uma lista em ordem crescente. A lista deve ser
# impressa após a inserção de cada novo número na lista. Não vale usar os métodos
# de ordenação do Python.

number = 1
list = []

while number >= 0:
    number = int(input("Digite o valor: "))

    if len(list) == 0:
        list.append(number)

    if number > list[-1]:
        list.append(number)
    else:
        for i in range(len(list)):
            if number < list[i]:
                list.insert(i, number)
                break

    if number >= 0:
        print("[" + " <= ".join([str(i) for i in list]) + "]")
