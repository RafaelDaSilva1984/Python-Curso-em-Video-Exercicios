c18 = cm18 = cm = cf = ctot = 0
print('-----Cadastros Pessoais-----')
while True:
    idade = int(input('Qual sua idade? '))
    if idade >= 18:
        c18 += 1       
    if idade < 18:
        cm18 += 1         
    sexo = ' '
    while sexo not in 'MF':        
        sexo = str(input('Qual seu sexo?[M/F]: ')).strip().upper()[0]
        if sexo not in 'MF':
            print('Para continuar digite ->[M/F]')
        if sexo in 'Mm':
            cm += 1            
        if sexo in 'Ff'and idade < 20:
            cf += 1
        if sexo in 'MF':
           ctot += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
        if escolha not in 'SN':
            print('Para continuar digite ->[S/N]')
    if escolha == 'N':
        break

print(f'Pessoas do Sexo masculino cadastrados são:{cm}')
print(f'Mulheres menores de 20 anos cadastradas são:{cf}')
print(f'Pessoas maiores de 18 anos cadastradas são:{c18}')
print(f'Pessoas menores de 18 anos cadastradas são:{cm18}')
print(f'Total de pessoas cadastradas igual a:{ctot}')
print('----------Acabou----------')


        

