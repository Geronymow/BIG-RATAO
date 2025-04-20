from menu import mostrar_menu
from pedido import add_item, mostrar_pedido, finalizar, remover_item

def console():
    print("BEM VINDO!!")
    print("1 - Ver cardápio")
    print("2 - Adicionar item ao pedido")
    print("3 - Ver pedido")
    print("4 - Finalizar pedido")
    print("5 - Remover item do pedido")
    print("0 - Sair\n")

def switch_case(desc):
    if desc == 1:
        mostrar_menu()
        print()
    elif desc == 2:
        add_item()
    elif desc == 3:
        mostrar_pedido()
    elif desc == 4:
        finalizar()
    elif desc == 5:
        remover_item()
    else:
        print("Opção inválida!\n")
