from math import factorial
print(('-_-' * 20))
num = int(input('Digite um valor com WHILE:! '))
c = num + 1
f = 1
print('Calculando Fatorial {}! = '.format(num), end=' ')
while c > 1:
    c = c -1
    f = f * c
    print('{}'. format(c), end= ' ')
    print(' x 'if c > 1 else ' = ', end='')
print('({})'. format(f))
print(('-_-' * 20))
num = int(input('Digite um valor com FOR:! '))
c = num + 1
f = 1
print('Calculando Fatorial {}! = '.format(num), end=' ')
for n in range(0, num):
    c = c -1
    f = f * c
    print('{}'. format(c), end= ' ')
    print(' x 'if c > 1 else ' = ', end='')
print('({})'. format(f))
print(('-_-' * 20))

num = int(input('Digite um valor com MATH IMPORT FACTORIAL:! '))
f = factorial(num)
print('O fatorial de {}! é = {}:'.format(num , f))

print(('-_-' * 20))