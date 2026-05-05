# Escreva um programa que leia três valores inteiros que correspondem aos ângulos de um triângulo.
# Uma mensagem de erro é apresentada caso esses ângulos não formem um triângulo (algum dos ângulos é não positivo ou a soma deles não é 180 graus).
# Classifique o triângulo como:
# - Retângulo: tem um ângulo reto e dois agudos;
# - Acutângulo: tem três ângulos agudos;
# - Obtusângulo: tem um ângulo obtuso e dois agudos.
# Lembrando que o ângulo agudo é aquele que mede menos de 90 graus, o reto possui exatamente 90 graus e o obtuso apresenta uma medida acima de 90 graus.
# A imagem abaixo mostra um exemplo de cada triângulo.

angle1 = int(input("1o ângulo: "))
angle2 = int(input("2o ângulo: "))
angle3 = int(input("3o ângulo: "))

if angle1 + angle2 + angle3 != 180 or 0 in [angle1, angle2, angle3]:
    print("Não formam um triângulo")
elif 90 in [angle1, angle2, angle3]:
    print("triângulo retângulo")
elif angle1 < 90 and angle2 < 90 and angle3 < 90:
    print("triângulo acutângulo")
elif angle1 > 90 or angle2 > 90 or angle3 > 90:
    print("triângulo obtusângulo")
