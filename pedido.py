from menu import menu

pedido = []

def add_item():
    escolha = int(input("Digite o código do pedido que deseja adicionar (ou '0' para voltar): "))
    if escolha == 0:
        return
    if escolha in menu:
        pedido.append(menu[escolha]) 
        print("Pedido adicionado com sucesso!\n")
    else:
        print("Código inválido! Digite outro\n")

def mostrar_pedido():
    if not pedido:
        print("Nenhum item no pedido.\n")
        return

    total = 0.0
    print("Seu pedido até agora:\n")
    for item in pedido:
        preco = None
        descricoes = []

        for i in item:
            if isinstance(i, dict) and "preco" in i:
                preco = i["preco"]
                total += preco
            else:
                descricoes.append(i)

        descricao_str = ", ".join(descricoes)
        print(f"{descricao_str}")
        print(f"Preço: R$ {preco:.2f}\n")

    print(f"Total: R$ {total:.2f}\n")

def remover_item():
    if not pedido:
        print("Nenhum item para remover.\n")
        return
    
    escolha = int(input("\nDigite o número do item que deseja remover (ou 0 para cancelar): "))
    if escolha == 0:
        return
    if escolha <= len(pedido):
        removido = pedido.pop(escolha - 1)
        descricoes_removido = [i for i in removido if not isinstance(i, dict)]
        print(f"Item '{', '.join(descricoes_removido)}' removido com sucesso!\n")
    else:
        print("Número inválido.\n")

def finalizar():
    mostrar_pedido()
    print("Pedido finalizado.\nObrigado pela preferência!")
    exit()
