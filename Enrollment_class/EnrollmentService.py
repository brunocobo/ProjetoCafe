import json
import os
from functions.functions import Functions
from tabulate import tabulate
from Students_class.StudentService import StudentService

class EnrollmentService:
    def __init__(self):
        self.enrollment = []
        self.classes = []
        self.students = []
        self.load_enrollments_from_file()
        self.load_classes_from_file()
        self.load_students_from_file()

    def add_enrollment(self):
        print('=' * 50)
        print('Adicionar Matrículas'.center(50, '='))
        print('=' * 50)

        functions_instance = Functions()
        self.load_enrollments_from_file()
        self.load_students_from_file()
        enrollment_code = int(functions_instance.get_valid_input('Digite o código da matrícula: ', str.isdigit))

        # Encontre o aluno correspondente com base no código de matrícula
        selected_student = next((student for student in self.students if student['enroll'] == enrollment_code), None)

        student_instance = StudentService()
        if not selected_student:
            print(f'Aluno com código {enrollment_code} não encontrado.')

            # Pergunte ao usuário se deseja adicionar o aluno
            add_student_option = input('Deseja adicionar o aluno? [S/N]: ').strip().lower()
            if add_student_option.lower() == 's':
                # Chame a função para adicionar um estudante existente
                student_instance.add_student()
            else:
                # Caso contrário, informe que a matrícula não pode ser adicionada
                print('Matrícula não pode ser adicionada, pois o aluno não foi encontrado.')

        else:
            print(f'Aluno encontrado: {selected_student["name"]}')

            # Solicite ao usuário que selecione uma turma existente
            print('Turmas disponíveis:')
            classes_table = [[class_data['class_code']] for class_data in self.classes]
            print(tabulate(classes_table, headers=['Turma'], tablefmt='pretty'))

            class_code = int(
                functions_instance.get_valid_input('Digite o código da turma para cadastrar o aluno: ', str.isdigit))

            # Verifique se a turma existe na lista de turmas
            selected_class = next((class_data for class_data in self.classes if class_data['class_code'] == class_code),
                                  None)

            if not selected_class:
                print(f'Turma com código {class_code} não encontrada.')
            else:
                # Faça o cadastro do aluno na turma selecionada
                new_enrollment = {
                    'enrollment_code': enrollment_code,
                    'student_code': enrollment_code,
                    'class_code': class_code  # Usando 'class_code' do dicionário 'selected_class'
                }

                self.enrollment.append(new_enrollment)
                self.save_enrollments_to_file()
                print('=' * 50)
                print('Matrícula adicionada com sucesso!')
                print('=' * 50)

    def get_student_name_by_enrollment_code(self, enrollment_code):
        student = next((student for student in self.students if student['enroll'] == enrollment_code), None)
        return student['name'] if student else 'N/A'

    def list_enrollment(self):
        print('=' * 50)
        print('Lista de Matrículas'.center(50, '='))
        print('=' * 50)

        # para carregar as informações mais recentes
        self.load_enrollments_from_file()
        self.load_students_from_file()

        if not self.enrollment:
            print('Sem matrículas cadastradas.')
        else:
            # ordenar a lista de matrículas por ordem crescente
            sorted_enrollments = sorted(self.enrollment, key=lambda x: x['enrollment_code'])

            table_data = []
            for enroll in sorted_enrollments:
                enrollment_code = enroll['enrollment_code']
                class_code = enroll['class_code']

                # Use a função para obter o nome do aluno correspondente
                student_name = self.get_student_name_by_enrollment_code(enrollment_code)

                table_data.append([enrollment_code, class_code, student_name])
            headers = ['Matrícula', 'Turma', 'Nome do Aluno']
            print(tabulate(table_data, headers=headers, tablefmt='fancy_grid'))

        print('=' * 50)

    def update_enrollment(self):
        print('=' * 50)
        print('Atualizar Matrícula'.center(50, '='))
        print('=' * 50)

        enrollment_code = int(input('Digite a matrícula para atualizar: '))

        # para encontrar a matrícula
        selected_enrollment = next((enrollment for enrollment
                                    in self.enrollment if enrollment['enrollment_code'] == enrollment_code), None)

        if not selected_enrollment:
            print(f'Matrícula: {enrollment_code} não encontrada!')
        else:
            # solicitar ao usuário que selecione uma nova turma existente
            print('Turmas Disponíveis:')
            classes_table = [[class_data['class_code']] for class_data in self.classes]
            print(tabulate(classes_table, headers=['Turma'], tablefmt='fancy_grid'))

            new_class_code = int(input('Digite o código da nova turma para atualizar a matrícula: '))

            # para verificar se a nova turma existe na lista
            select_class = next((class_data for class_data in self.classes
                                 if class_data['class_code'] == new_class_code), None)

            if not select_class:
                print(f'Turma: {new_class_code} não encontrada.')
            else:
                # atualizar a turma na matrícula selecionada
                selected_enrollment['class_code'] = new_class_code
                self.save_enrollments_to_file()
                print('=' * 50)
                print('Matrícula atualizada com sucesso!')
                print('=' * 50)

    def exclude_enrollment(self):
        print('=' * 50)
        print('Você selecionou Excluir Matrícula'.center(50, '='))
        print('=' * 50)

        while True:
            search_term = int(input('\nDigite a matrícula do aluno a ser excluído: ').strip())

            if not search_term:
                continue

            enroll_to_remove = [enroll for enroll in self.enrollment if search_term == enroll['enrollment_code']]

            if enroll_to_remove:
                for enroll in enroll_to_remove:
                    self.enrollment.remove(enroll)
                self.save_enrollments_to_file()
                print('\n', '=' * 50)
                print(f"Matrícula: '{search_term}' excluída com sucesso!")
                print('\n', '=' * 50)

            else:
                print('=' * 50)
                print(
                    f'Eita, não encontrei essa matrícula: {search_term}\n'
                    'Tente novamente ou verifique a lista de matrículas!\n'
                )

            continue_deleting = input('Deseja continuar excluindo? [S/N]: ').strip().lower()
            if continue_deleting != 's':
                break

    def load_enrollments_from_file(self):
        try:
            with open('./List/enrollment_data.json', 'r', encoding='utf-8') as file:
                self.enrollment = json.load(file)
        except FileNotFoundError:
            self.enrollment = []

    def load_classes_from_file(self):
        try:
            with open('./List/classes_data.json', 'r', encoding='utf-8') as file:
                self.classes = json.load(file)

        except FileNotFoundError:
            self.classes = []

    def load_students_from_file(self):
        try:
            with open('./List/students_data.json', 'r', encoding='utf-8') as file:
                self.students = json.load(file)
        except FileNotFoundError:
            self.students = []

    def save_enrollments_to_file(self):
        output_dir = "./List/"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open('./List/enrollment_data.json', 'w', encoding="utf-8") as file:
            json.dump(self.enrollment, file, indent=4,
                      ensure_ascii=False)
            # usei ensure_ascii=False para corrigir a codificação na lista de Classes_data


