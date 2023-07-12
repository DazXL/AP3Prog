def alt_excluir_moto():
    file = open('moto.txt', 'r')
    read = file.readlines()
    # print(read)
    indice_exclusao = []
    print(f'Lista de motos:')
    for x in read:
        print(f'{read.index(x)}: {x}')
        indice_exclusao.append(read.index(x))
        # print(indice_exclusao)
    print('Digite o número da moto a ser excluída:')
    digito = int(input())

    if read[digito]:
        print(f'{read[digito].strip()} foi escolhido')
        print(f'deseja excluir? s/n')
        resposta = str(input()).lower()
        # print(resposta)
        if resposta == 's':
            read.pop(digito)
            indice_exclusao.pop()
            # print(indice_exclusao)
            print(f'entrada excluída')
            # print(read)
            f = open('moto.txt', 'w')
            # print(len(read))
            for x in indice_exclusao:

                f.write(f'{read[x].strip()}\n')
        elif resposta == 'n':
            print(f'Exclusão cancelada!')
            return
        else:
            print('resposta inválida')
            return

def alt_excluir_cliente():
    file = open('cliente.txt', 'r')
    read = file.readlines()
    # print(read)
    indice_exclusao = []
    print(f'Lista de clientes:')
    for x in read:
        print(f'{read.index(x)}: {x}')
        indice_exclusao.append(read.index(x))
        # print(indice_exclusao)
    print('Digite o número do cliente a ser excluído:')
    digito = int(input())

    if read[digito]:
        print(f'{read[digito].strip()} foi escolhido')
        print(f'deseja excluir? s/n')
        resposta = str(input()).lower()
        # print(resposta)
        if resposta == 's':
            read.pop(digito)
            indice_exclusao.pop()
            # print(indice_exclusao)
            print(f'entrada excluída')
            # print(read)
            f = open('cliente.txt', 'w')
            # print(len(read))
            for x in indice_exclusao:

                f.write(f'{read[x].strip()}\n')
        elif resposta == 'n':
            print(f'Exclusão cancelada!')
            return
        else:
            print('resposta inválida')
            return



alt_excluir_cliente()