maior = menor = 0
num = []
for c in range(5):
    num.append(int(input('Digite um valor: ')))
    if c == 0:
        menor = maior = num[c]
    if num[c] > maior:
        maior = num[c]
    if num[c] < menor:
        menor = num[c]

print(f'O maior numero é {maior} e se encontra na posição ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}... ', end='')
print(f'O menor número é {menor} e se encontra na posição ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}... ', end='')
