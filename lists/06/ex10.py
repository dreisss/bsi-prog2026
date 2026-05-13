#!/usr/bin/env python

# Escreva uma função chamada que recebe como parâmetro uma quantidade indeterminada
# de números reais e retorna a média aritmética, a variância populacional e o
# desvio padrão populacional. A média é x¯=∑ni=1xin, a variância é V=∑ni=1(xi−x¯)^2/n,
# e o desvio padrão é D^2=∑ni=1(xi−x¯)^2/n, no qual n é a quantidade de elementos
# do conjunto e xi é o i-ésimo elemento do conjunto. Depois escreva um programa
# que leia uma sequência de números reais em uma mesma linha e usa a função para
# mostrar o resultado da média, variância e desvio padrão desses dados.

from math import sqrt


def avg_std_dev(numbers):
    avg = sum(numbers) / len(numbers)
    std = sum([(i - avg) ** 2 for i in numbers]) / len(numbers)
    dev = sqrt(std)

    return avg, std, dev


numbers_input = input("Digite os números separados por espaços: ")

if numbers_input == " ":
    print("Nenhum valor informado")
else:
    numbers = [float(i) for i in numbers_input.split(" ")]
    avg, std, dev = avg_std_dev(numbers)

    print(f"Média = {avg:.2f}")
    print(f"Variância = {std:.2f}")
    print(f"Desvio padrão = {dev:.2f}")
