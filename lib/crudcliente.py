''''
'r' usado para ler algo
'w' usado apra escrever algo
'r+' usado para ler e escrever algo
'a' usado para acrescentar algo

'''


class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone


class CadastroCliente:
    def __init__(self):
        self.clientes = []

    def criar_cliente(self, nome, email, telefone):
        novo_cliente = Cliente(nome, email, telefone)
        self.clientes.append(novo_cliente)
        f = open('cliente.txt', 'a')
        f.write(f'Nome: {novo_cliente.nome} ')
        f.write(f'e-mail: {novo_cliente.email} ')
        f.write(f'telefone: {novo_cliente.telefone}\n')
        f.close()
        print('Cliente foi criado com sucesso!')

    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in self.clientes:
                print(f"Nome: {cliente.nome}, Email: {cliente.email}, Telefone: {cliente.telefone}")

    #lista alternativa
    def alt_listar_clientes(self):
        print('Lista de Clientes')
        f = open('cliente.txt', 'r')
        for x in f:
            print(x)

    def buscar_cliente(self, nome):
        for cliente in self.clientes:
            if cliente.nome == nome:
                print(f"Nome: {cliente.nome}, Email: {cliente.email}, Telefone: {cliente.telefone}")
                return
        print("Cliente não encontrado.")

    def atualizar_cliente(self, nome, novo_email, novo_telefone):
        for cliente in self.clientes:
            if cliente.nome == nome:
                cliente.email = novo_email
                cliente.telefone = novo_telefone
                print("Cliente atualizado com sucesso!")
                return
        print("Cliente não encontrado.")

    def excluir_cliente(self, nome):
        for cliente in self.clientes:
            if cliente.nome == nome:
                self.clientes.remove(cliente)
                print("Cliente excluído com sucesso!")
                return
        print("Cliente não encontrado.")

    def alt_excluir_cliente(self):
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


'''# Exemplo de uso
cadastro = CadastroCliente()

# Criar clientes
cadastro.criar_cliente("Gustavo", "gustavo@email.com", "1267856")
cadastro.criar_cliente("Ana", "ana@email.com", "6455321")

# Listar clientes
cadastro.listar_clientes()

# Buscar cliente
cadastro.buscar_cliente("Gustavo")

# Atualizar cliente
cadastro.atualizar_cliente("Gustavo", "novoemail@email.com", "969504")

# Excluir cliente
cadastro.excluir_cliente("Ana")

# Listar clientes novamente para verificar as alterações
cadastro.listar_clientes()

# arquivo = open('texto.txt')
# with open('texto.txt') as file:
#    print(file.read)
# arquivo.close()'''



