# Escreva um programa que leia as coordenadas de um ponto (x,y) e o raio r de
# uma circunferência centrada na origem (0.0,0.0). O programa deve dizer se o
# ponto está: - dentro da circunferência; - sobre a circunferência; - fora da
# circunferência. O programa deve informar um erro caso r≤0. A fórmula da
# distância é d^2=(x2−x1)^2+(y2−y1)^2

from math import sqrt

radius = float(input("Raio: "))

if radius <= 0:
    print("Raio inválido!")
else:
    x = float(input("x: "))
    y = float(input("y: "))
    distance = sqrt(x**2 + y**2)

    if distance == radius:
        print("O ponto está sobre a circunferência")
    elif distance > radius:
        print("O ponto está fora da circunferência")
    elif distance < radius:
        print("O ponto está dentro da circunferência")
