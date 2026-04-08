#!/usr/bin/env python

# Por volta do ano 1200 d.C, Leonardo de Pisa descreveu uma sequência de
# números conhecida como "Números de Fibonacci" para demonstrar o crescimento
# de uma população de coelhos. Os dois primeiros números da sequência são 1 e 1,
# os demais são resultados da soma dos dois números anteriores. Por exemplo, os
# 8 primeiros números da sequência de Fibonacci são: 1, 1, 2, 3, 5, 8, 13, 21.
# Escreva um programa que apresenta os n primeiros números da sequência de Fibonacci,
# sendo que o valor de n é informado pelo usuário.

n = int(input("Valor de n: "))

if n < 0:
    print("Quantidade inválida!")
else:
    current = previous1 = previous2 = 1

    for i in range(0, n):
        print(current, end="" if i == n - 1 else " ")

        if i >= 1:
            current = previous1 + previous2
            previous1 = previous2
            previous2 = current
