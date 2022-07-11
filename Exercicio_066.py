print('''Esse Programa é para Digitar valores inteiros, somar os valores 
             E somar as quantidade e só para com 999...''')
n = s = q = 0
while True:
    n  = int(input('Digite um valor (999 faz parar): '))
    if n == 999:
        break
    q += 1
    s += n
print(f'A soma é {s} e quantidade de valores é {q}')
