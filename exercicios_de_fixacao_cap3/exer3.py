''' Projeto...: Exercício 3
    Autor.....: Ricardo Hatsugai
    Data......: 04/01/2024
    Versão....: 1.0'''

n1 = float(input("Digite a nota N1: "))
n2 = float(input("Digite a nota N2: "))
n3 = float(input("Digite a nota N3: "))
n4 = float(input("Digite a nota N4: "))
md1 = (n1+n2+n3+n4)/4

if (md1 >= 7.0):
    print("Aprovado com média %2.2f." % md1)

if (md1 < 7.0):
    ne = float(input("Média não alcançada, favor entrar com a nota N5: "))
    md2 = (md1+ne)/2
    if(md2 >= 5.0):
        print("Aprovado em exame com média %2.2f." % md2)
    else:
        print("Reprovado com média %2.2f." % md2)
