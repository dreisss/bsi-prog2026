#!/usr/bin/env python

# Na matemática, o fatorial de um número natural , representado por n!,
# é o produto de todos os inteiros positivos menores ou iguais a \(n\).
# Por exemplo, o fatorial de 5 é 120 (1×2×3×4×5). Escreva um programa para
# calcular o fatorial de um número qualquer informado pelo usuário. Lembrando
# que o fatorial de zero é um. Não vale utilizar o módulo math.

n = int(input("Digite um número: "))

if n == 0:
    print("0! = 1")
elif n < 0:
    print("Não é um número natural.")
else:
    result = 1

    for i in range(2, n + 1):
        result *= i

    print(f"{n}! = {result}")
