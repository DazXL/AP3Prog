class Motocicleta:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
class MotocicletaD:
    def __init__(self):
        self.motocicletas = []

    def criar_motocicleta(self, marca, modelo, ano):
        motocicleta = Motocicleta(marca, modelo, ano)
        self.motocicletas.append(motocicleta)
        f = open('moto.txt', 'a')
        f.write(f'Marca: {motocicleta.marca.upper()} ')
        f.write(f'Modelo: {motocicleta.modelo.upper()} ')
        f.write(f'Ano: {motocicleta.ano.upper()}\n')
        f.close()
        print("Motocicleta foi criada com êxito!")

    def listar_motocicletas(self):
        if len(self.motocicletas) == 0:
            print("Não há motocicletas cadastradas.")
        else:
            print("Motocicletas cadastradas:")
            for motocicleta in self.motocicletas:
                print(f"Marca: {motocicleta.marca}, Modelo: {motocicleta.modelo}, Ano: {motocicleta.ano}")


    # lista alternativa
    def alt_listar_motocicletas(self):
        print('Lista de Motos')
        f = open('moto.txt', 'r')
        for x in f:
            print(x)

    def atualizar_motocicleta(self, indice, marca, modelo, ano):
        if indice >= 0 and indice < len(self.motocicletas):
            motocicleta = self.motocicletas[indice]
            motocicleta.marca = marca
            motocicleta.modelo = modelo
            motocicleta.ano = ano
            print("Motocicleta atualizada com êxito!")
        else:
            print("Índice inválido!")

    def excluir_motocicleta(self, indice):
        if indice >= 0 and indice < len(self.motocicletas):
            motocicleta = self.motocicletas.pop(indice)
            print(f"Motocicleta '{motocicleta.marca} {motocicleta.modelo}' foi excluída com sucesso!")
        else:
            print("Índice inválido!")

    def alt_excluir_moto(self):
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

'''dao = MotocicletaD()
dao.criar_motocicleta('honda', 'cbm', 2020)
dao.listar_motocicletas()'''