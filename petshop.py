def agendar_servicos():
    print("\n=== Agendar Serviços ===")
    print("1. Banho - R$25,00")
    print("2. Tosa - R$35,00")
    print("3. Consulta Veterinária - R$100,00")
    print("4. Fotografia Profissional para Pets - R$150,00")
    print("0. Sair")
    opcao3 = int(input())
    if opcao3 == 1:
        print("Serviço selecionado : Banho")
        databanho = str(input("Digite a data para realizar o serviço: "))
        print("Serviço marcado com sucesso")
        agendar_servicos()
    elif opcao3 == 2:
        print("Serviço selecionado: Tosa")
        datatosa = str(input("Digite a data para realizar o serviço: "))
        print("Serviço marcado com sucesso")
        agendar_servicos()
    elif opcao3 == 3:
        print("Serviço selecionado: Consulta Veterinária")
        dataconsulta = str(input("Digite a data para realizar o serviço: "))
        print("Serviço marcado com sucesso")
        agendar_servicos()
    elif opcao3 == 4:
        print("Serviço selecionado: Fotografia Profissional para Pets")
        datafotografia = str(input("Digite a data para realizar o serviço: "))
        print("Serviço marcado com sucesso")
        agendar_servicos()
    elif opcao3 == 0:
        menu()
    elif opcao3 != 1 and opcao3 != 2 and opcao3 != 3 and opcao3 != 4 and opcao3 != 0:
        print("Voce não selecionou nenhuma opção, por favor digite novamente...")
        return agendar_servicos()

def listar_servicos():
    print("=== Listar Serviços ===")
    print("Banho - R$25,00")
    print("Tosa - R$35,00")
    print("Consulta Veterinária - R$100,00")
    print("Fotografia Profissional para Pets - R$150,00")

def produtos():
    print("Ração para cães adultos - R$29,90 1Kg")
    print("Ração para cães filhotes - R$19,90 1Kg")
    print("Ração para gatos adultos - R$21,90 1Kg")
    print("Ração para gatos filhotes - R$15,90 1Kg")

def comprar_produto():
    global gatoadulto, gatofilhote, caoadulto, caofilhote
    print("=== Comprar Produto ===")
    print("1. Ração para cães adultos R$ 29,90 1Kg")
    print("2. Ração para cães filhotes R$ 19,90 1Kg")
    print("3. Ração para gatos adultos R$ 21,90 1Kg")
    print("4. Ração para gatos filhotes R$ 15,90 1Kg")
    print("0. Sair")
    opcao2 = int(input("Digite o número do produto que deseja comprar: "))
    if opcao2 == 1:
        caoadulto = int(input("Digite quantas deseja comprar: "))
        print("Ração para cães adultos 1Kg foi adcionada ao carrinho")
        comprar_produto()
    elif opcao2 == 2:
        caofilhote = int(input("Digite quantas deseja comprar: "))
        print("Ração para cães filhotes 1Kg foi adcionada ao carrinho")
        comprar_produto()
    elif opcao2 == 3:
        gatoadulto = int(input("Digite quantas deseja comprar: "))
        print("Ração para gatos adultos 1Kg foi adcionada ao carrinho")
        comprar_produto()
    elif opcao2 == 4:
        gatofilhote = int(input("Digite quantas deseja comprar: "))
        print("Ração para gatos filhotes 1Kg foi adcionada ao carrinho")
        comprar_produto()
    elif opcao2 == 0:
        return menu()
    elif opcao2 != 1 and opcao2 != 2 and opcao2 != 3 and opcao2 != 4 and opcao2 != 0:
        print("Voce não selecionou nenhuma opção, por favor digite novamente...")
        return comprar_produto()

def menu():
    while True:
            print("=== Menu do Petshop ===")
            print("1. Listar Produtos")
            print("2. Comprar Produto")
            print("3. Listar Serviços")
            print("4. Agendar Serviço")
            print("0. Sair")
            opcao = int(input())
            if opcao == 1:
                print("Listar Produtos")
                produtos()
            elif opcao == 2:
                print("Comprar produto")
                comprar_produto()
            elif opcao == 3:
                print("Listar Serviços")
                listar_servicos()
            elif opcao == 4:
                print("Agendar Serviço")
                agendar_servicos()
            elif opcao == 0:
                break
            elif opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 0:
                print("Voce não selecionou nenhuma opção, por favor digite novamente...")
menu()