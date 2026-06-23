# Escreva uma função chamada soma_positivos() que recebe como parâmetro uma
# lista de números inteiros e retorna um inteiro que corresponde ao somatório
# de todos os números positivos da lista.

# Depois escreva um programa que leia a quantidade de números a serem lidos,
# depois leia cada um desses números, guardando-os em uma lista. Por fim,
# apresente o somatório de todos os positivos lidos através da função.

# OBS: Não é permitido usar a função sum() nem colocar input() e/ou print()
# dentro da função.


def soma_positivos(numbers):
    sum = 0

    for n in numbers:
        if n > 0:
            sum += n

    return sum


quantity = int(input("Digite a quantidade: "))
numbers = []

for i in range(quantity):
    n = int(input(f"Digite o número ({i + 1}/{quantity}): "))
    numbers.append(n)

print(f"Soma dos positivos = {soma_positivos(numbers)}")
