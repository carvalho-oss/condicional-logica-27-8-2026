import os
os. system('cls')

idade = int(input('Digite sua idade:'  ))

if idade <16:
    print('não podem votar')
elif idade ==16:
    print('opcional')
elif idade <= 17:
    print('opcional')

elif idade <=65:
    print('obrigatório')
else:
    print('não é obrigatório')