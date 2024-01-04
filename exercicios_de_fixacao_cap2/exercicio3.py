''' Projeto....: Exercício3
    Autor......: Ricardo Hatsugai
    Data.......: 31/12/2023
    Versão.....: 1.0 '''

''' Ler dois valores inteiros para as variáveis A e B, e efetuar a troca dos valores de forma que a variálvel A passe
a possuir o valor da variável B, e a variável B passe a possuir o valor da variável A. '''

a = int(input("Informe um número inteiro para variável A: "))
b = int(input("Informe outro número inteiro para a variável B: "))

print(f"Os valores que você informou para a variável A é %i, e B é %i" % (a, b))
print("\n")

aux = b
b = a
a = aux

print(f"Agora com os valores invertidos, a variável A é %i, e a variável B é %i" % (a,b))