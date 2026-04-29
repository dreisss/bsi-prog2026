#!/usr/bin/env python

# Na matemática uma matriz de permutação é uma matriz An×n em que cada linha e
# cada coluna possui um único valor 1.0 e n−1 valores 0.0. Escreva um programa
# que leia a dimensão de uma matriz quadrada e depois leia cada um de seus
# elementos e no final diz se essa matriz é uma matriz de permutação ou não.

dimension = int(input("Dimensão da matriz quadrada: "))
matrix: list[list[float]] = []

for i in range(dimension):
    row = [float(n) for n in input().split(" ")]
    matrix.append(row)

is_permutation = True

for row in matrix:
    if row.count(1.0) != 1 or row.count(0) != dimension - 1:
        is_permutation = False
        break

for column_i in range(dimension):
    column = [row[column_i] for row in matrix]

    if column.count(1.0) != 1 or column.count(0) != dimension - 1:
        is_permutation = False
        break

if is_permutation:
    print("Matriz de permutação")
else:
    print("Essa matriz não é de permutação")
