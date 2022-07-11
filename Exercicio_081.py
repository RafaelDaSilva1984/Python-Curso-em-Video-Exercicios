lista = list()
sel = 5

while True:  
    lista.append(int(input(f'Digite um valor {len(lista)}: ')))    
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
        if escolha not in 'SN':
            print('Para continuar digite ->[S/N]')            
    if escolha == 'N':
        break
for i, v in enumerate(lista):    
    if sel in list(lista):
            if v == 5:
                print(f'O número {sel} faz parte da lista e na posição {i} da lista.') 
    if sel not in list(lista):
        print(f'O número {sel} não foi encontrado na  lista.')
        break
lista.sort(reverse=True)
print(f'Lista = {lista}')
print(f'Foram adicionados {len(lista)} valores. ')

