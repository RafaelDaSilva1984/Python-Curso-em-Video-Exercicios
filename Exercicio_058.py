from random import randint
comp = randint ( 0, 10)
v = False
ct = 0
while v != comp:
    v = int(input('Digite uma valor entre 0 e 10: '))    
    if v == comp:
        print('Fim do JOGO, Parabéns')
    elif v < comp:
        print('Tente Valor maior, Tente mais uma vez')
    elif v > comp:
        print('Tente Valor menor, Tente mais uma vez')
    else:        
        print('Digite novamente')
    ct += 1    
print('Você usou um total de tentativas igual a:',ct,'Para finalizar o Jogo')
