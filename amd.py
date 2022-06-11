import sqlite3
import bibliotecaDB

def chamaAdm():
    opc = 1
    while opc != 5:
        print('-----------------------')
        print('1- Cadastrar Produto')
        print('2- Repor Estoque')
        print('3- Remover Produto')
        print('4- Listar Produtos')
        print('5- Sair')
        opc = int(input('Digite uma opção: '))
        print('-----------------------')

        if opc == 1:
            bibliotecaDB.cadastrarProduto()
        elif opc == 2:
            bibliotecaDB.reporProduto()
        elif opc == 3:
            bibliotecaDB.removerProduto()
        elif opc == 4:
            bibliotecaDB.listaProdutos()
