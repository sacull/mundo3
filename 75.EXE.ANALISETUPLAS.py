numero = (int(input('Digite um numero: ')),
          int(input('Digite um numero: ')),
          int(input('Digite um numero: ')),
          int(input('Digite um numero: ')))
print(f'O numero 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'o número 3 se encontra na posição {numero.index(3)} ')
print(f'Os numeros pares são ', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')