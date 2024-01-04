''' Projeto....: Exercício 7
    Autor......: Ricardo Hatsugai
    Data.......: 31/12/2023
    Versão.....: 1.0'''

''' Elaborar um programa que calcule e apresente o valor do resultado da área de uma 
    circunferência.'''

from math import pi


r = float(input("Informe o valor do raio de circunferência: "))
vol = pi * r ** 2

print("O valor da circunferência do raio é %3.2f;" % vol)