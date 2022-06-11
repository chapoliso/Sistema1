import sqlite3
import amd
import cliente
import bibliotecaDB
import os

Llogin = ['jl']

opcao = 1
while opcao != 3:
    print('-----------------------')
    print('1 - Entar')
    print('2 - Cadastrar')
    print('3 - Sair')
    opcao = int(input('Digite a opção desejada: '))
    print('-----------------------\n')
    os.system("clear")

    if opcao == 1:
        login = input("Login: ")
        if login == 'admin':
            amd.chamaAdm()
        else:
            if login in Llogin:
                cliente.chamaCliente()
            else:
                print('Não localizado! Verifique novamente!')
    elif opcao == 2:
        login = input('Digite o login: ')
        bibliotecaDB.cadastroCliente(login, Llogin)