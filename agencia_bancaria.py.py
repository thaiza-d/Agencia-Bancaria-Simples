limite = 500
extrato= 0
def menu():
    print('-'*30)
    print('AGÊNCIA BANCÁRIA'.center(30))
    print('-'*30)
    print('''[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair''')

def opcao1():
    dep = float(input('Qual valor deseja depositar? R$'))
    print(f'Valor R${dep:.2f} adicionado a sua conta com sucesso!')


def opcao2():
    sac = float(input('Qual valor deseja sacar? R$'))
    try:
        if sac <= 500:
            print(f'Saque de R${sac:.2f} efetuado com sucesso!')
        else:
            print('Digite um valor menor ou igual ao seu limite diário de R$500.00')
    except ValueError:
        print('ERRO! Digite um número válido!')


def opcao3():
    print(f'Segue abaixo as informações do seu extrato bancário:\n{extrato}')

while True:
    menu()
    try:
        opcao = int(input('Sua opção: '))
    except (ValueError, TypeError):
        print('Erro! Digite uma opção válida')
        continue
    if opcao == 1:
        opcao1()
    elif opcao == 2:
        opcao2()
    elif opcao == 3:
        opcao3()
    elif opcao == 4:
        print('Encerrando o programa!')
        break
    else:
        print('Operação inválida! Selecione um número válido!')