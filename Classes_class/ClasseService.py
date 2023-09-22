import json
import os
from functions.functions import Functions
from tabulate import tabulate


class ClassesService:
    def __init__(self):
        self.classes = []
        self.courses = []
        self.professors = []
        self.load_classes_from_file()
        self.load_professors_from_file()
        self.load_courses_from_file()

    def add_classe(self):
        print('=' * 50)
        print('Adicionar Turmas'.center(50, '='))
        print('=' * 50)

        functions_instance = Functions()

        class_code = int(functions_instance.get_valid_input('Digite o código da turma: ', str.isdigit))

        # para verificarse o código da turma já existe nas classes existentes
        if any(classe['class_code'] == class_code for classe in self.classes):
            print(f'Turma com código {class_code} já existe.')
            return

        # soliciar ao usuário que selecione um professor existente
        print('Professores disponíveis:')
        professors_table = [[professor['code'], professor['name']] for professor in self.professors]
        print(tabulate(professors_table, headers=['Código', 'Nome'], tablefmt='pretty'))

        professor_code = int(functions_instance.get_valid_input('Digite o código do professor da turma: ', str.isdigit))

        # para verificar se o código do professor existe na lista de professores
        selected_professor = next((professor for professor in self.professors if professor['code'] == professor_code),
                                  None)
        if not selected_professor:
            print(f'Professor com código {professor_code} não encontrado.')
            return

        # solicitar ao usuário que selecione uma disciplina existente
        print('Disciplinas disponíveis:')
        courses_table = [[course['code'], course['course']] for course in self.courses]
        print(tabulate(courses_table, headers=['Código', 'Disciplina'], tablefmt='pretty'))

        while True:
            discipline_code = int(
                functions_instance.get_valid_input('Digite o código da disciplina da turma: ', str.isdigit))

            # verificar se o código da disciplina existe na lista de disciplinas
            selected_discipline = next((course for course in self.courses if course['code'] == discipline_code), None)
            if selected_discipline:
                break  # sai do loop se o código for válido

            print(f'Disciplina com código {discipline_code} não encontrada. Tente novamente.')

        new_classe = {
            'class_code': class_code,
            'professor': selected_professor['name'],
            'discipline': selected_discipline['course']
        }

        self.classes.append(new_classe)
        self.save_classes_to_file()
        print('=' * 50)
        print('Turma adicionada com sucesso!')
        print('=' * 50)

    def list_classe(self):
        print('=' * 50)
        print('Lista de Turmas Cadastradas'.center(50, '='))
        print('=' * 50)

        # para carregar as informações mais recentes
        self.load_classes_from_file()

        if not self.classes:
            print('Sem turmas cadastradas.')
        else:
            table_data = []
            for classe in self.classes:
                class_code = classe['class_code']
                professor_name = classe['professor']
                discipline_name = classe['discipline']

                table_data.append([class_code, professor_name, discipline_name])

            headers = ['Código da Turma', 'Nome do Professor', 'Nome da Disciplina']
            print(tabulate(table_data, headers=headers, tablefmt='fancy_grid'))

        print('=' * 50)

    def update_classe(self):
        print('=' * 50)
        print('Atualizar Turma'.center(50, '='))
        print('=' * 50)

        while True:
            class_code_input = input('Digite o código da turma a ser atualizada: ')

            # Verificar se a entrada é um número inteiro válido
            if not class_code_input.isdigit():
                print('Por favor, digite um código de turma válido.')
            else:
                class_code = int(class_code_input)
                break

        for classe in self.classes:
            if classe['class_code'] == class_code:
                # solicitar ao usuário os novos códigos do professor e da disciplina
                new_professor_code = int(input('Digite o novo código do professor: '))
                new_discipline_code = int(input('Digite o novo código da disciplina: '))

                # para encontrar o professor e a disciplina correspondentes aos novos códigos
                selected_professor = next(
                    (professor for professor in self.professors if professor['code'] == new_professor_code), None)
                selected_discipline = next((course for course in self.courses if course['code'] == new_discipline_code),
                                           None)

                # verifica se o professor e a disciplina foram encontrados
                if selected_professor and selected_discipline:
                    # atualizar informações da turma com os novos códigos do professor e da disciplina
                    classe['professor_code'] = new_professor_code
                    classe['discipline_code'] = new_discipline_code

                    self.save_classes_to_file()

                    print('=' * 50)
                    print('Informações da turma atualizadas com sucesso!')
                    print('=' * 50)
                    return
                else:
                    print('Professor ou disciplina com os novos códigos não encontrados.')
                    return

        print('=' * 50)
        print('Não encontrei essa turma, vamos voltar ao menu '
              '\nanterior para que você possa listar as turmas,'
              '\né só selecionar a opção (2).')
        print('=' * 50)

    def exclude_classe(self):
        print('=' * 50)
        print('Excluir Turma'.center(50, '='))
        print('=' * 50)

        class_code = int(input('Digite o código da turma a ser excluída: '))

        for classe in self.classes:
            if classe['class_code'] == class_code:
                self.classes.remove(classe)
                self.save_classes_to_file()
                print('=' * 50)
                print(f'Turma com código {class_code} excluída com sucesso!')
                print('=' * 50)
                return

        print('Turma não encontrada.')

    def load_classes_from_file(self):
        try:
            with open('./List/classes_data.json', 'r', encoding='utf-8') as file:
                self.classes = json.load(file)
        except FileNotFoundError:
            self.classes = []

    def load_professors_from_file(self):
        try:
            with open('./List/professor_data.json', 'r', encoding='utf-8') as file:
                self.professors = json.load(file)

        except FileNotFoundError:
            self.professors = []

    def load_courses_from_file(self):
        try:
            with open('./List/courses_data.json', 'r', encoding='utf-8') as file:
                self.courses = json.load(file)

        except FileNotFoundError:
            self.courses = []

    def save_classes_to_file(self):
        output_dir = "./List/"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open('./List/classes_data.json', 'w', encoding="utf-8") as file:
            json.dump(self.classes, file, indent=4,
                      ensure_ascii=False)
            # usei ensure_ascii=False para evitar a codificação incorreta na lista de Classes_data
