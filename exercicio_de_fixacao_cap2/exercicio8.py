''' Projeto....: Exercício 8
    Autor......: Ricardo Hatsugai
    Data.......: 31/12/2023
    Versão.....: 1.0
    Descrição..: Elaborar um programa que leia dois valores numéricos reais desconhecidos 
    maiores que zero, representados pelas variáveis A e B. Calcular e apresentar sem 
    nehuma formatação os resultados das quatro operações aritméticas básicas como 
    R1(soma), R2(Subtração), R3(multiplicação) e R4(divisão)'''

a = float(input("Informe um valor real positivo: "))
b = float(input("Informe outro valor real positivo: "))

# Soma
print("A soma do valor %.2f + %.2f = %.2f;" % (a,b,(a+b)))

# Subtração
print("A subtração do valor %.2f - %.2f = %.2f;" % (a,b,(a-b)))

# Multiplicação
print("A multiplicação do valor %.2f * %.2f = %.2f;" % (a,b,(a*b)))

# divisão
print("A divisão do valor %.2f / %.2f = %.2f;" % (a,b,(a/b)))

# resto
print("O resto do valor %.2f mod %.2f = %.2f;" % (a,b,(a%b)))