''' Projeto..........: c02ex09.py
    Autor............: Ricardo Hatsugai
    Data.............: 27/12/2023
    Versão...........: 1.0
    Revisão..........: 27/12/2023 '''

''' 
    Finalidade

    Este programa tem por finalidade solicitar entrada de dados para o usuário.
 '''

nome = input("Entre seu nome: ")
idade = int(input("Entre sua idade: "))

print()

print("Olá, %s." % nome)
print("Você tem %i anos de idade." % idade)

print()

print("Olá, %s" % nome, end="")
print(" você tem %i anos de idade." % idade)