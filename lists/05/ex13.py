#!/usr/bin/env python

# Escreva um programa que leia uma palavra como entrada e depois diga se essa
# palavra é ou não palíndroma (palavras que podem ser lidas, indiferentemente,
# da esquerda para a direita ou vice-versa).

word = input("Digite a palavra: ")

if word == word[::-1]:
    print("É palíndroma")
else:
    print("Não é palindroma")
