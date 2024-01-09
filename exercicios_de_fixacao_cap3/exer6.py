''' Projeto.....: Exercício 5
    Autor.......: Ricardo Hatsugai
    Data........: 08/01/2024
    Versão......: 1.0
    Descrição...: Efetuar a leitura de quatro valores numéricos inteiros representados pelas variáveis A, B, C e D. 
    Apresentar apenas os valores que sejam divisíveis por 2 e 3.'''

a = int(input("Informe o valor da variável A: "))
b = int(input("Informe o valor da variável B: "))
c = int(input("Informe o valor da variável C: "))
d = int(input("Informe o valor da variável D: "))


if (a % 2 == 0 or a % 3 == 0):
    print("O valor de A é divisível por 2 ou 3.")
if (b % 2 == 0 or b % 3 == 0):
    print("O valor de B é divisivel por 2 ou 3.")
if (c % 2 == 0 or c % 3 == 0):
    print("O valor de C é divisível por 2 ou 3.")
if (d % 2 == 0 or d % 3 == 0):
    print("O valor de D é divisível por 2 ou 3.")