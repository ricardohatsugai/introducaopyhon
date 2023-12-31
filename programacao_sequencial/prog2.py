nome = str(input("Informe seu nome..............: "))
nasc = int(input("Informe o ano de seu nascimento:"))
hoje = int(input("Informe o ano autal...........: "))
idade = hoje - nasc
print("Olá, %s" % nome)
print("você possui em torno de %d anos de idade" % idade)
enter = input("\nPressione <Enter> para encerrar...")