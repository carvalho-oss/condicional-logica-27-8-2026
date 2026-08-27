import os

# Limpa o terminal.
os. system('cls')

#ENTRADA.
print('= SOLICITANDO=')
primeiro_numero = float(input('Digite o primeiro número: '))
segundo_numero = float(input('Digite o segundo número:'))


# PROCESSAMENTO.
soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao =primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero

#SAÍDA.
print('\n = EXIBINDO DADOS' )
print('soma: ' , soma)
print('subtracao: ' , subtracao)
print('multiplicacao: ', multiplicacao)
print('Divisao: ' , divisao)


