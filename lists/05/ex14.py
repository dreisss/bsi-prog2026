#!/usr/bin/env python

# Escreva um programa que conta a quantidade de palavras e a quantidade de vogais
# em uma dada frase. Considere que a frase pode ter espaços em branco repetidos
# antes ou depois de quaisquer palavras. Para reduzir o escopo, considere também
# que a frase só terá letras do alfabeto e espaços em branco (não terá pontuações,
# números, acentos e nem qualquer outro tipo símbolo).

phrase = input("Digite uma frase: ")

words = vowels = word_length = 0

for c in phrase + " ":
    if c in [" ", "\t"]:
        if word_length != 0:
            words += 1
            word_length = 0
    else:
        word_length += 1

    if c.lower() in ["a", "e", "i", "o", "u"]:
        vowels += 1

print(f"Quantidade de palavras = {words}")
print(f"Quantidade de vogais = {vowels}")
