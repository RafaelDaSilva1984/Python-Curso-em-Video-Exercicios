primeiro = int(input('Digite o primeiro valor: '))
r = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end= ' ')
    termo += r
    cont += 1
print('FIM')
