#!/usr/bin/env python

# Na matemática uma matriz identidade é uma matriz diagonal An×n cujos elementos
# da diagonal principal são todos iguais a 1 e os outros elementos são iguais a 0.
# Escreva um programa que leia a dimensão de uma matriz quadrada e depois leia cada
# um de seus elementos e no final diz se essa matriz é uma matriz identidade ou não.

dimension = int(input("Dimensão da matriz quadrada: "))
matrix = []

for i in range(dimension):
    row = input().split(" ")
    matrix.append(row)

for i in range(dimension):
    is_identity = True

    for j in range(dimension):
        if (i == j and matrix[i][j] != "1") or (i != j and matrix[i][j] != "0"):
            is_identity = False
            break

    if not is_identity:
        print("Essa matriz não é uma matriz identidade")
        break
else:
    print("Matriz identidade")
