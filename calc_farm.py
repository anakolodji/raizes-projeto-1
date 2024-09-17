# Dicionário para armazenar os insumos de cada cultura
insumos_culturas = {
    'soja': {
        'Nitrogênio (N)': 17.5,
        'Fósforo (P)': 4.5,
        'Potássio (K)': 5
    },
    'milho': {
        'Nitrogênio (N)': 1.75,
        'Fósforo (P)': 2.5,
        'Potássio (K)': 4
    }
}

# Dicionário para armazenar unidades de medida (opcional)
unidades_medidas = {
    'soja': {
        'Nitrogênio (N)': 'g',
        'Fósforo (P)': 'g',
        'Potássio (K)': 'g'
    },
    'milho': {
        'Nitrogênio (N)': 'g',
        'Fósforo (P)': 'g',
        'Potássio (K)': 'g'
    }
}


# Função para listar os insumos específicos de uma cultura com números
def listar_insumos(cultura):
    print(f"\nLista de insumos cadastrados para {cultura.capitalize()}:")
    for idx, (insumo, _) in enumerate(insumos_culturas[cultura].items(), start=1):
        print(f"{idx}. {insumo}")


# Função para calcular os insumos necessários
def calcular_insumos(area, cultura, insumos_desejados):
    insumos_detalhados = {}  # Armazena insumos detalhados para cada tipo
    for tipo in insumos_desejados:
        if tipo in insumos_culturas[cultura]:
            quantidade_por_m2 = insumos_culturas[cultura][tipo]
            insumos_detalhados[tipo] = area * quantidade_por_m2
        else:
            print(f"Insumo '{tipo}' não encontrado para {cultura}.")

    # Imprimir insumos detalhados
    for tipo, quantidade in insumos_detalhados.items():
        unidade = unidades_medidas[cultura].get(tipo, 'g/m2')
        print(f"Você precisará de {quantidade} {unidade} de {tipo} para a {cultura}.")

    return insumos_detalhados


# Função para inserir insumos
def inserir_insumos(cultura):
    listar_insumos(cultura)
    indices = input("Digite os números dos insumos desejados, separados por vírgula: ")
    indices = [int(i.strip()) for i in indices.split(',')]
    insumos_desejados = [list(insumos_culturas[cultura].keys())[i - 1] for i in indices if
                         0 < i <= len(insumos_culturas[cultura])]
    print(f"Insumos selecionados: {insumos_desejados}")
    return insumos_desejados


