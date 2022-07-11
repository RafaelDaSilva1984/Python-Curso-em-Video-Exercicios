from random import randint
print('Vamos Jogar Par ou Impar')

sv = 0
sd = 0
soma = (sv + sd)
while sd == 0:
    computador = randint(0, 10)
    jogador = (int(input('Digite uma valor: ')))
    escolha = str(input('Par ou Impar: [P/I]')).upper().strip()
    if escolha in 'Pp' and (computador + jogador) % 2 == 0:
        print('Vc venceu')        
        sv += 1
        soma = sv + sd      
       
    if escolha in 'Pp' and (computador + jogador) % 2 == 1:
        print('Vc Perdeu')                       
        sd += 1 
        soma = sv + sd         

    if escolha in 'Ii' and (computador + jogador) % 2 == 0:
        print('Vc Perdeu')                            
        sd += 1
        soma = sv + sd        

    if escolha in 'Ii' and (computador + jogador) % 2 == 1:
        print('Vc Perdeu')                           
        sd += 1
        soma = sv + sd        

print(f'Foram {soma} tentativas, minha Escolha foi',computador)