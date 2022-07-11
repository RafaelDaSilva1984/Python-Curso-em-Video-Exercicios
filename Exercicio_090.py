print('-*-'*20)
dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Media']= float(input(f'A Média de {dados["Nome"]} : '))
if dados['Media'] >= 7.5:
   dados['Situacao'] = 'Aprovado'
elif 5 <= dados['Media'] < 7.5:
    dados['Situacao'] = 'recuperação'
else:
    dados['Situacao'] = 'Reprovado'
print('-*-'*15)
for k, v in dados.items():
    print(f'- {k} é igual a {v}')
print('-*-'*10)
print(dados)
print('-*-'*5)
