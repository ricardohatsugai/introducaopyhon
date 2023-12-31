''' Projeto..: Exercício 6
    Autor....: Ricardo Hatsugai
    Data.....: 31/12/2023
    Versão...: 1.0'''

''' Elaborar um programa que leia o valor numérico correspondente ao salário atual de um trabalhador 
    e também faça a leitura do valor do percentual de reajuste a ser atribuído. Usar máscara de formatação 999iiii.99'''

sa = float(input("Informe seu salário bruto: "))
pr = float(input("Informe o percentual de reajuste PR: "))
pr = pr / 100

ns = sa + (sa * pr)

print("O novo salário atualizado é %7.2f." % ns)