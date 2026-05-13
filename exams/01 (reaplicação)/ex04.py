# Escreva um programa que lê um número inteiro não negativo n e imprime o
# seguinte padrão: na 1a linha imprime n−1 espaços em branco e um asterisco;
# na 2a linha imprime n−2 espaços em branco e dois asteriscos; ...; na última
# linha imprime zero espaços em branco e n asteriscos.

number = int(input("Número: "))

for i in range(number):
    print(f"{' '*(number - i - 1)}{'*'*(i + 1)}")
