#!/usr/bin/env python

# Escreva um programa para mostrar na tela a tabuada de multiplicação dos números de um dado intervalo de n a m, sendo 1<=n<=m<=9.
# Use dois comandos de repetição aninhados: um para percorrer os valores a serem multiplicados (números de 1 a 9); e outro para
# percorrer o intervalo [n,m]. Garanta que o intervalo lido esteja correto e que cada coluna está separada por uma tabulação.

n = int(input("n: "))
m = int(input("m: "))

if 1 <= n <= m <= 9:
    for i in range(1, 10):
        for j in range(n, m + 1):
            print(f"{j} * {i} = {i * j}", end="\t")

        print()
else:
    print("Intervalo inválido!")
