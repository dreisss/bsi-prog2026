#!/usr/bin/env python

# Um número primo é um inteiro positivo maior que 1 que possui exatamente dois divisores: 1 e ele mesmo. Por
# exemplo: 2, 3, 5, 7, 11, 13 e 17. Escreva um programa que diga se um número dado pelo usuário é primo ou não.

n = int(input("Digite um número: "))

if n == 1:
    print("Não é primo")
else:
    for i in range(2, abs(n)):
        if n % i == 0:
            print("Não é primo")
            break

    else:
        print("É primo")
