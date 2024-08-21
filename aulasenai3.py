# Crie um sistema de banco, com as seguintes operações:

# # SISTEMA DE BANCO 

# - Acesso a conta
# - Ver extrato
# - Fazer um deposito
# - Fazer um saque 
# - Sair do sistema 



senha =  int(input('cadastre sua senha:'))
login  =  input('cadastre seu login: ')

login_user = input("Digite seu usuário: ")
senha_user = int(input("Digite sua senha: "))

if senha == senha_user and login == login_user:
    print('Acesso autorizado')

saldo = 0        

menu = 1
while menu > 0:
      print("Seja bem-vindo, escolha uma opção abaixo: ")
      print('0. Ver extrato \n1. Fazer depósito \n2. Fazer saque \n3. Sair')
      menu = menu - 1

saldo = 0 

lista = ["Ver extrato", "Fazer depósito", "Fazer saque, Sair"]

escolha = int(input("Escolha uma opção (0/1/2/3): "))

if escolha == 0:
    print(f"Seu saldo atual é: R$ {saldo:.2f}")

elif escolha == 1:
            deposito = float(input("Digite o valor do depósito: R$ "))
            saldo += deposito
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")
elif escolha == 2:
      saque = float(input(f"Digite o valor que deseja sacar: "))
      if saque > saldo:
            print("Saldo insuficiente")
      if saque < saldo:
        print(f"Saque de R$ {saque:.2f} realizado com sucesso!")           

elif escolha == 3:
            print("Saindo, Até logo!")
else:
    print("Opção invalida, escolha um número de 0 a 3")

n = input('clique enter sair')
      