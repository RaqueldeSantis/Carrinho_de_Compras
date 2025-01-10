# Inicializa uma lista vazia para o carrinho de compras
carrinho = []

# Loop para adicionar itens ao carrinho
while True:
    item = input("Adicione um item ao carrinho (ou digite 'sair' para finalizar): ")

    if item.lower() == 'sair':
        break  # Sai do loop se o usuário digitar 'sair'

    carrinho.append(item)  # Adiciona o item ao carrinho

# Exibe os itens do carrinho de compras
print("\nItens no carrinho de compras:")
for i, item in enumerate(carrinho, start=1):
    print(f"{i}. {item}")
