   
while True:
    v = int(input('Digite o valor da sua tabuada desejada: ')) 
    if v < 0:
        break       
    for c in range(1, 11):           
        print(f'{v} x {c} = {v * c}')
print('Programa tabuada não aceita número negativo... ENCERRADO')

'''  
# Com While não consegui....
ct = 0
while True:
    v = int(input('Digite o valor da sua tabuada desejada: ')) 
    if v < 0:
        break       
    while ct < 10:
        ct +=1           
        print(f'{v} x {ct} = {v * ct}')
'''         
    
          
    
        
    


