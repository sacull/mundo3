import time

numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
          'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'quatorze', 'quinze', 'dezesseis',
          'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    resp = int(input('Digite um numero entre 0 e 20: '))
    if resp < 0 or resp > 20:
        print('Valor invalido')
        continue
    print('-'*30)
    print(numero[resp])
    for i in range (0,3,1):
        time.sleep(1)
        print('.', end='')


    pare = ' '
    pare = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if pare in 'Nn':
        break
