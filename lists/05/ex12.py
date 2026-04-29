#!/usr/bin/env python

# Elabore um programa para ler uma data no formato dia/mês/ano e depois mostre
# essa data no formato ano/mês/dia. A quantidade de dígitos nos elementos da
# data podem variar, por exemplo o mês pode ser dado como 02 ou apenas como 2, o
# ano pode ser dado como 2001, ou 01, ou apenas 1.

date_str = input("Digite a data (dd/mm/aaaa): ")
reversed = "/".join(reversed(date_str.split("/")))

print(reversed)
