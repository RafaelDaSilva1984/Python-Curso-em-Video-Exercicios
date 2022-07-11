num = [[], []]
vl = 0
for sel in range(1,8):
    vl = (int(input(f'Digite o {sel}º valor: ')))
    if vl % 2 == 0:
        num[0].append(vl)
        num[0].sort()     
    else:
        vl % 2 == 1
        num[1].append(vl)
        num[1].sort()        
print(f'Todos os valores Pares na Ordem Crescente {num[0]} e Impares na Ordem Crescente  {num[1]}')


