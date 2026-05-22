#!/usr/bin/env python

# Implemente uma função recursiva chamada inverte() que inverte os elementos de
# uma lista in-place (modificada diretamente na lista, sem listas extras).
# Estabeleça que parâmetros essa função deve ter para funcionar recursivamente.

# Depois implemente um programa que leia os valores da lista do usuário e os
# inverte usando a função.


def inverte(list, i=0) -> list[str]:
    length = len(list)

    if i >= length // 2:
        return list
    else:
        list[i], list[length - 1 - i] = list[length - 1 - i], list[i]
        return inverte(list, i + 1)


list = input("Digite os elementos: ").split(" ")
print(f"Lista invertida = {" ".join(inverte(list))}")


# SOLUÇÃO 2 (não aceita)
# def inverte(list):
#     if len(list) in [0, 1]:
#         return list
#     else:
#         return list[-1] + inverte(list[:-1])


# list = input("Digite os elementos: ")
# print(f"Lista invertida = {inverte(list)}")
