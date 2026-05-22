#!/usr/bin/env python

# O Máximo Divisor Comum (MDC) de dois números inteiros é o maior número que
# divide ambos sem deixar resto. Por exemplo: mdc(12,8)=4. Podemos calcular o
# MDC usando o algoritmo de Euclides, que se baseia na seguinte ideia:
# mdc(a,b)=mdc(b,a%b). Esse processo é repetido até que o resto da divisão seja
# zero. Quando isso acontece, o MDC é o valor de a. Pensando recursivamente,
# isso pode ser definido como: caso base mdc(a,0)=a; e caso recursivo
# mdc(a,b)=mdc(b,a%b),parab≠0. Sendo assim, escreva uma função recursiva chamada
# mdc() que recebe dois números inteiros como parâmetros e retorna o máximo
# divisor comum entre eles. Depois escreva um programa que lê dois números do
# usuário e usa a função para mostrar o MDC entre eles.


def mdc(n1, n2):
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    else:
        return mdc(n2, n1 % n2)


n1 = int(input("1o número: "))
n2 = int(input("2o número: "))

print(f"mdc({n1}, {n2}) = {mdc(n1, n2)}")
