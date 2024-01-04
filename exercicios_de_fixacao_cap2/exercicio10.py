''' Projeto....: Exercício 10
    Autor......: Ricardo Hatsugai
    Data.......: 31/12/2023
    Versão.....: 1.0
    Descrição..: Construir um programa que leia um valor numérico inteiro N e 
    apresentar como resultado os seus valores sucessor e antecessor sem o uso de 
    atribuição a uma variável de saída.'''

N = int(input("Informe um número inteiro positivo: "))
print("O número antecessor de %i é %i, e seu sucessor é %i" % (N, (N-1), (N+1)))