nome = str(input("Informe seu nome...............: "))
nasc = int(input("Informe o ano de seu nascimento: "))
hoje = int(input("Informe o ano atual............: "))
idade = hoje - nasc
print("Olá % , você possui em torno de %d anos de idade" % (nome, idade))
enter = input("\nPressione <Enter> para encerrar...")