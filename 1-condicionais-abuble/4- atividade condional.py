import os
os. system('cls')

primeiro_numero = int(input('Digite seu número:  '))
segundo_numero = int(input('Digite seu número:  '))
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

print(f'primeiro:{primeiro_numero}')
print(f'segundo;{segundo_numero}')
print(f'seu maior numero:{maior}')
print(f'seu menor numero:{menor}')