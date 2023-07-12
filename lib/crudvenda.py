import datetime


class Listar:
    def __init__(self):
        self.nome = ''
        self.moto = ''

    def listanome(self):

        try:
            buscacliente = open('cliente.txt', 'r')
            readcliente = buscacliente.readlines()
            buscacliente.close()
            copiacliente = readcliente
            indicecliente = []
            # print(copiacliente)
            # print(len(copiacliente))

            print('Lista de clientes:\n')
            for linha in copiacliente:
                print(f'{copiacliente.index(linha)} - {linha}')
                indicecliente.append(copiacliente.index(linha))
                # print(indicecliente)

            print('Digite o número do cliente irá vender a moto: ')
            numcliente = int(input())
            # print(f'{copiacliente[numcliente]} foi escolhido')
            #print(numcliente)

            if copiacliente[numcliente]:
                print(f'{copiacliente[numcliente].strip()} foi escolhido\n')
                escolhidocliente = copiacliente[numcliente].strip()
                #print(escolhidocliente)
                Listar.nome = escolhidocliente
                Listar.listamotos()

            '''else:
                print(copiacliente[numcliente])
                print(f'{copiacliente[numcliente]} foi escolhorido')'''
        except:
            print('número de cliente inválido\n')
            # print('file not found')
            Listar.listanome()

    def listamotos():
        buscamoto = open('moto.txt', 'r')
        readmoto = buscamoto.readlines()
        buscamoto.close()
        copiamoto = readmoto
        indicemoto = []
        print('Lista de motos:\n')
        for linha2 in copiamoto:
            print(f'{copiamoto.index(linha2)} - {linha2}')
            indicemoto.append(copiamoto.index(linha2))
            # print(indicemoto)

        print('Digite o número da moto que irá ser vendida: ')
        nummoto = int(input())
        # print('f{copiamoto[nummoto]} foi escolhido')

        if copiamoto[nummoto]:
            print(f'{copiamoto[nummoto].strip()} foi escolhido\n')
            escolhidomoto = copiamoto[nummoto].strip()
            #print(escolhidomoto)
            Listar.moto = escolhidomoto
            Listar.vendavai()
        else:
            print('número de moto inválido\n')
            # print('file not found')
            Listar.listamotos()

    def vendavai():
        data = datetime.datetime.now()
        print(f'deseja concluir venda? s/n')
        x = input().upper()
        if x == 'S':
            abrevenda = open('venda.txt', 'a')
            abrevenda.write(f'A moto {Listar.moto} foi vendida para {Listar.nome} em {data}\n')
            print(f'A moto {Listar.moto} foi vendida para {Listar.nome} em {data}\n')
            print('Venda concluída com sucesso!\n')
            abrevenda.close()
        elif x == 'N':
            print('Venda Cancelada\n')
            return

# Listar.listanome()
