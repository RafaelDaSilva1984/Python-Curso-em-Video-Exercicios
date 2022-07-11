from random import randint # faz sorteio dos valores do range
from time import sleep # adicina o tempo para a impressão em tela
print('-_-'*9) # separar as linhas
print('    JOGO DA MEGA SENA') # mensagem de inicio
lista = list() # primeira lista
jogos = list() # lista geral
sorteio = int(input('Quantos você quer que eu sorteie ? ')) # Solicita qtd de vez a ser executado sorteio
tot = 1 # laço
while tot <=sorteio: # Inicio laço do sorteio
    cont = 0 # contador de 0 a 6 valores a ser sorteados
    while True: # laço para eliminar números repitidos
        num = randint(1,60) # range de inicio e fim
        if num not in lista: # verifica se o valor já está na lista se não estiver adiciona o mesmo na lista
            lista.append(num) # adiciona
            cont += 1 # conatador de valores
        if cont >= 6: # limite de números
            break # termina qaundo valores igual a 6
    lista.sort() # ordena do menor para o maior valor
    jogos.append(lista[:]) # adiciona uma cópia da lista
    lista.clear() # lista os valores da lista anterior
    tot += 1 # total do laço principal
print('-='*3,f'SORTEANDO {sorteio} Jogos','-='*3) # imprime os valores da lista
for i , l in enumerate(jogos): # enumera o numero da lista
    print(f'Jogo {i+1}: números sorteados :{l}') # enumera o numero da lista e imprime alista
    sleep(1) # tempo entre uma impressão e outra
print('_-_ '*5, 'BOA SORTE !!!','_-_ '*5 ) # Mensagem final
