#!/usr/bin/env python

# Escreva uma função chamada lista_seta() que recebe uma lista como parâmetro e
# retorna uma string que tem cada elemento da lista entre parênteses e separados
# po setas ->. Depois disso, escreva um programa que recebe todos os elementos
# de uma lista em uma única linha e depois passe essa lista para a função e
# imprima o seu retorno.


def lista_seta(num_list):
    return "->".join([f"({i})" for i in num_list])


numbers = input("Digite os elementos separados por espaço: ")
print(lista_seta(numbers.split(" ")))
