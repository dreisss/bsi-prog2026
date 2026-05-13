#!/usr/bin/env python

# Escreva uma função chamada menor() que recebe uma quantidade indeterminada de
# números como parâmetros e retorna o menor deles. Em seguida escreva um programa
# que usa essa função, sendo que os números devem ser lidos pelo teclado e passados
# para a função.


def menor(nums):
    nums.sort()
    return nums[0]


nums = int(input("Digite a quantidade de números: "))
numbers = [int(input(f"Digite o número {i+1}/{nums}: ")) for i in range(nums)]

print(f"Menor = {menor(numbers)}")
