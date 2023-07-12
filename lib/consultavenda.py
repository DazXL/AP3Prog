
class Buscador:
    def busca(self, listwords): #definindo a função de busca de vendas específicas

        try:
            file = open('venda.txt', 'r')  # abre o arquivo de vendas
            read = file.readlines()  # lê o conteúdo do arquivo
            file.close()  # fecha o arquivo
            copyread = read  # copia o conteúdo da lista read
            # print(f'copy:{copyread}')
            for linha in copyread:  # loop para ler cada linha da cópia da lista
                x = linha  # converte a linha para string
                if x.find(listwords) != -1:  # busca na string a palavra chave
                    print(f'{x.strip()}')  # imprime a linha correspondente
                    # copyread.pop(0)
                    # print(f'copy: {copyread}')

               # elif x.find(listwords) == -1:
                    #print('buscando...')
                    # copyread.pop(0)
                    # print(f'copy: {copyread}')
            print(f'\nConsulta encerrada.')
            print(f'Caso nenhum dado mostrado, nada foi encontrado\n')

        except FileExistsError:
            print('The file is not there ')


'''x = open('venda.txt', 'r')
consulta = x.readlines()
x.close()
'''
# for line in consulta:


# keyword = input('Digite o nome da moto: ')
# Buscador.busca('venda.txt', 'cbr')
