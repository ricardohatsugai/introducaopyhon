''' Projeto..: Exercício2
    Autor....: Ricardo Hatsugai
    Data.....: 31/12/2023
    Versão...: 1.0 '''

''' Finalidade: Ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus Celsius. '''

f = float(input("Informe a temperatura em graus Fahrenheit: "))

c = ((f - 32.0) * 50) / 90

print("A temperatura {:.2f} Fº em Cº é {:.2f}.".format(f, c))