# ============ ↳ 𐔌  PROJETO MENUTECH 𐔌 ==========
import os
os.system("cls")
import json

def salvar_item(cardapio):
    with open("cardapio.json", "w", encoding="utf-8") as arquivo:
        json.dump(cardapio, arquivo, ensure_ascii=False, indent=4)

def carregarCardapio():
    try:
        with open("cardapio.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    
cardapio = carregarCardapio() 
mesas = []

while True:
    os.system("cls")
    print("=" * 35)
    print(""" 
    MENU PRINCIPAL
          
    1- Adicionar item no cardápio 
    2- Consultar cardápio
    3- Registrar pedido da mesa
    4- Consultar pedido da mesa
    5- Fechar conta
    """)
    print("=" * 35)
    opcao = int(input("Digite o número da opção desejada: "))
    
    match opcao:
        case 1:
            os.system("cls")
            item = input("Digite o nome do produto: ").upper()
            preco = float(input("Insira o preço do produto: "))
            codigo = len(cardapio) + 1
            produto = {
                "item": item,
                "preco": preco,
                "codigo": codigo
            }
            cardapio.append(produto)
            salvar_item(cardapio)
            input("ENTER para voltar para o menu...")
        case 2:
            os.system("cls")
            print("ITENS CADASTRADOS: ")
            for item in cardapio:
                print(f"Nome do produto: {item["item"]} | COD: {item["codigo"]} | Preço: {item["preco"]}")
            input("ENTER para voltar para o menu...")
        case 3:
            ...
        case 4:
            ...
        case 5:
            ...
        case _:
            print("Digite uma opção válida!")
            opcao = int(input("Digite o número da opção desejada: "))