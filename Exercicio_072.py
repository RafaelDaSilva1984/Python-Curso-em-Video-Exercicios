print('Exercìcio 072 de Tuplas - Valores entre 0 e 20')
numext = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 
'Nove', 'Dez', 'Onze','Doze', 'Treze', 'Quatorze', 'Quinze',
'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
maior = menor =  0

while True:    
    while True:
        num = int(input('Digite um valor de 0 a 20: '))          
        if num in range(0 , 21):            
            break
        if num > maior:
            maior = num 
            print('Valor Maior',end= ' !!! ')
        if num < menor:
            menor = num 
            print('Valor Menor',end= ' !!! ')          
                  
        print(f'Por favor, Digite novamente valor entre 0 e 20, sua última escolha foi {num} ... ')
          
    print(f'O valor digitado foi: {numext[num]}') 
    escolha = input('Deseja continuar programa escolha -> [S/N]: ').strip().upper()[0]
    if escolha not in 'Ss':
        break
print(f'Você escolheu a opção {escolha}ão o programa foi Finalizado...')
           

    
        
      

        



            
    
    
       
        




       


    

    
      

       
        