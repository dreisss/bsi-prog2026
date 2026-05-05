# Escreva um programa que lê como entrada um inteiro n≥0 e mostra como resultado um float

n = int(input("n: "))

if n < 0:
    print("n deve ser não negativo")
else:
    sum = n

    for i in range(1, n + 1):
        sum += 1 / i

    print(f"s = {sum:.2f}")
