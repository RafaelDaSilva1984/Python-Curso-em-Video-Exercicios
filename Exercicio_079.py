#Exercicio 079

num = list()
cont = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor not in num :
        num.append(valor)
        print('Valor adicionado com Sucesso...')
    else:
        print('Valor Duplicado não vou adicionar...')      
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
        if escolha not in 'SN':
            print('Para continuar digite ->[S/N]')
    if escolha == 'N':
        break  
print('Lista Finalizada sem valores Duplicados...!...!')
num.sort()
print(f'Você digitou os valores: {num}')



