
valor = []
mai = 0
men = 0
for vl in range(0, 5):
    valor.append(int(input(f'Digite um valor na posição {vl} : ')))
    if vl == 0: # Se o Primeiro valor da lista valor igaul a 0
        mai = men = valor[vl] # O maior = menor = valor
    else:
        if valor[vl] > mai: # Se o valor na posição vl = maior
            mai = valor[vl] # maior = valor na vl
        if valor[vl] < men: # Se o valor na posição vl = menor
            men = valor[vl] # menor = valor na vl       
print(f'Os valores da lista são:{valor}')
print(f'O maior valor é: {mai} nas posições', end= '')
for i, v in enumerate(valor):
    if v == mai:
        print(f' {i}...', end='')
print()
print(f'O menor valor é: {men} nas posições', end= '')
for i, v in enumerate(valor):
    if v == men:
        print(f' {i}...', end='')
print()
