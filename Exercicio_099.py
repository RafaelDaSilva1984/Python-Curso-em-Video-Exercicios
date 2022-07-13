from time import sleep
    
def valor(*num):
    cont = maior = 0
    print('\nAnalisando os valores...')
    print('-='*len(num)*5)
    for vl in num:               
        print(f'{vl}', end=' ', flush=True)
        sleep(0.35)
        if cont == 0:
            maior = vl
        else:
            if vl > maior:
                maior = vl
        cont += 1
    print(f'Foram informados {cont} valores ao todo...')
    print(f'O Maior valor informado foi {maior}.')    
    print('-='*len(num)*5)
valor(2, 5 ,3 , 8, 1)
valor(4, 7)
valor(1 ,2)
valor(6)
valor()

