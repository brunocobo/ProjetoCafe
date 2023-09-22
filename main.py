# ALUNO: BRUNO MARTINS RODRIGUES COBO
# CURSO: Superior de Tecnologia em Big Data e Inteligência Analítica
# ATIVIDADE SOMATIVA 2

from Courses_class.MenuCourses import MenuCourses
from Professors_class.MenuProfessors import MenuProfessors
from Students_class.MenuStudents import MenuStudents
from functions.functions import Functions
from Classes_class.MenuClasses import MenuClasses
from Enrollment_class.MenuEnrollment import MenuEnrollment


class AcademicSystem:
    # Essa classe é sistema acadêmico principal.

    def __init__(self):
        # Inicializa instâncias de classes de menu
        self.classes_instance = MenuClasses()
        self.professors_instance = MenuProfessors()
        self.students_instance = MenuStudents()
        self.enrollment_instance = MenuEnrollment()
        self.courses_instance = MenuCourses()

    def main_menu(self):
        # O método main_menu exibe um menu principal e permite ao usuário escolher as opções.

        while True:
            print("=" * 50)
            print("VOCÊ ESTÁ NO MENU PRINCIPAL".center(50, "="))
            print("=" * 50)
            print(
                "(1) Gerenciar Estudantes\n"
                "(2) Gerenciar Professores\n"
                "(3) Gerenciar Disciplinas\n"
                "(4) Gerenciar Turmas\n"
                "(5) Gerenciar Matrículas\n"
                "(6) SAIR\n"
            )
            option = input("DIGITE A OPÇÃO DESEJADA: ")

            if option == "1":
                self.manage_students()
            # chama o método para gerenciar estudantes.

            elif option == "2":
                self.manage_professors()
            # chama o método para gerenciar professores.

            elif option == "3":
                self.manage_courses()
            # chama o método para gerenciar disciplinas.

            elif option == "4":
                self.manage_classes()
            # chama o método para gerenciar turmas.

            elif option == "5":
                self.manage_enrollment()
            # chama o método para gerenciar matrículas.

            elif option == "6":
                # exibe uma mensagem de despedida e encerra o programa.
                print("\nGoodbye, Hasta luego, Au revoir, Arrivederci, Até logo!")
                break
            else:
                # opção escolhida não for válida, chama a função para exibir uma mensagem de opção inválida.
                Functions.show_invalid_option()

    def manage_courses(self):
        self.courses_instance.manage_courses()
        # O método manage_courses chama a função de gerenciamento de disciplinas da instância de MenuCourses.

    def manage_enrollment(self):
        self.enrollment_instance.manage_enrollment()
    # Método para gerenciar matrículas. Chama a função correspondente na instância de MenuEnrollment.

    def manage_classes(self):
        self.classes_instance.manage_classes()
    # Método para gerenciar turmas. Chama a função correspondente na instância de MenuClasses.

    def manage_students(self):
        self.students_instance.manage_students()
    # Método para gerenciar estudantes. Chama a função correspondente na instância de MenuStudents.

    def manage_professors(self):
        self.professors_instance.manage_professors()
    # Método para gerenciar professores. Chama a função correspondente na instância de MenuProfessors.


if __name__ == "__main__":
    # Cria uma instância da classe AcademicSystem e inicia o menu principal.
    system = AcademicSystem()
    system.main_menu()

teste