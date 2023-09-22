from Courses_class.CourseService import CourseService
from functions.functions import Functions


class MenuCourses:
    def __init__(self):
        self.courses_instance = CourseService()

    def manage_courses(self):
        while True:
            print("=" * 50)
            print("VOCÊ ESTÁ NO MENU DE DISCIPLINAS".center(50, "="))
            print("=" * 50)
            print(
                "(1) Incluir Disciplina\n"
                "(2) Listar Disciplinas\n"
                "(3) Atualizar Disciplina\n"
                "(4) Excluir Disciplina\n"
                "(5) Voltar ao menu principal\n"
            )
            option = input("DIGITE A OPÇÃO DESEJADA: ")

            if option == "1":
                self.add_courses()

            elif option == "2":
                self.list_courses()

            elif option == '3':
                self.update_courses()

            elif option == '4':
                self.exclude_courses()

            elif option == "5":
                break
            else:
                Functions.show_invalid_option()

    def add_courses(self):
        self.courses_instance.add_course()

    def list_courses(self):
        self.courses_instance.list_course()

    def update_courses(self):
        self.courses_instance.update_course()

    def exclude_courses(self):
        self.courses_instance.exclude_course()
