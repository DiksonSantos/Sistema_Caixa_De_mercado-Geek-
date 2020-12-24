from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()

def menu() -> None:
    print(30*'=')
    print(25*'=', 'Bem Vindo', 25*'=')
    print(25*'=', 'Shopping_Virtual', 25*'=')
    print(40*'=')

    print('Selecione Uma Opção a Baixo')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produto')
    print('3 - Comprar Produto')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar Pedido')
    print('6 - Sair Do Sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte Sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção Invalida')
        sleep(2)
        menu()

def cadastrar_produto() -> None:
    print('Cadastrar Produto')
    print(20*'=')

    nome: str = input('Informe Nome Do Produto: ')
    preco: float = float(input('Informe o Preço do Produto: '))


    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O Produto {produto.nome} Foi Cadastrado Com Sucesso!')
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de Produtos')
        print(30*'--')
        for produto in produtos:
            print(produto)
            print(30*'-')
            sleep(1)

    else:
        print('Produtos Ainda Não Cadastrados.')
    sleep(2)

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe Codigo Do Produto')
        print(15*'==', 'Produtos Disponiveis', 15*'==')
        for produto in produtos:
            print(produto)
            print(30*'=')
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_Carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto) #GET pega p valor da chave (produto) [Dicionario]
                    if quant:
                        item[produto] = quant + 1
                        print(f'O Produto {produto.nome} agora possui {quant + 1} Unidade no Carrinho')
                        tem_no_Carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_Carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi add ao carrinho')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} Foi Adicionado ao Carrinho')
        else:
            print(f'o Produto com o codigo {codigo} Não foi encontrado')
            sleep(2)
            menu()



    else:
        print('Ainda Não existem Produtos')
        sleep(2)
        menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos do Carrinho')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print(20*'-')
                sleep(1)
    else:
        print('Ainda Não tem nada no carrinho')
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        print('Produtos do Carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1] #Preço[0] * Quantidade[1]
                print(20*'-')
                sleep(1)

        print(f'Sua Fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte Sempre')
        carrinho.clear() #Limpa Carrinho
        sleep(5)

    else:
        print('Ainda Não Ha produtos No Carrinho')

def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()

