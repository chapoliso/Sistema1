import sqlite3

def cadastrarProduto():
    prod = input('Nome: ')
    quant = int(input('Quantidade: '))
    preco = float(input('Valor: '))
    con = sqlite3.connect("meu_banco.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO produtos (nome, quantidade, valor) VALUES (?,?,?)", [prod, quant, preco])
    con.commit()
    con.close()

def reporProduto():
    cod = int(input('Qual o ID do produto? '))
    novaQuant = int(input('Quantidade para repor: '))
    con = sqlite3.connect("meu_banco.db")
    cursor = con.cursor()
    cursor.execute("UPDATE produtos SET quantidade = quantidade + ? WHERE id = ?", (novaQuant, cod))
    con.commit()
    con.close()

def removerProduto():
    cod = int(input('Digite o codigo do produto'))
    con = sqlite3.connect("meu_banco.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", [cod])
    con.commit()
    con.close()


def listaProdutos():
    print('LISTAR PRODUTOS')
    con = sqlite3.connect("meu_banco.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM produtos;")
    produto = cursor.fetchall()
    con.commit()
    con.close()
    for linha in produto:
        print("---------------")
        print('ID: ', linha[0])
        print('Nome: ', linha[1])
        print('Quantidade: ', linha[2])
        print('Preço: ', linha[3])


def cadastroCliente(valor, lista):
        if valor in lista:
            print('Login inválido!')
        else:
            lista.append(valor)

def compraProduto(valorCod, valorQuant):
    con = sqlite3.connect("meu_banco.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = ?;", [valorCod])
    produto = cursor.fetchone()
    cursor.execute("UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?", (valorQuant, valorCod))
    con.commit()
    con.close()
    return produto
 

def criaCarrinho(lista):
    carrinho = []
    carrinho.append(lista)
    print(carrinho)