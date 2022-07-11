


vl = (int(input('Digite o valor 01: ')),
     int(input('Digite o valor 02: ')),
     int(input('Digite o valor 03: ')),
     int(input('Digite o valor 04: ')))

print(f'Os valores da sua escolha foram:{vl}')
print(f'O número 9 apareceu {vl.count(9)}')
if 3 in vl:
    print(f'O numero 3 está na {vl.index(3)+1}ª posição')
else:
    print(f'O numero 3 não foi inserido em nenhuma posição.' )
print('Os valores foram\n', end='')
for v in vl:
    if v % 2 == 0:
        print(v,'-> Par', )
    if v % 2 != 0:
        print(v,'-> Impar')

