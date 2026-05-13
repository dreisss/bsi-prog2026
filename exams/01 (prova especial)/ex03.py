# Escreva um programa que leia dois números inteiros que correspondem ao início
# e o fim de um intervalo. Depois o programa calcula e mostra o somatório de
# todos os números desse intervalo (considere intervalo fechado).

start = int(input("Início: "))
finish = int(input("Fim: "))

sum = 0
for i in range(start, finish + 1):
    sum += i

print(f"Soma dos números no intervalo = {sum}")
