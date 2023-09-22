from Professors_class.ProfessorService import ProfessorService
from functions.functions import Functions


class MenuProfessors:

    def __init__(self):
        # Inicializa uma instância de MenuProfessors com uma instância de ProfessorService.
        self.professors_instance = ProfessorService()

    def manage_professors(self):
        # Função para gerenciar professores.
        while True:
            print('=' * 50)
            print('VOCÊ ESTÁ NO MENU DE PROFESSORES'.center(50, '='))
            print('=' * 50)
            print(
                '(1) Incluir Professor\n'
                '(2) Listar Professor\n'
                '(3) Atualizar Professor\n'
                '(4) Excluir Professor\n'
                '(5) Voltar ao Menu Principal\n'
            )
            option = input('DIGITE A OPÇÃO DESEJADA: ')
            if option == '1':
                # Chama o método para adicionar um professor.
                self.add_professor()

            elif option == '2':
                # Chama o método para listar os professores.
                self.list_professor()

            elif option == '3':
                # Chama o método para atualizar informações de um professor.
                self.update_professor()

            elif option == '4':
                # Chama o método para excluir um professor.
                self.exclude_professor()

            elif option == '5':
                # Retorna ao menu principal.
                break
            else:
                # Exibe uma mensagem de opção inválida.
                Functions.show_invalid_option()

    def exclude_professor(self):
        # Chama o método para excluir um professor da instância de ProfessorService.
        self.professors_instance.exclude_professor()

    def update_professor(self):
        # Chama o método para atualizar informações de um professor da instância de ProfessorService.
        self.professors_instance.update_professor()

    def list_professor(self):
        # Chama o método para listar os professores da instância de ProfessorService.
        self.professors_instance.list_professor()

    def add_professor(self):
        # Chama o método para adicionar um professor da instância de ProfessorService.
        self.professors_instance.add_professor()
