menu = True
v = int(input('Digite um valor: '))
v2 = int(input('Digite um valor: '))
while menu != 5:
    menu = int(input(''' Escolha a Opção
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Sair
    Qual sua escolha entra as opções: '''))
    if menu == 1:
        somar = (v + v2)
        print('A soma de {} e {} é igual a:'.format(v,v2),somar)
    if menu > 5:
        print('Opção Inválida, tente novamente...')
    elif menu == 2:    
        mult = (v * v2)
        print('A multiplicação entre {} e {} é igual a: '.format(v,v2),mult)
    elif menu == 3:
        if v > v2:
            maior = v
            print('O Maior valor entre {} e {} é: '.format(v,v2),v)
        elif v2 > v:
            maior = v2
            print('O Maior valor entre {} e {} é: '.format(v,v2), v2)
    elif menu == 4:
        v = int(input('Digite um valor: '))
        v2 = int(input('Digite um valor: '))
        menu = int(input(''' Escolha a Opção
        [1] - Somar
        [2] - Multiplicar
        [3] - Maior
        [4] - Novos números
        [5] - Sair
        Qual sua escolha entra as opções: '''))
        if menu == 1:
            somar = (v + v2)
            print('A soma de {} e {} é igual a:'.format(v,v2),somar)
        if menu > 5:
            print('Opção Inválida, tente novamente...')
        elif menu == 2:    
            mult = (v * v2)
            print('A multiplicação entre {} e {} é igual a: '.format(v,v2),mult)
        elif menu == 3:
            if v > v2:
                maior = v
                print('O Maior valor entre {} e {} é: '.format(v,v2),v)
            elif v2 > v:
                maior = v2
                print('O Maior valor entre {} e {} é: '.format(v,v2), v2)
        
else:
    print('Saindo do Programa ...')




