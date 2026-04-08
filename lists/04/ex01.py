#!/usr/bin/env python

# Escreva um programa para calcular a área e o perímetro de um quadrado, caso a medida de lado informada seja inválida,
# uma mensagem deve ser apresentada para o usuário e o valor lido novamente.

side = int(input("Digite o lado: "))

while side <= 0:
    print("Valor inválido!")
    side = int(input("Digite o lado: "))

print(f"Area = {side * side:.2f}")
print(f"Perímetro = {4 * side:.2f}")
