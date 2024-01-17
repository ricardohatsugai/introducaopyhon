''' Projeto.....: Exemplo 12
    Autor.......: Ricardo Hatsugai
    Versão......: 1.0'''

vlr1 = eval(input("Entre um valor numérico <A>: "))
vlr2 = eval(input("Entre um valor numérico <B>: "))

resp = (vlr1 > vlr2) and vlr1 or vlr2

print()
print("O maior valor informado : ", resp)

Enter = input("\nPressione <Enter> para encerrar...")