# Função para calcular a área e o número de ruas
def calcular_area(cultura):
    if cultura == 'soja':
        lado = float(input("Seu terreno é quadrado. Insira o valor do lado do terreno (em metros): "))
        largura = comprimento = lado
    elif cultura == 'milho':
        comprimento = float(input("Seu terreno é retangular. Insira o comprimento do terreno (em metros): "))
        largura = float(input("Agora insira a largura do terreno (em metros): "))
    else:
        print("Cultura inválida!")
        return 0, 0, 0, 0

    area = largura * comprimento

    # Calcula o número de ruas com base na largura do terreno
    largura_ideal = 10
    if largura >= 2 * largura_ideal:
        ruas = int(largura // largura_ideal)
    else:
        ruas = 1  # Se não houver largura suficiente para 2 ruas, a rua ocupará toda a largura

    return area, largura, comprimento, ruas


# Função para imprimir a tabela
def imprimir_tabela():
    print("\nTabela de Dados:")
    print(f"{'N°':<5}{'Cultura':<10}{'Área (m2)':<15}{'Largura (m)':<15}{'Comprimento (m)':<20}{'Número de Ruas':<15}")
    for i, (cultura, area, largura, comprimento, ruas) in enumerate(
            zip(culturas_plantadas, areas, larguras, comprimentos, numero_ruas), start=1):
        print(f"{i:<5}{cultura.capitalize():<10}{area:<15.2f}{largura:<15.2f}{comprimento:<20.2f}{ruas:<15}")


# Função para adicionar novo insumo
def adicionar_novo_insumo(cultura):
    insumo = input("Digite o nome do novo insumo: ")
    quantidade = float(
        input(f"Digite a quantidade de {insumo} (em kg/m2 para fertilizante e semente, L/m2 para herbicida): "))
    insumos_culturas[cultura][insumo] = quantidade
    unidades_medidas[cultura][insumo] = input(f"Digite a unidade de medida para {insumo} (kg/L/g): ")


# Função de menu para inserir insumos
def menu_insumos():
    while True:
        print("\nMenu de insumos:")
        print("1. Adicionar novo insumo")
        print("2. Listar insumos")
        print("3. Voltar ao menu principal")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            print("\nEscolha a cultura:")
            print("1. Soja")
            print("2. Milho")
            opcao_cultura = int(input("Digite o número da cultura desejada: "))
            cultura = 'soja' if opcao_cultura == 1 else 'milho'
            adicionar_novo_insumo(cultura)
        elif opcao == 2:
            print("\nEscolha a cultura:")
            print("1. Soja")
            print("2. Milho")
            opcao_cultura = int(input("Digite o número da cultura desejada: "))
            cultura = 'soja' if opcao_cultura == 1 else 'milho'
            insumos_desejados = inserir_insumos(cultura)
            print(f"Insumos selecionados para cálculo: {insumos_desejados}")
        elif opcao == 3:
            break
        else:
            print("Opção inválida!")


def atualizar_dados(posicao):
    cultura = culturas_plantadas[posicao]
    print(f"\nAtualizando dados para a cultura {cultura.capitalize()}:")

    # Opções para atualizar largura e/ou comprimento
    print("Escolha o que deseja atualizar:")
    print("1. Largura")
    print("2. Comprimento")
    print("3. Largura e Comprimento")
    escolha = int(input("Digite o número da opção desejada: "))

    if escolha == 1 or escolha == 3:
        largura = float(input("Digite o novo valor da largura (em m): "))
        larguras[posicao] = largura
        # Atualizar número de ruas com base na nova largura
        numero_ruas[posicao] = calcular_numero_ruas(largura)

    if escolha == 2 or escolha == 3:
        comprimento = float(input("Digite o novo valor do comprimento (em m): "))
        comprimentos[posicao] = comprimento

    if escolha == 1 or escolha == 2 or escolha == 3:
        # Recalcular área com base nos valores atualizados de largura e comprimento
        area = larguras[posicao] * comprimentos[posicao]
        areas[posicao] = area

        # Informar ao usuário a nova área de plantio
        print(f"Sua nova área de plantio é de {area:.2f} m2.")

        # Recalcular insumos com base na nova área
        insumos_desejados = list(insumos_culturas[cultura].keys())  # Assume todos os insumos
        insumos_detalhados = calcular_insumos(area, cultura, insumos_desejados)
        insumos[posicao] = insumos_detalhados

        # Informar ao usuário a quantidade de insumos necessária
        print("Você precisará dos seguintes insumos:")
        for tipo, quantidade in insumos_detalhados.items():
            unidade = unidades_medidas[cultura].get(tipo, 'g/m2')
            print(f"{quantidade} {unidade} de {tipo}.")


# Função para calcular o número de ruas com base na largura do terreno
def calcular_numero_ruas(largura):
    largura_ideal = 10  # Largura ideal para cada rua em metros
    if largura >= 2 * largura_ideal:
        ruas = int(largura // largura_ideal)
    else:
        ruas = 1  # Se não houver largura suficiente para 2 ruas, a rua ocupará toda a largura
    return ruas


# Função de menu principal
def menu():
    while True:
        print("\nMenu de opções:")
        print("1. Insira os dados relativos à sua cultura")
        print("2. Impressão de dados")
        print("3. Atualizar dados")
        print("4. Deletar dados")
        print("5. Menu de insumos")
        print("6. Sair do programa")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            print("\nEscolha a cultura:")
            print("1. Soja")
            print("2. Milho")
            opcao_cultura = int(input("Digite o número da cultura desejada: "))

            if opcao_cultura == 1:
                cultura = 'soja'
            elif opcao_cultura == 2:
                cultura = 'milho'
            else:
                print("Opção de cultura inválida!")
                continue

            area, largura, comprimento, ruas = calcular_area(cultura)
            if area == 0:
                continue
            print(f"Você possui uma área de {area:.2f} m2 com {ruas} ruas.")
            print(f"Para plantar nessa área, você precisa de:")

            insumos_desejados = inserir_insumos(cultura)
            insumos_detalhados = calcular_insumos(area, cultura, insumos_desejados)

            for tipo, quantidade in insumos_detalhados.items():
                unidade = unidades_medidas[cultura].get(tipo, 'g/m2')
                print(f" * {quantidade:.2f} {unidade} de {tipo}")

            areas.append(area)
            larguras.append(largura)
            comprimentos.append(comprimento)
            insumos.append(insumos_detalhados)
            culturas_plantadas.append(cultura)
            numero_ruas.append(ruas)

        elif opcao == 2:
            if areas:
                imprimir_tabela()
            else:
                print("Nenhum dado de área ou insumo foi inserido.")

        elif opcao == 3:
            if areas:
                imprimir_tabela()
                posicao = int(input(f"Digite o número da área a ser atualizada (1 a {len(areas)}): ")) - 1
                if 0 <= posicao < len(areas):
                    atualizar_dados(posicao)
                else:
                    print("Número da área inválido.")
            else:
                print("Nenhum dado de área foi inserido.")

        elif opcao == 4:
            if areas:
                imprimir_tabela()
                posicao = int(input(f"Digite o número da área a ser deletada (1 a {len(areas)}): ")) - 1
                if 0 <= posicao < len(areas):
                    areas.pop(posicao)
                    larguras.pop(posicao)
                    comprimentos.pop(posicao)
                    insumos.pop(posicao)
                    culturas_plantadas.pop(posicao)
                    numero_ruas.pop(posicao)
                else:
                    print("Número da área inválido.")
            else:
                print("Nenhum dado de área foi inserido.")

        elif opcao == 5:
            menu_insumos()

        elif opcao == 6:
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida!")


# Listas para armazenar dados das culturas
culturas_plantadas = []
areas = []
larguras = []
comprimentos = []
insumos = []
numero_ruas = []

# Início do menu principal
menu()
