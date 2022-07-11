num = [[0,0,0],[0,0,0],[0,0,0]]
somaimpar = 0
somapar = 0
somac = 0
maior = 0
maior2 = 0
vl = 0
for c in range(0,3):
    for l in range(0,3):
        num[c][l] = int(input(f'Digite um valor [{c} , {l}]:'))
        if num[c][l] > maior:
            maior = num[c][l]
        if num[c][l] % 2 == 0:
            num.append(num[c][l])
            somapar += num[c][l]
        else:
            num.append(num[c][l])
            somaimpar += num[c][l]
    somac = (num[0][2] + num [1][2] + num [2][2])
    if num[1][l] > maior2:
        maior2 = num[1][l]  
for c in range(0,3):
    for l in range(0,3):
        print(f'[{num[c][l]: ^5}]', end='')
    print()
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores impares é {somaimpar}')
print(f'A soma dos valores da terceira coluna é {somac}')
print(f'O maior valor da segunda linha é {maior2}')
print(f'O maior valor da matriz é {maior}')




