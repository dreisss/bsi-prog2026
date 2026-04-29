#!/usr/bin/env python

# Faça um programa que cria duas listas de comprimento N=10 com valores reais
# aleatórios uniformemente distribuídos no intervalo [1,99]. Depois disso, criar
# uma terceira lista de comprimento \(N \times 2\) que é composta pelos elementos
# da primeira e da segunda lista alternados. Por exemplo, sendo a primeira lista
# [1,2,3] e a segunda lista [4,5,6], a terceira lista deve ser [1,4,2,5,3,6].
# No final o programa deve mostrar as três listas.

from random import uniform

list01 = [round(uniform(1, 99), 2) for _ in range(10)]
list02 = [round(uniform(1, 99), 2) for _ in range(10)]
list03 = []

for i in range(10):
    list03.append(list01[i])
    list03.append(list02[i])

print("[" + ", ".join([f"{i:.2f}" for i in list01]) + "]")
print("[" + ", ".join([f"{i:.2f}" for i in list02]) + "]")
print("[" + ", ".join([f"{i:.2f}" for i in list03]) + "]")
