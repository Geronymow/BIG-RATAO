menu = {
    1: ["x-lanchão", "refrigerante", "batata-frita", {"preco": 35.00}],
    2: ["x-frangão", "refrigerante", "batata-frita", {"preco": 20.00}],
    3: ["x-ratão", "refrigerante", "batata-frita", {"preco": 50.00}],
    4: ["x-vegetariano", "refrigerante", "batata-frita", {"preco": 30.00}],
    5: ["x-Peixão", "refrigerante", "batata-frita", {"preco": 25.00}],
    6: ["Lanche", {"preco": 15.00}],
    7: ["Refrigerante", {"preco": 15.00}],
    8: ["Batata", {"preco": 15.00}]
}

def mostrar_menu():
    for key, itens in menu.items():
        preco = None
        descricoes = []

        for item in itens:
            if isinstance(item, dict) and "preco" in item:
                preco = item["preco"]
            else:
                descricoes.append(item)

        descricao_str = ", ".join(descricoes)
        print(f"{key} -> {descricao_str}")
        print(f"Preço: R$ {preco:.2f}\n")
