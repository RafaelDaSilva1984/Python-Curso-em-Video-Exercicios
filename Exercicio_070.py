

print("---------Valores de consumo----------")
soma = 0
qtd = 0
qtd1000 = 0
menor = 0
barato = 0
while True:
    prodt = str(input("Que produto você comprou: ")).upper()
    val = float(input("Qual o valor: "))
    if val > 1000:
        qtd1000 += 1
    soma = soma + val
    qtd += 1
    if qtd == 1:
        menor = val
        barato = prodt
    else:        
        if val < menor:
            menor = val 
            barato = prodt                          
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input("Você que continuar:[S/N] ")).strip().upper()[0]
    if escolha == 'N':
        break

print(f'Valor total de compras: R$ {soma :.2f}')
print(f'Foram {qtd1000} produtos da lista acima de R$ 1000,00')
print(f'O produto de menor valor é {barato} e custou R$ {menor :.2f}')
print('---------- Fim das Compras ----------')



