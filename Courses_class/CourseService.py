import json
import os
from functions.functions import Functions
from tabulate import tabulate


class CourseService:

    def __init__(self):
        self.courses = []
        self.load_courses_from_file()

    def add_course(self):
        print('=' * 50)
        print('Adicionar Disciplina'.center(50, '='))
        print('=' * 50)

        functions_instance = Functions()
        while True:
            new_course = {
                'course': str(input('Digite o nome da disciplina: ').strip().upper()),
                'code': int(functions_instance.get_valid_input('Digite o código da disciplina: ', str.isdigit)),
            }

            if not any(
                    course['course'] == new_course['course'] or
                    course['code'] == new_course['code'] for course in self.courses
            ):
                self.courses.append(new_course)
                self.save_courses_to_file()
                print('=' * 50)
                print('\nDados válidos!\n'
                      'Disciplina cadastrada com sucesso!')
                print('=' * 50)
            else:
                print('=' * 50)
                if any(course['course'] == new_course['course'] for course in self.courses):
                    print('Nome já cadastrado!')
                if any(course['code'] == new_course['code'] for course in self.courses):
                    print('Código já cadastrado!')
                print('Tente novamente!\n')
                print('=' * 50)

            if not Functions.should_continue():
                break

    def list_course(self):
        print('=' * 50)
        print('Lista de Disciplinas Cadastradas'.center(50, '='))
        print('=' * 50)

        # para caregar as innformações mais recentes
        self.load_courses_from_file()

        if not self.courses:
            print('Sem disciplinas cadastradas')
        else:
            table_data = []
            for course in self.courses:
                course_name = course['course']
                course_code = course['code']

                table_data.append([course_code, course_name])

            headers = ['Código', 'Nome Disciplina']
            print(tabulate(table_data, headers=headers, tablefmt='fancy_grid'))

        print('=' * 50)

    def update_course(self):
        while True:
            print('=' * 50)
            print('Atualizar Disciplina'.center(50, '='))
            print('=' * 50)

            search_term = str(input('Digite o nome da disciplina: ').strip().upper())

            found_courses = [course for course in self.courses if search_term in course['course']]

            if not found_courses:
                print('Disciplina não encontrada na base de dados')
                if not Functions.should_continue():
                    break
                continue

            print('***' * 15)
            print('Disciplina Encontrada')
            for idx, course in enumerate(found_courses, start=1):
                print(f"({idx}) Disciplina: {course['course'].upper()}, Código: {course['code']}")
                print('***' * 15)
            try:
                code_to_search = int(input("\nDigite o código da disciplina: ").strip())

            except ValueError:
                print('Código Inválido!')
                continue

            select_course = next((course for course in found_courses if code_to_search == course['code']), None)

            if select_course:
                self.update_course_info(select_course)
                if not Functions.should_continue():
                    break
            else:
                print(f'Nenhuma disciplina com o código \'{code_to_search}\' foi encontrada')

    def update_course_info(self, course):

        while True:
            print('=' * 50)
            print(f"\nAtualizando Informações para a Disciplina: {course['course'].upper()}")

            try:
                rep = int(input('\nQual informação deseja atualizar:\n'
                                'Digite 1 para nome da Disciplina\n'
                                'Digite 2 para código da Disicplina\n'
                                '\nQual opção deseja?: ').strip())
                if rep == 1:
                    print('=' * 50)
                    print('Você selecionou nome da diciplina!'.center(50, '='))
                    print('=' * 50)
                    course['course'] = input('\nDigite o novo nome da disciplina: ').strip().lower()
                    break

                elif rep == 2:
                    print('=' * 50)
                    print('Você selecionou Código!'.center(50, '='))
                    print('=' * 50)
                    course['code'] = int(input('\nDigite o novo código: '))
                    break

                else:
                    print('Opção inválida. Digite uma opção válida')

            except ValueError:
                print('Opção inválida. Digite um número válido.')

        self.save_courses_to_file()
        print('=' * 50, '\nInformação atualizada com sucesso!\n')

    def exclude_course(self):
        print('=' * 50)
        print('Você selecionou Excluir Disciplina'.center(50, '='))
        print('=' * 50)

        while True:
            search_term = input('\nDigite o nome da disciplina a ser excluída: ').strip().upper()

            if not search_term:
                continue
            # course_to_remove = [course for course in self.courses if search_term in course['course']]
            course_to_remove = [course for course in self.courses if search_term == course['course']]

            if course_to_remove:
                for course in course_to_remove:
                    self.courses.remove(course)
                self.save_courses_to_file()
                print('\n', '=' * 50)
                print(f"Disciplina: '{search_term}' excluída com sucesso!")
                print('\n', '=' * 50)

            else:
                print('=' * 50)
                print(
                    f'Não encontrei nenhuma disciplina com o nome: \'{search_term}\'\n'
                    'Tente digitar um nome válido ou verifique a lista de disciplinas!\n')

            continue_deleting = input('Deseja continuar excluindo? [S/N]: ').strip().lower()
            if continue_deleting != 's':
                break

    def save_courses_to_file(self):
        output_dir = "./List/"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open('./List/courses_data.json', 'w', encoding="utf-8") as file:
            json.dump(self.courses, file, indent=4, ensure_ascii=False)

    def load_courses_from_file(self):
        try:
            with open("./List/courses_data.json", 'r', encoding="utf-8") as file:
                data = file.read()
                if data:
                    self.courses = json.loads(data)
                else:
                    self.courses = []
        except FileNotFoundError:
            self.courses = []
