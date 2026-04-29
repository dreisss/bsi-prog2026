#!/usr/bin/env python

# Elabore um programa que cria uma lista A de comprimento N=10 composta de números inteiros aleatórios no intervalo [0,N].
# Depois disso, crie uma lista B de todos os valores existentes na lista A sem repetir.
# Por exemplo, considerando que A=[1,3,1,2,4,2], a outra lista deve ser B=[1,3,2,4], pois todos estes elementos estão
# em A, mas não repetimos o 1 nem o 2. Note que os elementos de B seguem a mesma ordem que ocorrem em A.
# No final apresente as duas listas.

from random import randint

listA = [randint(0, 10) for _ in range(10)]
listB = []

for el in listA:
    if listB.count(el) == 0:
        listB.append(el)

print(listA)
print(listB)
