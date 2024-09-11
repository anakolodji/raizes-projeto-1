def calcular_area_cultura1(largura, comprimento):
    return largura * comprimento

def calcular_insumos_cultura1(area, insumo_por_metro):
    return area * insumo_por_metro

def dataEntry():
    print("Selecione o tipo de dado")
    while True:
      print("1. Largura do plantio")
      print("2. Comprimento do plantio")
      print("3. Insumo")
      print("4. Deletar dados")
      print("5. Sair do programa")
      escolha = input("Escolha uma opção: ")

def mainMenu():
    while True:
        print("1. Entrada de dados")
        print("2. Saída de dados")
        print("3. Atualizar dados")
        print("4. Deletar dados")
        print("5. Sair do programa")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            dataEntry()
            pass
        elif escolha == '2':
            print("Saída de dados")
            # Lógica para saída de dados
            pass
        elif escolha == '3':
            # Lógica para atualizar dados
            pass
        elif escolha == '4':
            # Lógica para deletar dados
            pass
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

mainMenu()
