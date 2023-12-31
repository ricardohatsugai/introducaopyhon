''' Projeto....: Exercício 4
    Autor......: Ricardo Hatsugai
    Data.......: 31/12/2023
    Versão.....: 1.0'''

'''
    Ler dois valores numéricos inteiros representados pelas variáveis A e B, e 
    apresentar o resultado do quadrado da diferença do primeiro valor(variável A) 
    em relação ao segundo valor(variável B) calculado para a variável R.
'''

a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))

r = (a-b)**2

print("O quadrado da diferença de A em relação a B é %.2f" % r)