v = int(input('Digite valor p/ Fibonaci: '))
termo1 = 0 # termo definido
termo2 = 1 # termo definido
print(termo1 ,'->',termo2, end= '-> ')
cont = 3 
while cont <= v:
    termo3 = termo1 + termo2 # termo definido entre a soma do TERMO 1 + TERMO 2             
    print(termo3, end= '-> ')
    termo1 = termo2 # Passa o valor do termo1 para termo2
    termo2 = termo3 # Passa o valor do termo2 para termo3
    cont += 1
print('...-> Fim da sequeência de Fibonaci ...')





