#!/usr/bin/env python

# Escreva um programa que exiba um menu das operações aritméticas, no qual o usuário escolhe uma operação e um número
# e o programa apresenta a tabuada desse número. Depois disso, o menu deve ser exibido novamente para queoutra opção
# possa ser escolhida. Esse processo se repete até o usuário escolher a opção sair.


option = 0

while option != 5:
    print(
        """********* MENU *********
* 1 - Soma             *
* 2 - Subtração        *
* 3 - Multiplicação    *
* 4 - Divisão          *
* 5 - Sair             *
************************"""
    )

    option = int(input("Opção: "))

    if option == 5:
        break
    else:
        n = int(input("Escolha o número: "))

        for i in range(1, 10):
            match option:
                case 1:
                    print(f"{n} + {i} = {n + i}")
                case 2:
                    print(f"{n} - {i} = {n - i}")
                case 3:
                    print(f"{n} * {i} = {n * i}")
                case 4:
                    print(f"{n} / {i} = {n / i:.2f}")

        print()
