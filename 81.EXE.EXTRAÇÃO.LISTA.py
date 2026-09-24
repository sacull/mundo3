lista = list()
while True:
    n = int(input(f'Digite um valor: '))
    lista.append(n)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[:1]
    if resp == 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores digitados em ordem decrescente foram {lista}')
if 5 in lista:
    for i in range(len(lista)):
        if i == 5:
            pos = lista[i]
            print(f'O valor 5 apareceu na lista na posição {i}')
else:
    print('O valor 5 não apareceu na lista')