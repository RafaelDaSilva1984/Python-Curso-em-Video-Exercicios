# Modelo Rafael iniciante
num = [[], [], []]
for c in range(0,3): 
    l = c  
    valor = int(input(f'Digite um valor [{c} , {l}]:'))
    num[0].append(valor)
for c in range(0,3):
    a = 1
    valor = int(input(f'Digite um valor [{a} , {c}]:'))
    num[1].append(valor)
for c in range(0,3):
    b = 2
    valor = int(input(f'Digite um valor [{b} , {c}]:'))
    num[2].append(valor)

print(f'[{num[0][0]: ^5}] [{num[0][1]: ^5}] [{num[0][2]: ^5}]')
print(f'[{num[1][0]: ^5}] [{num[1][1]: ^5}] [{num[1][2]: ^5}]')
print(f'[{num[2][0]: ^5}] [{num[2][1]: ^5}] [{num[2][2]: ^5}]')

# Modelo Mestre Guanabara
num = [[0,0,0],[0,0,0],[0,0,0]]
for c in range(0,3):
    for l in range(0,3):
        num[c][l] = int(input(f'Digite um valor [{c} , {l}]:'))
for c in range(0,3):
    for l in range(0,3):
        print(f'[{num[c][l]: ^5}]', end='')
    print()
