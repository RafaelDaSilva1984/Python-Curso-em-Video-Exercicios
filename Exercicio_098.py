from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-'*35)
    print(f'Contagem de {i} a {f} de {p} em {p}.')
    sleep(1)
    if i < f:
        c = i
        while c <= f:
            print(f'{c}', end=' ', flush=True)
            sleep(0.35)
            c += p
        print('FIM!')
    else:
        c = i
        while c >= f:
            print(f'{c}', end=' ', flush=True)
            sleep(0.35)
            c -= p
        print('FIM!')   
#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-'*35)
print('Agora é a sua vez de personalizar o contagem...')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
