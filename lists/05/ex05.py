#!/usr/bin/env python

# Escreva um programa que cria uma lista de comprimento N=10 contendo números reais aleatórios, uniformemente distribuídos
# no intervalo [10,100], representando os preços de compra de produtos.
# Em seguida, crie uma segunda lista de mesmo comprimento com os preços de venda desses produtos. Para isso, cada preço de
# venda deve ser calculado somando ao preço de compra uma fração aleatória do próprio preço, em que essa fração é um número real
# uniformemente distribuído no intervalo [0.05,0.50].
# Por fim, determine e mostre:
# - quantos produtos possuem lucro inferior a 10%;
# - quantos possuem lucro entre 10% e 20% (inclusive);
# - quantos possuem lucro superior a 20%.

from random import uniform

cost = [uniform(10, 100) for _ in range(10)]
sell = [el * (1 + uniform(0.05, 0.50)) for el in cost]

bellow_10 = between_10_20 = above_20 = 0

for i in range(10):
    percent_gain = (sell[i] - cost[i]) / cost[i]

    if percent_gain > 0.2:
        above_20 += 1

    elif percent_gain < 0.1:
        bellow_10 += 1

    elif 0.1 <= percent_gain <= 0.2:
        between_10_20 += 1


print("Preços de compra = [" + ", ".join([f"{i:.2f}" for i in cost]) + "]")
print("Preços de venda = [" + ", ".join([f"{i:.2f}" for i in sell]) + "]")
print(f"Lucro menor que 10% = {bellow_10}")
print(f"Lucro entre 10% e 20% = {between_10_20}")
print(f"Lucro acima de 20% = {above_20}")
