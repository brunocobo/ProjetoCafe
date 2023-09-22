from Students_class.StudentService import StudentService
from functions.functions import Functions


class MenuStudents:

    def __init__(self):
        # Inicializa uma instância de StudentService para gerenciar operações relacionadas a estudantes.
        self.students_instance = StudentService()

    def manage_students(self):
        # Exibe um menu de gerenciamento de estudantes.
        while True:
            print("=" * 50)
            print("VOCÊ ESTÁ NO MENU DE ESTUDANTES".center(50, "="))
            print("=" * 50)
            print(
                "(1) Incluir Estudante\n"
                "(2) Listar Estudante\n"
                "(3) Atualizar Estudante\n"
                "(4) Excluir Estudante\n"
                "(5) Voltar ao menu principal\n"
            )
            option = input("DIGITE A OPÇÃO DESEJADA: ")

            if option == "1":
                # Chama o método para adicionar um estudante.
                self.add_student()

            elif option == "2":
                # Chama o método para listar os estudantes.
                self.list_students()

            elif option == '3':
                # Chama o método para atualizar informações de um estudante.
                self.update_students()

            elif option == '4':
                # Chama o método para excluir um estudante.
                self.exclude_students()

            elif option == "5":
                # Retorna ao menu principal.
                break
            else:
                # Exibe uma mensagem de opção inválida.
                Functions.show_invalid_option()

    def add_student(self):
        # Chama o método de adição de estudante da instância de StudentService.
        self.students_instance.add_student()

    def list_students(self):
        # Chama o método de listagem de estudantes da instância de StudentService.
        self.students_instance.list_students()

    def update_students(self):
        # Chama o método de atualização de estudantes da instância de StudentService.
        self.students_instance.update_students()

    def exclude_students(self):
        # Chama o método de exclusão de estudante da instância de StudentService.
        self.students_instance.exclude_students()
