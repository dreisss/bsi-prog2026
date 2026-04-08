#!/usr/bin/env python

# Escreva um programa que leia um número inteiro positivo N
# e exiba na tela uma tabela N×N em que cada linha
# é composta pelos números de 1 a N.

n = int(input("Valor de N: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(j, end="\n" if j == n else "  ")
