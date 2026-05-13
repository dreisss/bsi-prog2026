#!/usr/bin/env python

# Escreva uma função chamada busca() que tem como parâmetros uma lista de elementos
# inteiros e um k (que representa o valor chave que está sendo pesquisado) e retorna
# o índice da primeira ocorrência do elemento k na lista. Caso k não esteja na lista,
# a função retorna -1. Depois disso escreva um programa que leia vários valores
# inteiros em uma mesma linha e o valor k a ser buscado e no final mostra em que
# posição da lista k se encontra.


def busca(numbers, k):
    for i, el in enumerate(numbers):
        if k == int(el):
            return i

    return -1


data = input("Dados: ").split(" ")
k = int(input("Chave de busca (k): "))

result = busca(data, k)

if result == -1:
    print(f"Chave {k} não encontrada")
else:
    print(f"Chave {k} encontrada no índice {result}")
