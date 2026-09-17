time = ('Flamengo', 'Palmeiras', 'Athletico-PR',
        'Bahia', 'Fluminense', 'Cruzeiro', 'Atlético-MG',
        'Coritiba', 'Red Bull Bragantino', 'Santos', 'São Paulo',
        'Vitória', 'Corinthians', 'Botafogo', 'Mirassol', 'Grêmio',
        'Vasco', 'Internacional', 'Remo', 'Chapecoense')
print(f'Os cinco primeiros colocados a série A 2026 são \n{time[0:6]}\n')
print(f'Os últimos 4 colocados são {time[-1:-5:-1]}\n')
print(f'Os times em ordem alfabetica {sorted(time)}')
print(f'O ultimo colocado é {time[-1]}')