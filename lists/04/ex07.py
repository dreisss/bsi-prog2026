#!/usr/bin/env python

# Na teoria dos números, um quadrado perfeito é um número inteiro
# não negativo que pode ser expresso como o quadrado de outro número inteiro.
# Por exemplo, 0, 1, 4 e 9 são números inteiros resultantes de outros números
# elevados ao quadrado, nesse caso os números 0, 1, 2 e 3, respectivamente.
# Escreva um programa para verificar se um número informado é ou não um quadrado
# perfeito. A solução mais adequada para este problema usa raiz quadrada, mas
# aqui estamos exercitando repetições, então como você conseguiria determinar
# isso usando repetição.


n = int(input("Digite um número: "))

if n < 0:
    print("O número deve ser não negativo!")
else:
    for i in range(1, n):
        if i * i == n:
            print("Quadrado perfeito")
            break
    else:
        print("Não é quadrado perfeito")
