''' Projeto...: Exercício2_cap2
    Autor.....: Ricardo Hatsugai
    Data......: 27/12/2023
    Versão....: 1.0
    Revisão...: 0
    Descrição: Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é 
    F=(9.0 * C + 160.0) / 5.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius. Dica: use a funcionalidade 
    eval() para a entrada da temperatura.
'''

c = eval(input("Informe a temperatura em Celsius Cº: "))
f = (9.0 * c + 16.0) / 5.0

print("A tempoeratura %.2f Celsius, " % c, end="")
print(" é em Fahrenheit %.2f. F" % f)