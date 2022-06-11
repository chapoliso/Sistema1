import sqlite3
import bibliotecaDB
import os

def chamaCliente():
    opcao = 1
    while opcao != 4:
        print('-----------------------')
        print('1 - Comprar')
        print('2 - Carrinho')
        print('3 - Finalizar')
        print('4 - Sair')
        opcao = int(input('Digite a opção desejada: '))
        print('-----------------------\n')
        system("clear")

        if opcao == 1:
            cod = int(input('Código do produto: '))
            quant = int(input('Quantidade a ser comprada: '))
            compra = []
            montacompra = bibliotecaDB.compraProduto(cod, quant)
            for e in montacompra:
                compra.append(e)
            compra[2] = quant
            print(compra)
            
            
