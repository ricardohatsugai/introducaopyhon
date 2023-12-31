''' Projeto...........: c02ex08
    Autor.............: Ricardo Hatsugai
    Data..............: 03/12/2023
    Versão............: 1.0
    Revisão...........: 03/12/2023
'''

"""
    Finalidade

    Este programa tem por finalidade apresentar alguns resultados Obtidos a partir do uso
      do módulo de biblioteca matemática interna da linguagem Python
"""

import math # Chamada do módulo de recursos matemáticos

print("2 ^ 3 .............: %10.2f" % math.pow(2, 3))
print("sqrt 25............: %10.2f" % math.sqrt(25))
print("floor 2.10.........: %10.2f" % math.floor(2.10))
print("celling 2.10.......: %10.2f" % math.ceil(2.10))
print("e ^2 ..............: %10.2f" % math.exp(2))
print("log2(2) ...........: %10.2f" % math.log2(2))
print("log10(2) ..........: %10.2f" % math.log10(2))
print("factorial(5) ......: %10.2f" % math.factorial(5))

enter = input("\nPressione <Enter> para encerrar... ")