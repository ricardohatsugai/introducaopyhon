''' Projeto....: Exercício 5
    Autor......: Ricardo Hatsugai
    Data.......: 31/12/2023
    Versão.....: 1.0'''

''' Construir um programa que leia três valores numéricos inteiros(A,B,C) 
    e apresentar como resultado o valor da soma dos quadrados dos valores lidos'''

from math import sqrt

a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))
c = int(input("Digite outro número inteiro: "))

a = sqrt(a)
b = sqrt(b)
c = sqrt(c)

d = a+b+c

print("A soma dos números A, B e C elevados ao quadrado é %i" % d)