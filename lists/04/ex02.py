#!/usr/bin/env python

# Escreva um programa para ler n valores informados pelo usuário
# e mostrar qual é o maior e o menor dos números lidos

quant = int(input("Digite a quantidade de números a serem lidos: "))
max = min = 0

for i in range(0, quant):
    ni = int(input(f"{i + 1}o valor: "))

    if i == 0:
        max = min = ni

    max = ni if ni > max else max
    min = ni if ni < min else min

print(f"Menor = {min}")
print(f"Maior = {max}")
