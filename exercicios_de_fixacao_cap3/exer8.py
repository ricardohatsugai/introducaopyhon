''' Projeto....: Exercício 8
    Autor......: Ricardo Hatsugai
    Data.......: 17/01/2024
    Versão.....: 1.0
    Descrição..: Fazer a leitura de um valor numérico inteiro qualquer e apresentá-lo 
    caso não seja maior que 3. Dica: para a solução deste problema utilize o operador 
    lógico de negação.'''

valor = int(input("Entre um valor numérico inteiro: "))

resp = ("O número %i é maior que 3" % valor) if not(valor <= 3) else ("O número %i é menor que 3" % valor)

print()
print(resp)

enter = input("\nPressione <Enter> para encerrar...")

