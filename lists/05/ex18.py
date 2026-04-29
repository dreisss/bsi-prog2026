#!/usr/bin/env python

# O produto das matrizes Am×p e Bp×n é uma matriz Cm×n em que cada elemento cij
# é obtido por meio da soma dos produtos dos elementos  correspondentes da i-ésima
# linha de A pelos elementos da j-ésima coluna de B. Escreva um programa que: lê
# as dimensões m, n e p; cria as matrizes A e B com valores inteiros aleatórios
# no intervalo [0,3]; cria a matriz C=A×B; e mostra as três matrizes no final.

from random import randint

m_dim = int(input("Dimensão m: "))
n_dim = int(input("Dimensão n: "))
p_dim = int(input("Dimensão p: "))

A = [[randint(0, 3) for _ in range(p_dim)] for _ in range(m_dim)]
B = [[randint(0, 3) for _ in range(n_dim)] for _ in range(p_dim)]
C = [[0 for _ in range(n_dim)] for _ in range(m_dim)]

for i in range(m_dim):
    for j in range(n_dim):
        for k in range(p_dim):
            C[i][j] += A[i][k] * B[k][j]

print()
print("A:")
for row in A:
    print(" ".join([str(n) for n in row]))

print()
print("B:")
for row in B:
    print(" ".join([str(n) for n in row]))

print()
print("C:")
for row in C:
    print(" ".join([str(n) for n in row]))
