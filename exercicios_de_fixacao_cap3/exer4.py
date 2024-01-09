''' Projeto....: Exercício 4
    Autor......: Ricardo Hatsugai
    Data.......: 05/01/2024
    Versão.....: 1.0'''

a = int(input("Entre com um valor numérico inteiro: "))
b = int(input("Entre com outro valor numérico inteiro: "))
c = int(input("Entre com mais um valor numérico inteiro: "))

# Função Aplicando a propriedade distribuitiva
def ordenacao(a, b, c):
    if(a > b):
        a, b = b, a
    if(a > c):
        a, c = c, a
    if(b > c):
        b, c = c, b
    
    return a, b, c


# Saída dos valores em ordem crescente
print("Os valores digitados na ordem crescente são: %i, %i e %i." % ordenacao(a,b,c))