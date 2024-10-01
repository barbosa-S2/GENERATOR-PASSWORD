import random

def gerar_senhas(quantidade, comprimento):
    """Gera a quantidade especificada de senhas com o comprimento indicado.

    Args:
        quantidade (int): Número de senhas a serem geradas.
        comprimento (int): Comprimento de cada senha.
    """
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*().,;'

    for _ in range(quantidade):
        senha = ''
        for _ in range(comprimento):
            senha += random.choice(chars)
        print(senha)

while True:
    print('\n==== Seja Bem Vindo ao Generator Password ======')
    print('===== 1. Gerar novas senhas ====================')
    print('===== 2. Sair ==================================')
    opcao = input('\nEscolha uma opção: ')

    if opcao == '1':
        quantidade = int(input('Quantas senhas você quer gerar? '))
        comprimento = int(input('Qual o comprimento das senhas? '))
        gerar_senhas(quantidade, comprimento)
    elif opcao == '2':
        print('Saindo...')
        break
    else:
        print('Opção inválida. Por favor, escolha 1 ou 2.')
