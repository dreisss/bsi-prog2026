#!/usr/bin/env python

# Faça um programa que cria uma lista A de comprimento N=10 composta de números inteiros aleatórios no intervalo [0,N].
# Depois disso, crie uma segunda lista B compostas apenas pelos elementos da lista A que não se repetem.
# Por exemplo, considerando que a lista A=[1,3,1,2,4,2], a outra lista deve ser B=[3,4], pois esses são os valores que aparecem apenas uma vez em A. Note que os elementos de B seguem a mesma ordem em que eles ocorrem em A.
# No final apresente as duas listas.

from random import randint

listA = [randint(0, 10) for _ in range(10)]
listB = listA.copy()

for el in listA:
    if listA.count(el) > 1:
        listB.remove(el)

print(listA)
print(listB)
