class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print(f"O contato já existe")
        else:
            self.contatos[nome] = telefone
            print("Contato adicionado com sucesso")

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print("Contato removido com sucesso.")
        else:
            print("Contato não encontrado na agenda")

    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            print(f"Nome: {nome}, Telefone: {self.contatos[nome]}")
        else:
            print("O contato não foi encontrado")

    def listar_contatos(self):
        if self.contatos:
            print("Lista de Contatos:")
            for nome, telefone in self.contatos.items():
                print(f"Nome: {nome}, Telefone: {telefone}")
        else:
            print("Agenda vazia")


def menu():
    minha_agenda = AgendaTelefonica()
    while True:
        print("\nAgenda Telefonica")
        print("1-Adicionar contato")
        print("2-Remover contato")
        print("3-Pesquisar contato")
        print("4-Listar contatos")
        print("5-Sair do programa")
        opmenu = input("Escolha uma opção: ")

        if opmenu == '1':
            nome = input("Digite o nome: ")
            telefone = input("Diigite o telefone: ")
            minha_agenda.adicionar_contato(nome, telefone)
        elif opmenu == '2':
            nome = input("Digite o nome do contato que quer remover: ")
            minha_agenda.remover_contato(nome)
        elif opmenu == '3':
            nome = input("Digite o nome do contato: ")
            minha_agenda.pesquisar_contato(nome)
        elif opmenu == '4':
            minha_agenda.listar_contatos()
        elif opmenu == '5':
            print("Obrigado por utilizar a agenda")
            break
        else:
            print("Invalido, escolha um valor de 1 a 5.")


if __name__ == "__main__":
    menu()
