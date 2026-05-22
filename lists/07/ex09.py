#!/usr/bin/env python

# Implemente uma função recursiva chamada conta_caractere() que retorna quantas
# vezes um determinado caractere aparece em uma string. Defina que parâmetros
# essa função deve ter para funcionar recursivamente.

# Depois implemente um programa que leia uma string e um caractere para mostrar
# quantas vezes esse caractere aparece na string usando essa função.


def conta_caractere(word, char):
    if len(word) == 0:
        return 0
    elif word[0] == char:
        return 1 + conta_caractere(word[1:], char)
    else:
        return conta_caractere(word[1:], char)


word = input("Palavra: ")
char = input("Caractere: ")

print(
    f'O caractere "{char}" aparece {conta_caractere(word, char)} vez(es) na palavra "{word}"'
)
