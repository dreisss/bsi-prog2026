#!/usr/bin/env python

# Escreva uma função recursiva chamada busca() que procura pela primeira ocorrência
# de uma chave k em uma lista.

# Se a chave k está na lista, a função deve retornar o índice em que ela foi
# encontrada; caso contrário, deve retornar -1.

# A função deve ser implementada de forma recursiva, percorrendo a lista elemento
# por elemento. Estabeleça os parâmetros necessários para que a função funcione
# corretamente de forma recursiva.

# Depois escreva um programa que leia os dados da lista e o valor chave e faça a
# busca usando a função, indicando se a chave foi encontrada ou não.


def busca(list, key, count=0):
    if list == []:
        return -1
    elif key == list[0]:
        return count
    else:
        return busca(list[1:], key, count + 1)


list = input("Digite os números: ").split(" ")
key = input("Valor chave: ")

result = busca(list, key)

if result == -1:
    print(f"Chave {key} não encontrada")
else:
    print(f"Chave {key} encontrada na posição {busca(list, key)}")
