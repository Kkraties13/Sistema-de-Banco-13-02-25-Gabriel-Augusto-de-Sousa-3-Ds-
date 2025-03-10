import os

def enter():
    
    print("Pressione ENTER para continuar")
    input()
    
    os.system("cls")
    
class Banco:
    
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
        self.saldo_usuario = 0
        self.extrato_usuario = ["Histórico de operações"]
    

# login = "Teste"
# senha = "1234"

# saldo_usuario = 0
# extrato_usuario = ["Histórico de operações"]

    def Login(self, login_usuario = input("Digite o nome de usuário ou e-mail: "), senha_usuario = input("Digite sua senha: ")):
        
        while login_usuario.upper() != login_usuario.upper() or senha_usuario != self.senha:
            
            print("Login ou senha inválidos. Tente novamente.")

            enter()
            
            login_usuario = input("Digite o nome de usuário ou e-mail: ")
            senha_usuario = input("Digite sua senha: ")

        os.system("cls")

        print("Você está logado")

        enter()
        
        
        
    def Saque(self, valor_saque = float(input("Digite o valor para saque: "))):

        os.system("cls")
        
        if self.saldo_usuario > 0:

            print("Saldo insuficiente\nFaça ao menos um depósito")
            enter()     
            
        else:  
            
            valor_saque = float(input("Digite o valor para saque: "))
            
            saldo_usuario -= valor_saque
            
            self.extrato_usuario.append(f"- {str(valor_saque)}")
            
            print(f"Saque realizado com sucesso\nO saldo atual é de {saldo_usuario} Reais")
            
            enter()
            
            
            
    def Deposito(self, valor_deposito = float(input("Digite o valor do depósito: "))):

            os.system("cls")        
                
            valor_deposito = float(input("Digite o valor do depósito: "))

            saldo_usuario += valor_deposito
            
            self.extrato_usuario.append(f"+ {str(valor_deposito)}")
            
            print(f"Depósito realizado com sucesso\nO saldo atual é de {saldo_usuario} Reais")
            
            enter()
            
            
            
    def menu(self, opcao = input("Funções do banco:\n\tDigite S para Saque\n\tDigite D para Depósito\n\tDigite SA para Exibir o Saldo\n\tDigite E para ver o extrato\n\tDigite SC para saír da conta\nDigite aqui: ")
):

        while opcao.upper() != "SC":
            
            if opcao.upper() == "S":
                
                self.Saque()
            
            elif opcao.upper() == "D":
                
                self.Deposito()
            
            elif opcao.upper() == "SA":

                os.system("cls")
                
                print(f"O saldo atual da conta é: {saldo_usuario}")
                
                enter()
                
            elif opcao.upper() == "E":
                
                os.system("cls")
                
                for posicao_operacao in range(len(extrato_usuario)):
                    
                    print(self.extrato_usuario[posicao_operacao])
            
                
                print(f"Fim do extrato\n\nSaldo da Conta: R${saldo_usuario}\n")
                
                enter()
            
            else:
                
                os.system("cls")
                
                print("A chave de operação não consta no sistema ou foi digitada errada")
                
                enter()
                
                
                    
                
            
            opcao = input("Funções do banco:\n\tDigite S para Saque\n\tDigite D para Depósito\n\tDigite SA para Exibir o Saldo\n\tDigite E para ver o extrato\n\tDigite SC para saír da conta\nDigite aqui: ")

        
        os.system("cls")
        
        print("O Sistema foi finalizado com sucesso!")