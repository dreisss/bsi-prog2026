#!/usr/bin/env python

# Na disciplina de Programação, o professor dividiu a turma em 10 equipes para
# fazer um trabalho. Cada equipe deve ficar com um tema diferente, então o professor
# elaborou 10 temas de trabalho distintos e atribuiu uma para cada equipe. Entretanto,
# os alunos acharam que essa atribuição não foi justa, uma vez que alguns temas são
# bem mais difíceis do que outros. Então o professor resolveu fazer um sorteio.
# Ajude o professor criando um programa que atribui aleatoriamente um tema para
# cada equipe.

from random import randint

themes = list(range(0, 10))

for i in range(0, 10):
    index = 9 - i

    drawed = randint(0, index)
    print(f"Equipe {i + 1} fica com o Tema {themes[drawed] + 1}")
    themes[drawed] = themes[index]
