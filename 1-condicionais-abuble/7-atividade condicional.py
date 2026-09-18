import os
os .system('cls')

primeiro_numero = float(input('digite sua nota:'))
segundo_nummero = float(input('digite sua nota:'))
terceira_numero = float(input('digite sua nota:'))

#PROCESSAMENTO.

media = (primeiro_numero + segundo_nummero + terceira_numero) / 3

if media >= 7:
    
    print('sua media é:' , media)

    resultado = ('APROVADO')
else:
    
    resultado = ('REPROVADO')

# SAÍDA.
print(f'Média:{media}')
print(f'Resultado:{resultado}')
print('FIM DO PROGRAMA')