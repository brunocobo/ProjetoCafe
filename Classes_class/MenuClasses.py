from functions.functions import Functions
from Classes_class.ClasseService import ClassesService


class MenuClasses:
    def __init__(self):
        self.classes_instance = ClassesService()

    def manage_classes(self):
        while True:
            print("=" * 50)
            print("VOCÊ ESTÁ NO MENU DE TURMAS".center(50, "="))
            print("=" * 50)
            print(
                "(1) Incluir Turmas\n"
                "(2) Listar Turmas\n"
                "(3) Atualizar Turmas\n"
                "(4) Excluir Turmas\n"
                "(5) Voltar ao menu principal\n"
            )
            option = input("DIGITE A OPÇÃO DESEJADA: ")

            if option == "1":
                self.add_classes()

            elif option == "2":
                self.list_classes()

            elif option == '3':
                self.update_classes()

            elif option == '4':
                self.exclude_classes()

            elif option == "5":
                break
            else:
                Functions.show_invalid_option()

    def add_classes(self):
        self.classes_instance.add_classe()

    def list_classes(self):
        self.classes_instance.list_classe()

    def update_classes(self):
        self.classes_instance.update_classe()

    def exclude_classes(self):
        self.classes_instance.exclude_classe()

