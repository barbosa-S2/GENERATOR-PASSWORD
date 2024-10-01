import random

print('=====Seja Bem Vindo ao Generator Password=====')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*().,;'

number = input('Quantia de senhas para serem geradas: ')
number = int(number)

length = input('Quantos caracteres devem ter suas senhas: ')
length = int(length)

print('\nEstas são Senhas: ')
 
for pwd in  range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)


