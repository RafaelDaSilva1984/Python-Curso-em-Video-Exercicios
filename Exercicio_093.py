jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do Jogador: '))
total = int(input(f'O Jogador {jogador["Nome"]} fez quantos jogos: '))
for i in range(0,total):
    partidas.append(int(input(f'  - Na partida {i+1} o Jogador {jogador["Nome"]} fez quantos gols? ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'   ...O campo {k}, recebe o valor {v}... ')
print('-='*30)
print(f' ->   O Jogador {jogador["Nome"]} jogou {total} partidas.')
for i,v in enumerate(partidas):
    print(f'     ... - Na partida {i+1}, fez {v} GOLS')
print('-='*30)
print(f'   -> Foi total de {jogador["Total"]} bolas na rede do Jogador {jogador["Nome"]}...')
print('-=*=-'*13)
