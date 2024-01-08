''' Projeto....: Exercício 7
    Autor......: Ricardo Hatsugai
    Data.......: 08/01/2024
    Versão.....: 1.0'''

# Função para identificar o maior e o menor valor entre cinco números.
def encontra_maior_menor(a, b, c, d, e):
    # Inicializa as variáveis de maior e menor com o primeiro valor
    maior = menor = a

    # comparação
    if (b > maior):
        maior = b
    elif (b < menor):
        menor = b
    
    if (c > maior):
        maior = c
    elif (c < menor):
        menor = c

    if (d > maior):
        maior = d
    elif (d < menor):
        menor = d
    
    if (e > maior):
        maior = e
    elif (e < menor):
        menor = e
    
    return maior, menor

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))
E = int(input("Digite o valor de E: "))

# Chama a função para encontrar o maior e o menor valor
maior, menor = encontra_maior_menor(A, B, C, D, E)

# Apresenta os resultados
print("O maior valor é: %i" % maior)
print("O menor valor é: %i" % menor)