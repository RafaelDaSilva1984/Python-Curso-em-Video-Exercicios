print('NOTAS ALUNOS')
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2 ) / 2
    ficha.append([nome,[nota1, nota2], media])
    resp = str(input('Quer Continuar [S/N] ? '))
    if resp in 'Nn':
        break
print('_=_'*10)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('---'*10)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*15)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe ...): '))
    if opc == 999:
        print('Finalizando ....')
        break
    if opc <= len(ficha) -1 :
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<Volte Sempre>>>')
