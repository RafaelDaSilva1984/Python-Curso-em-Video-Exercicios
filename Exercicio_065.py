
q = 'S'
s = sm = maior = menor = media = 0
while q in 'Ss':
    v = int(input('Insira um valor: '))    
    sm += v
    s += 1 
    if s == 1:
        maior = menor = v
    else:
        if v > maior:
            maior = v
        if v < menor:
            menor = v   
    q = str(input('Você quer continuar [S/N]: ')).upper().strip()[0]
    media = sm / s      
print('O Menor valor é {} e o Maior valor é {}:'.format(menor,maior))
print('Dos', s ,'valores digitados','teremos média entre valores é:', media,) 



