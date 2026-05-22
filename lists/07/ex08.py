#!/usr/bin/env python

# Implemente uma função recursiva chamada eh_palindromo() que returna True se
# uma dada string é um palíndromo e False caso contrário. Estabeleça que parâmetros
# essa função deve ter para funcionar recursivamente.

# Depois implemente um programa que leia uma string do usuário e diz se ela é
# palíndroma ou não usando a função.


def eh_palindromo(word):
    if len(word) in [0, 1]:
        return True
    else:
        return (word[0] == word[-1]) and eh_palindromo(word[1:-1])


word = input("Digite uma palavra: ")

if eh_palindromo(word):
    print(f'"{word}" é palíndromo')
else:
    print(f'"{word}" não é palíndromo')
