#Exercicio 096
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de: {larg}m² x {comp}m² é de {a:.2f}m².')

    
#programa principal
print('Controle terrenos')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c )

