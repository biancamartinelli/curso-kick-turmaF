estoque_produtos = {}

def cadastrar_produto():
    codigo = input("Digite um código de produto: ")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    estoque_produtos[codigo] = produto
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    """
    Lista os produtos do dicionário
    """
    print("Lista de Produtos:")
    for codigo, produto in estoque_produtos.items():
        print(f"Código: {codigo}, Nome: {produto['nome']}, preço: {produto['preco']}")
    
def buscar_produto():
    codigo = input("Digite o código: ")

    if codigo in estoque_produtos:
        produto = estoque_produtos[codigo]
        print(f"Código: {codigo}, Nome: {produto['nome']}, preço: {produto['preco']}, quantidade: {produto['estoque']}")
    else:
        print("Produto não encontrado")

def atualizar_produto():
    codigo = input("Digite o código: ")
    
    if codigo in estoque_produtos:
        produto = estoque_produtos[codigo]
        print("Atualizando...")
        
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        estoque = int(input("Digite a quantidade em estoque: "))

        produto['nome'] = nome
        produto['preco'] = preco
        produto['estoque'] = estoque
        
        print("Atualizando...")
    else:
        print("Não encontrado")
        
def excluir_produto():
    codigo = input("Digite o código: ")
    
    if codigo in estoque_produtos:
        del estoque_produtos[codigo]
        print("Produto deletado")
    else:
        print("Não encontrado")
    
        
    
def main():
    while True:
        print("\nSistema lanchonete")
        print("1. Cadastrar produtos")
        print("2. Listar produtos")
        print("3. Burcar produtos")
        print("4. Atualizar produtos")
        print("5. Sair")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            cadastrar_produto()
        elif escolha == 2:
            listar_produtos()
        elif escolha == 3:
            buscar_produto()
        elif escolha == 4:
            atualizar_produto()
        elif escolha == 5:
            print("Saindo do programa...")
            break

if __name__ == "__main__":
    main()