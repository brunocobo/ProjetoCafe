from functions.functions import Functions
from Enrollment_class.EnrollmentService import EnrollmentService


class MenuEnrollment:

    def __init__(self):
        self.enrollment_instance = EnrollmentService()

    def manage_enrollment(self):
        while True:
            print("=" * 50)
            print("VOCÊ ESTÁ NO MENU DE MATRÍCULAS".center(50, "="))
            print("=" * 50)
            print(
                "(1) Incluir Matrícula\n"
                "(2) Listar Matrículas\n"
                "(3) Atualizar Matrícula\n"
                "(4) Excluir Matrícula\n"
                "(5) Voltar ao menu principal\n"
            )
            option = input("DIGITE A OPÇÃO DESEJADA: ")

            if option == "1":
                self.add_enrollment()

            elif option == "2":
                self.list_enrollment()

            elif option == '3':
                self.update_enrollment()

            elif option == '4':
                self.exclude_enrollment()

            elif option == "5":
                break
            else:
                Functions.show_invalid_option()

    def add_enrollment(self):
        self.enrollment_instance.add_enrollment()

    def list_enrollment(self):
        self.enrollment_instance.list_enrollment()

    def update_enrollment(self):
        self.enrollment_instance.update_enrollment()

    def exclude_enrollment(self):
        self.enrollment_instance.exclude_enrollment()
