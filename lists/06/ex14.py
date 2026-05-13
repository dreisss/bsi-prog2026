#!/usr/bin/env python

# Escreva três funções chamadas uniao(), intersecao() e diferenca(). Cada função
# tem como parâmetros duas listas A e B de números inteiros. A função uniao()
# retorna uma lista dos elementos que estão em A ou em B. A função intersecao()
# retorna uma lista com os elementos que estão tanto em A quanto em B. A função
# diferenca() retorna uma lista com os elementos que estão em A mas não em B.
# Em todos os casos, os elementos que estão na lista resultante devem seguir a
# ordem de ocorrência em A e depois em B, sem repetições de elementos. Depois
# disso escreva um programa que recebe os elementos de cada lista em sua respectiva
# linha e depois usa as funções para apresentar a união, a interseção e a diferença
# delas.


def uniao(list1, list2):
    new = []

    for i in list1:
        if i not in new:
            new.append(i)

    for i in list2:
        if i not in new:
            new.append(i)

    return new


def intersecao(list1, list2):
    new = []

    for i in list1:
        if i in list2 and i not in new:
            new.append(i)

    return new


def diferenca(list1, list2):
    new = []

    for i in list1:
        if i not in list2:
            new.append(i)

    return new


l1 = [int(i) for i in input("L1: ").split(" ")]
l2 = [int(i) for i in input("L2: ").split(" ")]

print(f"L1 U L2 = {uniao(l1, l2)}")
print(f"L1 ∩ L2 = {intersecao(l1, l2)}")
print(f"L1 - L2 = {diferenca(l1, l2)}")
