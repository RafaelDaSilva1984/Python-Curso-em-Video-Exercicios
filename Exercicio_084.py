galera = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0: # se não cadastrei ninguém  maior e o menor peso da galera na poisção [1] é 0...
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:]) # [:] cópia de dados
    dados.clear()
    resp = str(input('Quer continuar ? [S/N]-> '))
    if resp in 'Nn':
        break   
print(f'Ao todo Foram cadastradas na sua lista {len(galera)} pessoas...')
print(f'O maior peso foi {maior}kg de -> ', end= '')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}] ',end='')
for n,i in enumerate(galera):
    if i[1] == maior:
        print(f'[Posição {n}]',end=' ')
print()
print(f'O menor peso foi {menor}kg de -> ', end= '')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}]',end='')
for n,i in enumerate(galera):
    if i[1] == menor:
        print(f'[Posição {n}]',end=' ')
print()
