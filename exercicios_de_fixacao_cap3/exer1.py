''' Projeto....: Exercício 1 - Cap3
    Autor......: Ricardo Hatsugai
    Data.......: 04/01/2024
    Versão.....: 1.0'''

''' Efeturar a leitura de dois valores numéricos inteiros representados pelas 
variáveis A e B e apresentar o resultado da diferença do maior valor pelo menor 
valor computado sobre a variável R. Não se preocupe com a possibilidade de os 
valores informados serem iguais'''

a = int(input("Entre com um valor numérico inteiro: "))
b = int(input("Entre com outro valor numérico inteiro: "))

if (a >= b):
    r = a - b
    print("A diferença entre o maior valor e o menor é %d." % r)
else:
    r = b - a
    print("A diferença entre o maior valor e o menor é %d." % r)