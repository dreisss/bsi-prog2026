# Escreva um programa que leia dois inteiros positivos, largura e altura.
# O programa deve desenhar um "quadro" com essas dimensões utilizando o caractere # nas bordas e espaços em branco no centro.
# Caso uma dimensão lida seja menor que 2, o programa deve ler esse valor novamente.

height = width = 0

while height < 2:
    height = int(input("Altura: "))

while width < 2:
    width = int(input("Largura: "))

print("#" * width)
for i in range(height - 2):
    print("#" + " " * (width - 2) + "#")
print("#" * width)
