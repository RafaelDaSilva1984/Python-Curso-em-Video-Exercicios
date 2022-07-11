print('-'*40)
lista = (('Água', 1.75, 'Refrigerante', 9.15, 'Bife', 45.20, 'Batata', 5.53))
print(f'{"Listagem de Preços":^40}')
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-'*40)
