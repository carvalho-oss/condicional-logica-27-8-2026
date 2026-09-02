import os
os. system ('cls')

#ENTRADA.

nome = str(input('Digite seu nome: '))
primeira_nota = int(input('Digite primeira_nota:'))
segunda_nota = int(input('  Digite sua segunda_nota:'))

#PROCESSAMENTO.

media = (primeira_nota + segunda_nota) /2

# SAÍDA.

if media >= 9:
    print(f'  Sua foi A:{media}')
elif media >=7.5:
    print(f'sua foi nota B:{media}')
elif media >= 6:
    print(f'sua foi C:{media}')
elif media >= 4:
    print(f'sua nota foi D:{media}')
else:
    print(f'sua nota foi E:{media}')