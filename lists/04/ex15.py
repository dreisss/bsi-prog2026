#!/usr/bin/env python

# Escreva um programa que leia dígitos positivos pelo teclado e com eles crie um número inteiro formado por esses dígitos
# na mesma ordem em que foram lidos. Caso seja lido um número com mais de um dígito, este deve ser ignorado. Por exemplo,
# se forem lidos os dígitos 2, 3, 4 e 5, o programa deve gerar o inteiro 2345. Imprima esse número e depois o dobro desse
# número. A leitura dos dígitos termina quando for lido um número negativo.

i = 1
n = "1"
result = "0"

while int(n) > 0:
    n = input(f"{i}o dígito: ")

    if 0 < int(n) < 10:
        result += n

        i += 1

print(f"Número =  {int(result)}")
print(f"Dobro do número =  {int(result) * 2}")
