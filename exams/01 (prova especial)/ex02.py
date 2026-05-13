# Escreva um programa que leia dois números floats e mostra o resultado da divisão
# do primeiro número pelo segundo.
# Caso o segundo número seja zero, o programa deve informar que não pode fazer a
# divisão.

n1 = float(input("1o número: "))
n2 = float(input("2o número: "))

if n2 == 0:
    print("Não é possível dividir por zero")
else:
    print(f"{n1:.2f}/{n2:.2f}={n1/n2:.2f}")
