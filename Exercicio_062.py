
primeiro = int(input('Digite o primeiro valor: '))
r = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 3
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end= ' ')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos vc quer a mais ? '))
print('Foram mostrados um total de {} termos...'.format(total))




        
       
    

        
    
    
    

    
    
