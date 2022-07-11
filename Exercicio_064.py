print('''Sequência de valores, 
Onde todos os valores menos (-) o GAP serão somados, 
E o looping somente  será quebrado quando inseridos  o valor (999)''')
v = True
s = 0
sm = 0
while v != 999:
    v = int(input('Digite um valor {}: '.format(s +1)))    
    sm = sm + v
    s += 1
    #print(v)
    #print(sm)    
print('Foram inseridos valores:',s -1)
print('Soma dos valores inseridos foi:',sm - 999)