''' Projeto.....: Exercício 9
    Autor.......: Ricardo Hatsugai
    Data........: 31/12/2023
    Versão......: 1.0
    Descrição...: Elaborar um programa que leia dois valores numéricos inteiros, 
    os quais devem representar respectivamente a base e o expoente de uma potência, 
    calcule a potência na variável R e apresente o resultado obtido.'''

a = int(input("Informe um número inteiro: "))
b = int(input("Informe outro número inteiro: "))
r = a ** b

print("A potência da base A com o expoente B, é %.2f" % r)