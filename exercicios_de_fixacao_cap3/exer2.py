''' Projeto....: Exercício 2
    Autor......: Ricardo Hatsugai
    Data.......: 04/01/2024
    Versão.....: 1.0
    Descrição..: Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno 
    representadas pels variáveis N1, N2, N3 e N4. Calcular a média aritmética (variável MD) 
    desse aluno e apresentar a mensagem "Aprovado" se a média obtida for maior ou igual a 5.0; 
    caso contrário, apresentar a mensagem "Reprovado". Mostrar após a apresentação das mensagens 
    o valor da média obtida pelo aluno ao lado da mensagem, utilizando a máscara 99.99.'''

n1 = float(input("Entre com a nota N1: "))
n2 = float(input("Entre com a nota N2: "))
n3 = float(input("Entre com a nota N3: "))
n4 = float(input("Entre com a nota N4: "))

media = (n1+n2+n3+n4)/4

if(media >= 5.0):
    print("Aprovado com a nota %2.2f." % media)
else:
    print("Reprovado com a nota %2.2f." % media)