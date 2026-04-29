#!/usr/bin/env python

# Elabore um programa que cria duas listas A (comprimento N=10) e B (comprimento M=15)
# compostas de números inteiros aleatórios no intervalo [0,N].
# Depois disso, crie uma lista C de todos os valores que aparecem na lista A e na lista B,
# sendo que a lista C não deve ter valores repetidos.
# Por exemplo, considerando que A=[1,2,3,1,4,2,3] e B=[1,2,1,2,1,2,4], então C=[1,2,4].
# Note que os elementos de C seguem a mesma ordem em que eles ocorrem em A.
# No final apresente as três listas.

from random import randint

listA = [randint(0, 10) for _ in range(10)]
listB = [randint(0, 10) for _ in range(15)]
listC = []

for el in listA:
    if listB.count(el) >= 1 and listC.count(el) == 0:
        listC.append(el)

for el in listB:
    if listA.count(el) >= 1 and listC.count(el) == 0:
        listC.append(el)

print(listA)
print(listB)
print(listC)
