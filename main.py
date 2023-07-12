# import main
import lib.crudcliente
import lib.crudmoto
import lib.crudvenda
import lib.consultavenda
import sys
import datetime

# x = int
# z = int


def introducao():
    print('O que deseja fazer?\n')
    print('1 - Cadastro de Clientes')
    print('2 - Cadastro de Motos')
    print('3 - Venda de Moto')
    print('4 - Consultar vendas')
    print('0 - Encerrar')
    x = int(input())
    acesso(x)


def acesso(a):
    if a == 1:
        print('\nAcessando Cadastro de Clientes...\n')
        print('===============================')
        print('=====CADASTRO DE CLIENTES======')
        print('===============================\n')
        print('O que deseja fazer?\n')
        print('1 - Cadastro de Clientes')
        print('2 - Consulta de Clientes')
        print('3 - Exclusão de Clientes')
        print('0 - Retornar')
        z = int(input())
        if z == 1:
            print('cadastrando...')
            cadastro = lib.crudcliente.CadastroCliente()
            vnome = input('Digite o nome: ')
            vemail = input('Digite o e-mail: ')
            vtelefone = input('Digite o telefone: ')
            cadastro.criar_cliente(vnome, vemail, vtelefone)
            acesso(1)
        elif z == 2:
            print('consultando...')
            consulta = lib.crudcliente.CadastroCliente()
            consulta.alt_listar_clientes()
            input('pressione Enter para continuar')
            acesso(1)
        elif z == 3:
            print(f'Exclusão de clientes')
            excluir = lib.crudcliente.CadastroCliente()
            excluir.alt_excluir_cliente()
            input('pressione Enter para Continuar')
            acesso(1)
        elif z == 0:
            print('retornando\n')
            introducao()
        else:
            print('opção não encontrada\n')
            acesso(1)
    elif a == 2:
        print('\nAcessando Cadastro de Motos...\n')
        print('===============================')
        print('=======CADASTRO DE MOTOS=======')
        print('===============================\n')
        print('O que deseja fazer?\n')
        print('1 - Cadastro de Motos')
        print('2 - Consulta de Motos')
        print('3 - Excluir Motos')
        print('0 - Retornar')
        z = int(input())
        if z == 1:
            print('cadastrando...')
            cadastro = lib.crudmoto.MotocicletaD()
            vmarca = input('Digite a Marca: ')
            vmodelo = input('Digite o Modelo: ')
            vano = input('Digite o Ano: ')
            cadastro.criar_motocicleta(vmarca, vmodelo, vano)
            acesso(2)
        elif z == 2:
            print('consultando...')
            consulta = lib.crudmoto.MotocicletaD()
            consulta.alt_listar_motocicletas()
            input('pressione Enter para continuar')
            acesso(2)
        elif z == 3:
            print(f'Exclusão de motos')
            excluir = lib.crudmoto.MotocicletaD()
            excluir.alt_excluir_moto()
            input('pressione Enter para Continuar')
            acesso(2)
        elif z == 0:
            print('retornando\n')
            introducao()
        else:
            print('Opção não encontrada\n')
            acesso(2)
    elif a == 3:
        print('\nAcessando Venda de Motos...\n')
        print('===============================')
        print('=======VENDA DE MOTOS==========')
        print('===============================\n')
        print('O que deseja fazer?\n')
        print('1 - Vender Moto')
        print('0 - Retornar')
        z = int(input())

        if z == 1:
            # print('Opção em desenvolvimento!\n')
            vendendo = lib.crudvenda.Listar()
            vendendo.listanome()
            introducao()
        elif z == 0:
            print('retornando\n')
            introducao()

        else:
            print('Opção não encontrada\n')
            acesso(3)

    elif a == 4:
        print('\nAcessando Consulta de Vendas...\n')
        print('===============================')
        print('=======CONSULTA DE VENDAS======')
        print('===============================\n')
        print('O que deseja fazer?\n')
        print('1 - Buscar Vendas')
        print('2 - Listar Todas as Vendas')
        print('0 - Retornar')
        z = int(input())
        if z == 1:
            # print('Opção em desenvolvimento!\n')
            print('digite a MARCA ou um MODELO da moto')
            buscando = str(input()).upper()
            # print(buscando)
            listar = lib.consultavenda.Buscador()
            listar.busca(buscando)
            introducao()
        elif z == 2:
            f = open('venda.txt', 'r')
            for x in f:
                print(x)
            introducao()
        elif z == 0:
            print('retornando\n')
            introducao()
        else:
            print('Opção não encontrada\n')
            acesso(4)

    elif a == 0:
        print('Encerrando...')
        sys.exit()

    else:
        print('Opção não disponível, tente novamente\n')
        introducao()


print(' ___  ___  ___   ___   ___   _  _ ')
print('/ __||_ _|/ __| / __| / _ \ | \| |')
print('\__ \ | | \__ \| (__ | (_) || .  |')
print('|___/|___||___/ \___| \___/ |_|\_|\n')

print('Bem-vindo ao SISCON\n')
print('Versão beta de avaliação\n')
introducao()
