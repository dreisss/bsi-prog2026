#!/usr/bin/env python

# Escreva um programa para ler uma quantidade indeterminada de números inteiros. Ao final de cada leitura, o programa deve
# perguntar ao usuário se outra leitura deve ser feita. Caso a resposta seja sim (s), o programa faz a próxima leitura.
# Caso a resposta seja não No, o programa termina exibindo: (i) a quantidade de números lidos; (ii) a quantidade de números
# positivos ou neutros; (iii) a quantidade de números negativos; (iv) a quantidade de números pares; (v) a quantidade de
# números ímpares; e (vi) a média dos números lidos.

quantity = positive_or_neutral = negative = even = odd = avg = 0

number = int(input("Digite o valor: "))
continue_ = input("Deseja ler outro valor (s/n)? ")

while continue_ != "n":
    quantity += 1

    if number >= 0:
        positive_or_neutral += 1
    else:
        negative += 1

    if number % 2 == 0:
        even += 1
    else:
        odd += 1

    avg = ((quantity - 1) * avg + number) / quantity

    number = int(input("Digite o valor: "))
    continue_ = input("Deseja ler outro valor (s/n)? ")

quantity += 1

if number >= 0:
    positive_or_neutral += 1
else:
    negative += 1

if number % 2 == 0:
    even += 1
else:
    odd += 1

avg = ((quantity - 1) * avg + number) / quantity

print(
    f"""Lidos: {quantity}
Positivos ou neutros: {positive_or_neutral}
Negativos: {negative}
Pares: {even}
Ímpares: {odd}
Média = {avg:.2f}"""
)
