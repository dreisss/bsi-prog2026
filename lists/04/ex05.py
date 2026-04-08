#!/usr/bin/env python

# Escreva um programa para calcular be, onde b e e são números inteiros
# não negativos informados pelo usuário. Se o usuário informar algum
# valor negativo, esse deverá ser lido novamente. Lembre-se que:
# zero elevado a qualquer potência resulta em zero; e qualquer
# número elevado a zero resulta em um. Não vale usar a função math.pow() nem o operador ∗∗.

base = int(input("Base: "))
while base < 0:
    base = int(input("Base: "))


expoent = int(input("Expoente: "))
while expoent < 0:
    expoent = int(input("Expoente: "))


if expoent == 0:
    result = 1
else:
    result = base

    for i in range(1, expoent):
        result = result * base

print(f"{base}^{expoent} = {result}")
