from random import randint 
     # importa a a biblioteca de sortear numeros
from time import sleep  
        # importa timer de impressão na tela

def sorteia(lista): # define a função sorteia uma lista
    print('Foram Sorteados 5 valores...',  end='')
    for valor in range(0,5): # range de quantos números terá na lista
        vl = randint(1, 10) # sorteio de valores de 1 ,10 
        lista.append(vl) # adiciona os valores sorteados na lista do sorteia
        print(f'{vl}',end=' ', flush=True)
        sleep(0.3)
    print('--- FIM >>>')

def somaPar(lista): # define a função soma de numeros Pares
    soma = 0 # primeiro valores de par
    for valor in lista: # seleciona o valor dentro da lista      
        if valor % 2 == 0: # divide o valor e compara se divisão tem resto zero
            soma += valor # soma valor diviseis por 2 com resto zero
    print(f'Seus valores são {lista} somando os Pares temos: {soma}')
    print('Acabou..')


numeros = list() # cria lista numeros
sorteia(numeros) # cria a função sorteia os numeros
somaPar(numeros) # cria a função de somar de núemros pares



