while True:
    exp = str(input('Digite a expressão: ')).strip()   
    pilha = list()
    for simb in exp:
        if simb == '(':
            pilha.append('(')  # adiciona na pilha
        elif simb == ')':
            if len(pilha) > 0:
                pilha.pop() # retira da pilha
            else:
                pilha.append(')') # adiciona na pilha
                break
    if len(pilha) == 0: # qtd de simb na pilha == 0 está correto
        print(f'Sua expressão está válida...quantidade de simbolos  abertos e fechados igual a: {len(pilha)}')
    else:  # se qtd de simb maior que zero está incorreto
        print(f'Sua expressão está inválida...quantidade de simbolos  abertos e fechados é maior que zero total de: {len(pilha)}')
    resp = str(input('Quer continuar [S/N]:'))
    if resp in 'Nn':
        break
print('Fim...')



