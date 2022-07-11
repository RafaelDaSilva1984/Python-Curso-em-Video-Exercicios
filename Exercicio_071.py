print('------------BANCO SILVA-------------')
valor = int(input('Você quer sacar qual valor R$: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced # valor - cédula
        totced += 1 # qtd de vezes  foi possivel diminuir 50 do total valor at´q que o valor seja maior que cédula maior
    else:
        if totced  > 0: # só escreve se o total de cedula maior que R$ 0,00
            print(f'Total de {totced} de cédulas de R$ {ced:.2f}')
        if ced == 50: # troca cedula de valor maior para de menor diminui para a menor
            ced = 20
            totced += 1 
        elif ced == 20:
            ced = 10
            totced += 1 
        elif ced == 10:
            ced = 5
            totced += 1 
        elif ced == 5:
            ced = 2
            totced += 1 
        elif ced == 2:
            ced = 1
            totced += 1 
        totced = 0 # faz o total de cédulas de cada valor volte ao valor 0
        if total == 0:
            break
print('Volte sempre ao BANCO SILVA')


