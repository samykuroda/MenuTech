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
mesas = {}
 
while True:
    os.system("cls")
    print("=" * 35)
    print(""" 
    MENU PRINCIPAL
          
    1- Adicionar item no cardápio 
    2- Consultar cardápio
    3- Abrir mesa e adicionar pedido
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
            if not cardapio:
                print("Nenhum item cadastrado ainda.")
            else:
                for item in cardapio:
                    print(f"Nome do produto: {item['item']} | COD: {item['codigo']} | Preço: {item['preco']}")
            print()
            input("ENTER para voltar para o menu...")
        case 3:
            os.system('cls')
            num_mesa = int(input("Digite o número da mesa: "))
            
            if num_mesa not in mesas or mesas[num_mesa]["status"] == "fechada":
                mesas[num_mesa] = {
                        "status": "aberta",
                        "pedidos": [],
                        "total": 0.0
                    }
                print("Mesa aberta com sucesso!")
            else:
                print(f"Adicionando novos pedidos na Mesa {num_mesa} (já aberta).\n")
            
            while True:
                if len(cardapio) == 0:
                    print("O cardápio está vazio! Cadastre produtos no Menu 1 primeiro.")
                    input("Digite ENTER para voltar ao menu principal...")
                    break
 
                else:                
                    item_mesa = int(input("Digite o código do produto: "))
                    qtd = int(input("Quantidade: "))
                    item_encontrado = False
 
                    for item in cardapio:    
                        if item_mesa == item["codigo"]:
                            subtotal = item["preco"] * qtd
                                        
                            novo_item = {
                            "item": item["item"],
                            "preco": item["preco"],
                            "qtd": qtd,
                            "subtotal": subtotal
                    }
                            mesas[num_mesa]["pedidos"].append(novo_item)
                            mesas[num_mesa]["total"] += subtotal
                            print(f"-> Adicionado: {qtd} x {item['item']} (R$ {subtotal:.2f})")
                            item_encontrado = True
                            break
                        
                    if not item_encontrado:
                        print("Código de produto inválido!")
                    
                    continuar = input("\nDeseja adicionar mais itens nesta mesa? (s/n): ").lower()
                    if continuar != 's':
                        input("Digite ENTER para voltar ao menu")   
                        break  
        case 4:
            print(f"--- MESAS ABERTAS ---")
            mesa_aberta = False
            for numero, dados in mesas.items():
                if dados["status"] == "aberta":
                    mesa_aberta = True
                    print(f"\n--- MESA {numero} ---")
                    if len(dados["pedidos"]) == 0:
                        print("  (Nenhum pedido lançado)")
                    else:
                        for item in dados["pedidos"]:
                            print(f"  - {item['qtd']}x {item['item']} = R$ {item['subtotal']:.2f}")
                    print(f"  TOTAL: R$ {dados['total']:.2f}")
            if not mesa_aberta:
                print("\nNenhuma mesa aberta no momento.")
            print("==============================\n")
            input("Aperte ENTER para voltar ao menu")
 
        case 5:
            ...
        case _:
            print("Digite uma opção válida!")
            input("Aperte ENTER para continuar...")
 