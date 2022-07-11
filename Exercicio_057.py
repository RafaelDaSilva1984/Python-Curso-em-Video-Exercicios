cf = 0
cm = 0
s = ('F' , 'M')
while s != 'F' and s != 'M':    
    s = str(input('Digite seu Sexo [M/F]: ')).strip().upper() [0]
    if s != 'F' and s != 'M':
        print('Digite novamente, valor fora do esperado correto [F/M] ')
    elif s in 'f/F' :
        cf += 1
        print('Valor aceito, sexo Feminino, total de Mulheres',cf)
         
    elif s in 'm/M' :
        cm +=  1 
        print('Valor aceito, sexo Masculino, total de Homens',cm)