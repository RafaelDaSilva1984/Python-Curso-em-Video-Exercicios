colocacao = ('Coritiba','Corinthians', 'Palmeiras','São Paulo', 'Flamengo','Atletico MG','Santos','Fluminense','Internacional',
'Botafogo','Athletico PR', 'Goias', 'Atletico GO', 'Fortaleza','Chapecoense', 'Avai', 'Juventude','Ceara', 'Grêmio', 'Cruzeiro')
print('*_*' * 13)
print('-__-' * 13)
print('Times Ordenados',sorted(colocacao))
print('*_*' * 19)
print('-__-' * 7)
print(f'Os 5 Primeiros colocados são:',colocacao[:5])
for pos, times in enumerate(colocacao[:5]):
        print(f'Colocação na Tabela:',pos+1,'º:', times)
print('*_*' * 16)
print('-__-' * 10)
print(f'Os 4 ùltimos colocados são:', colocacao[16:])
for pos, times in enumerate(colocacao[16:]):
        print(f'Colocação na Tabela:',pos+16,'º:', times)
print('*_*' * 10)
print('-__-' * 16)
print(f'A',colocacao[15-1],'esta na',colocacao.index('Chapecoense')+1,'ª Posição')
print('*_*' * 7)
print('-__-' * 19)      

    
