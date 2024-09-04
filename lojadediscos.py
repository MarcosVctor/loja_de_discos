
def adicionar_disco(loja):
    """
    Adiciona um novo disco à loja.
    """
    titulo = input("Digite o título do disco: ")
    artista = input("Digite o nome do artista: ")
    loja.append({"titulo": titulo, "artista": artista, "disponivel": True})
    print("Disco adicionado com sucesso!")

def listar_discos(loja):
    """
    Lista todos os discos na loja com seu status.
    """
    if not loja:
        print("Nenhum disco na loja.")
        return
    
    print("\nDiscos na Loja:")
    for i, disco in enumerate(loja, start=1):
        status = "Disponível" if disco["disponivel"] else "Vendido"
        print(f"{i}. {disco['titulo']} por {disco['artista']} - {status}")

def vender_disco(loja):
    """
    Permite vender um disco se estiver disponível.
    """
    listar_discos(loja)
    if not loja:
        return
    
    try:
        indice = int(input("\nDigite o número do disco que deseja vender: ")) - 1
        if loja[indice]["disponivel"]:
            loja[indice]["disponivel"] = False
            print(f"Você vendeu o disco: {loja[indice]['titulo']} por {loja[indice]['artista']}")
        else:
            print("Este disco já foi vendido.")
    except (IndexError, ValueError):
        print("Escolha inválida.")

def main():
    loja = []
    while True:
        print("\n1. Adicionar Disco")
        print("2. Listar Discos")
        print("3. Vender Disco")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_disco(loja)
        elif opcao == '2':
            listar_discos(loja)
        elif opcao == '3':
            vender_disco(loja)
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
