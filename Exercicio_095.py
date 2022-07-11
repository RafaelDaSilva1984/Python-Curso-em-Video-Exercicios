jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    total = int(input(f'O Jogador {jogador["Nome"]} fez quantos jogos: '))
    partidas.clear()
    for i in range(0,total):
        partidas.append(int(input(f'  - Na partida {i+1} o Jogador {jogador["Nome"]} fez quantos gols? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
   
    while True:
        resp = str(input('Quer continuar [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro!! S ou N')
    if resp in 'Nn':
        break
print('___'*18) 
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print('___'*18) 
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<16}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador - [999 finaliza busca]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro!!! Não existe jogador com código da pesquisa {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i+1} o jogador {jogador["Nome"]} fez {g} Gols...')
    print('_-_'*18)
print('ENCERRADO...')










