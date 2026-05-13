#!/usr/bin/env python

# Escreva uma função chamar extrair_numeros() que tem como parâmetro uma string
# e retorna uma lista de números inteiros que que aparecem como string no parâmetro.
# Depois disso escreva um programa que recebe uma frase do usuário e usa a função
# para extrair e mostrar os números que essa frase tem.


def extrair_numeros(text):
    numbers = []
    reading = False

    for c in text:
        if c.isdigit():
            if reading == False:
                numbers.append(c)
                reading = True

            elif reading == True:
                numbers[-1] += c

        else:
            reading = False

    return [int(n) for n in numbers]


text = input("Texto: ")
print(f"Números extraídos = {extrair_numeros(text)}")
