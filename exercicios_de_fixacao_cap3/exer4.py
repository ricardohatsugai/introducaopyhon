''' Projeto....: Exercício 4
    Autor......: Ricardo Hatsugai
    Data.......: 05/01/2024
    Versão.....: 1.0'''

a = int(input("Entre com um valor numérico inteiro: "))
b = int(input("Entre com outro valor numérico inteiro: "))
c = int(input("Entre com mais um valor numérico inteiro: "))

if (a > b > c):
    print("Os valores digitados na ordem crescente são A = %i, B = %i e C = %i" % (a,b,c))
elif(b > a > c):
    print("Os valores digitados na ordem crescente são B = %i, A = %i e C = %i" % (b,a,c))
elif(c > a > b):
    print("Os valores digitados na ordem crescente são C = %i, A = %i e B = %i" % (c,a,b))
elif(c > b > a):
    print("Os valores digitados na ordem crescente são C = %i, B = %i e A = %i" % (c,b,a))
elif(b > c > a):
    print("Os valores digitados na ordem crescente são B = %i, C = %i e A = %i" % (b,c,a))
elif(a > c > b):
    print("Os valores digitados na ordem crescente são A = %i, C = %i e B = %i" % (a,c,b))