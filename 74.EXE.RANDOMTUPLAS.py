from random import randint
numero = (randint(1,10), randint(1,10), randint(1,10),
          randint(1,10), randint(1,10))
print('Os valores sorteados foram: ', end='')
for n in numero:
    print(n, end=' ')
print(f'O maior valor sorteado foi {max(numero)} e se encontra na posição {(numero.index(max(numero)))}', end=' ')
print(f'o menor valor sorteado foi {min(numero)} e se encontra na posição {(numero.index(min(numero)))}', end='')
