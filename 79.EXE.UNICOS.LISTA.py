num = []
resp = ''
while True:
    v = int(input('Digite um valor: '))
    if v in num:
        print(f'O número {v} Já exite na lista\n'
              f'Favor digitar outro número não repetido.\n')
    if v not in num:
        num.append(v)
        print(f'Valor {v} adicionado com sucesso!')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[:1]
    if resp == 'N':
        break
num.sort(reverse=False)
print(f'Lista atual: {num} ')