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
    
lista = ["Ver extrato", "Fazer depósito", "Fazer saque"]

for choose_num in range(len(lista)):
    print(choose_num+1, "-", lista[choose_num])

escolha = int(input("Escolha uma opção: "))

if escolha == 1:
    print(f"Seu saldo atual é: R$ {saldo:.2f}")

elif escolha == 2:
            deposito = float(input("Digite o valor do depósito: R$ "))
            saldo += deposito
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")
elif escolha == 3:
      saque = float(input(f"Digite o valor que deseja sacar: "))
      if saque > saldo:
            print("Saldo insuficiente")
      else:
        print(f"Saque de R$ {saque:.2f} realizado com sucesso!")


n = input('clique enter sair')      