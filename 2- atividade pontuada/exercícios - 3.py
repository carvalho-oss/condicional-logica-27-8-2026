import os
os.system ('cls')

# ENTRADA.

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * 2)

#   PROCESSAMENTO.

if imc <= 18.6:
    print('abaixo do peso ')

elif imc >=24.9:
    print('peso  ideal')

elif imc >= 25.0:
    print('Levemente acima do peso')

elif imc >= 29.9:
    print ('Levente acima do peso')

elif imc >= 30.0:
    print ('Obesidade grau I')

elif imc >= 34.9:
    print('Obesidade grau I')

elif imc >=  35.:
    print('Obesidade grau I')

elif imc  >= 39.9:
    print('Obesidade grau II')
