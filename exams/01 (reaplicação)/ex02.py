# Um número inteiro positivo é chamado de perfeito quando a soma de seus divisores
# positivos (exceto ele mesmo) é igual ao próprio número. Por exemplo: 28 é um
# número perfeito, pois 1+2+4+7+14=28. Escreva um programa que leia um número
# inteiro positivo n e informe se ele é um número perfeito. Caso o valor lido
# para n não seja positivo, o programa deve ler o valor novamente até que ele
# seja positivo.

number = 0

while number <= 0:
    number = int(input("Número: "))

sum = 1
for i in range(2, number):
    if number % i == 0:
        sum += i

if sum == number:
    print(f"{number} é um número perfeito")
else:
    print(f"{number} não é um número perfeito")
