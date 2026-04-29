#!/usr/bin/env python

# Elabore um programa que crie a lista a seguir usando o literal list: [20, 40, 50, 80, 90, 70, 60, 10, 30]. Depois disso, apresente essa lista no terminal nas seguintes formas:
# [20, 40, 50, 80, 90, 70, 60, 10, 30]
# 20->40->50->80->90->70->60->10->30
# [30->10->60->70->90->80->50->40->20]

list = [20, 40, 50, 80, 90, 70, 60, 10, 30]

print(list)

for i in range(9):
    print(list[i], end="->" if i != 8 else "")

print()

print("[", end="")

for i in range(9):
    print(list[8 - i], end="->" if i != 8 else "")

print("]")
