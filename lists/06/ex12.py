#!/usr/bin/env python

# Escreva uma função chamada int2bin() que tem como parâmetro um inteiro não
# negativo e retorna uma lista de 0's e 1's que correspondem a esse número
# convertido em binário. Não utilize funções prontas do Python para essa conversão,
# use a lógica baseadas em divisões sucessivas.


def int2bin(number):
    if number == 0:
        return 0

    result = ""
    div = number

    while div != 1:
        result += str(div % 2)
        div = div // 2

    result += "1"
    return result[::-1]


number = int(input("Digite o número: "))
print(f"Em binário = {int2bin(number)}")
