from datetime import datetime
dados = dict() 
print('*-*'*12)   
dados['nome'] = str(input('NOME: '))
nasc = int(input('Ano nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['carteira'] = int(input('Número do CTPS [0 não tem...]: '))
if dados['carteira'] != 0:
    dados['contratacao'] = int(input('Ano Contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao']+40)- datetime.now().year)
print('*-*'*12)
for k,v in dados.items():      
    print(f'  -{k} tem o valor ->: {v}')
print('*-*'*12)
print(dados)
