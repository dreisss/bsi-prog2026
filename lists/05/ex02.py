#!/usr/bin/env python

# Elabore um programa que leia 10 valores inteiros pelo teclado e os armazena em
# uma lista. Depois disso, mostre quantos elementos dessa lista estão abaixo e
# quanto elementos estão acima da média.

list = []
sum = n_above = n_bellow = 0

for i in range(10):
    number = int(input(f"digite o {i + 1}o valor: "))
    sum += number
    list.append(number)

avg = sum / len(list)

for el in list:
    if el > avg:
        n_above += 1
    elif el < avg:
        n_bellow += 1

print(f"Média = {avg:.2f}")
print(f"{n_bellow} elemento(s) abaixo da média")
print(f"{n_above} elemento(s) acima da média")
