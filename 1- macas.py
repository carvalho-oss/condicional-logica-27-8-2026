import os
os. system ('cls')

# ENTRADA.

print('\n cada maça custa R$ 1,30')

# PROCESSAMENTO.

macas = int(input( 'quantas maças deseja:   '))
maior = 1.30
menor = 1.00
total_1  = macas * menor
total_2 = macas  * maior

# SAÍDA.

if macas >= 12:
    print(f' o valor total é: 1,00: {total_1}')
else:
        print(f'o valor sera de R$1,30: {total_2}')

