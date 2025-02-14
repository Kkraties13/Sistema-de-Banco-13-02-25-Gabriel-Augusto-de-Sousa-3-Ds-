import os

def enter():
    
    print("Pressione ENTER para continuar")
    input()
    
    os.system("cls")

login = "Teste"
senha = "1234"

saldo_usuario = 0
extrato_usuario = ["Histórico de operações"]

login_usuario = input("Digite o nome de usuário ou e-mail: ")
senha_usuario = input("Digite sua senha: ")



while login_usuario.upper() != login.upper() or senha_usuario != senha:
    
    print("Login ou senha inválidos. Tente novamente.")
    login_usuario = input("Digite o nome de usuário ou e-mail: ")
    senha_usuario = input("Digite sua senha: ")
    

os.system("cls")

print("Você está logado")

enter()

opcao = input("Funções do banco:\n\tDigite S para Saque\n\tDigite D para Depósito\n\tDigite SA para Exibir o Saldo\n\tDigite E para ver o extrato\n\tDigite SC para saír da conta\nDigite aqui: ")

while opcao.upper() != "SC":
    
    if opcao.upper() == "S":
        
        os.system("cls")
        
        valor_saque = float(input("Digite o valor para saque: "))
        
        saldo_usuario -= valor_saque
        
        extrato_usuario.append(f"- {str(valor_saque)}")
        
        print(f"Saque realizado com sucesso\nO saldo atual é de {saldo_usuario} Reais")
        
        enter()
    
    elif opcao.upper() == "D":
        
        os.system("cls")        
        
        valor_deposito = float(input("Digite o valor do depósito: "))
        saldo_usuario += valor_deposito
        
        extrato_usuario.append(f"+ {str(valor_deposito)}")
        
        print(f"Depósito realizado com sucesso\nO saldo atual é de {saldo_usuario} Reais")
        
        enter()
    
    elif opcao.upper() == "SA":

        os.system("cls")
        
        print(f"O saldo atual da conta é: {saldo_usuario}")
        
        enter()
        
    elif opcao.upper() == "E":
        
        os.system("cls")
        
        for posicao_operacao in range(len(extrato_usuario)):
            
            
            print(extrato_usuario[posicao_operacao])
    
        
        print(f"Fim do extrato\n\nSaldo da Conta: R${saldo_usuario}\n")
        
        enter()
        
        
            
        
    
    opcao = input("Funções do banco:\n\tDigite S para Saque\n\tDigite D para Depósito\n\tDigite SA para Exibir o Saldo\n\tDigite E para ver o extrato\n\tDigite SC para saír da conta\nDigite aqui: ")