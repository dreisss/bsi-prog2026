#!/usr/bin/env python

# O Unicode (pesquise sobre) é um padrão criado para representar texto de forma consistente em qualquer idioma, sistema ou dispositivo.
# Esse define um sistema onde cada  caractere corresponde a um código numérico. Sendo assim, escreva um programa que leia dois números
# que representam o início e fim de um intervalo fechado e mostre os caracteres unicode que estão neste intervalo. Cada símbolo deve ser
# separado por uma tabulação e cada linha deve ter no máximo cinco símbolos. Garanta que o primeiro valor seja menor ou igual ao segundo
# valor para se ter um intervalo válido.

start = int(input("inicio: "))
finish = int(input("fim: "))

if finish < start:
    print("Intervalo inválido!")

else:
    print("_" * 41)
    print()

    for i in range(start, finish + 1, 5):
        print("|", end="")

        for j in range(i, i + 5):
            if j <= finish:
                print(f"{j}='{chr(j)}'", end="|")

        print()

    print("_" * 41)
