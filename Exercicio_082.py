lista = list()
listaimpar = list()
listapar = list()
c = 0
ci = 0
cp = 0
while True:
    c += 1
    valor = int(input('Digite um valor: '))
    if valor not in lista :
        lista.append(valor)
        if valor % 2 == 0:
            listapar.append(valor)  
            cp += 1          
        if valor % 2 == 1:
            listaimpar.append(valor)  
            ci += 1      
    resp = str(input('Quer continuar [S/N]: '))
    if resp in 'Nn':
        break
lista.sort()
print(f'Sua lista possui {c} valores: {lista}')
listaimpar.sort()
print(f'São {ci} valores IMPAR da lista sendo eles: {listaimpar}')
listapar.sort()
print(f'São {cp} valores PAR da lista sendo eles: {listapar}')
