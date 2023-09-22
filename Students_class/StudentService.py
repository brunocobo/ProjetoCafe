import json
from cpf_validator import cpf_validator
from cpf_validator.cpf_validator import is_valid_cpf
import os
from tabulate import tabulate


class StudentService:

    def __init__(self):
        # Inicializa uma instância de StudentService com uma lista vazia de estudantes e carrega os dados do arquivo.
        self.students = []
        self.load_students_from_file()

    def add_student(self):
        # Função para adicionar um novo estudante à lista.
        print('=' * 50)
        print('Adicionar Estudante'.center(50, '='))
        print('=' * 50)

        while True:
            # Solicita ao usuário informações sobre o novo estudante.
            new_student = {
                'name': str(input('Digite o nome do estudante: ').strip().upper()),
                'enroll': int(self.get_valid_input('Digite a matrícula do estudante: ', str.isdigit)),
                'cpf': ''
            }
            while True:
                # Solicita ao usuário o CPF do novo estudante e faz a validação
                new_student['cpf'] = input('Digite o CPF do estudante: ')
                if cpf_validator.is_valid_cpf(new_student['cpf']):
                    break
                else:
                    print('=' * 50)
                    print('CPF inválido. Tente novamente!')
                    print('=' * 50)

            if not any(
                    student['cpf'] == new_student['cpf'] or
                    student['enroll'] == new_student['enroll'] or
                    student['name'] == new_student['name'] for student in self.students
            ):
                # Verifica se o CPF, a matrícula ou o nome já estão cadastrados.
                # Se não estiverem, adiciona o novo estudante à lista.
                self.students.append(new_student)
                # Salva os dados atualizados no arquivo.
                self.save_students_to_file()
                print('=' * 50)
                print('\nDados válidos!\n'
                      'Estudante cadastrado com sucesso!')
                print('=' * 50)
            else:
                print('=' * 50)
                if any(student['cpf'] == new_student['cpf'] for student in self.students):
                    print('CPF já cadastrado!')
                if any(student['enroll'] == new_student['enroll'] for student in self.students):
                    print('Código já cadastrado!')
                if any(student['name'] == new_student['name'] for student in self.students):
                    print('Nome já cadastrado!')
                print('Tente novamente!\n')
                print('=' * 50)

            if not self.should_continue():
                break

    def list_students(self):
        # Função para listar os estudantes cadastrados.
        print('=' * 50)
        print('Lista de Estudantes Cadastrados'.center(50, '='))
        print('=' * 50)
        # para carregar as informações mais recentes
        self.load_students_from_file()

        if not self.students:
            print('Sem estudantes cadastrados')
        else:
            table_data = []
            for student in self.students:
                student_name = student['name']
                student_enroll = student['enroll']
                student_cpf = student['cpf']

                table_data.append([student_enroll, student_name, student_cpf])

            headers = ['Matrícula', 'Nome do Aluno', 'CPF do Aluno']
            print(tabulate(table_data, headers=headers, tablefmt='fancy_grid', stralign='center'))
        # Carrega os dados dos estudantes a partir do arquivo e exibe-os em forma de tabela.
        print('=' * 50)

    def update_students(self):
        # Função para atualizar informações de um estudante.
        while True:
            print('=' * 50)
            print('Atualizar Estudante'.center(50, '='))
            print('=' * 50)

            search_term = input('Digite o CPF do estudante: ')

            if not is_valid_cpf(search_term):
                # Valida se o CPF fornecido é válido.
                print('CPF inválido. Tente novamente!')
                if not self.should_continue():
                    break
                continue

            found_students = [student for student in self.students if search_term in student['cpf']]

            if not found_students:
                print('CPF não encontrado na base de dados')
                if not self.should_continue():
                    break
                continue

            print('***' * 15)
            print('Estudante Encontrado')
            for idx, student in enumerate(found_students, start=1):
                # Lista os estudantes encontrados e permite a seleção com base na matrícula.
                print(f"({idx}) Estudante: {student['name'].upper()}, Matrícula: {student['enroll']}".upper())
                print('***' * 15)

            try:
                code_to_search = int(input("\nDigite a matrícula do estudante: ").strip())

            except ValueError:
                print('Matrícula inválida!')
                continue

            select_student = next((student for student in found_students if code_to_search
                                   == student['enroll']), None)

            if select_student:
                # Se um estudante com a matrícula selecionada for encontrado, chama a função para atualizar informações.
                self.update_student_info(select_student)
                if not self.should_continue():
                    break
            else:
                print(f'Nenhum estudante com a matrícula \'{code_to_search}\' foi encontrado')

    def update_student_info(self, student):
        # Função para atualizar informações específicas.
        while True:
            print('=' * 50)
            print(f"\nAtualizando Informações para o Estudante: {student['name'].upper()}")

            try:
                rep = int(input('\nQual informação deseja atualizar:\n'
                                'Digite 1 para Nome\n'
                                'Digite 2 para Código\n'
                                'Digite 3 para CPF\n'
                                '\nQual opção deseja?: ').strip())

                if rep == 1:
                    print('=' * 50)
                    print('Você selecionou Nome!'.center(50, '='))
                    print('=' * 50)
                    student['name'] = input('\nDigite o novo nome: ').strip().lower()
                    break

                elif rep == 2:
                    print('=' * 50)
                    print('Você selecionou Código!'.center(50, '='))
                    print('=' * 50)
                    student['enroll'] = int(input('\nDigite a nova matrícula: '))
                    break

                elif rep == 3:
                    print('=' * 50)
                    print('Você selecionou CPF!'.center(50, '='))
                    print('=' * 50)
                    while True:
                        new_cpf = input('\nDigite o novo CPF: ')
                        if is_valid_cpf(new_cpf):
                            student['cpf'] = new_cpf
                            break
                        else:
                            print('CPF inválido. Tente novamente!')
                    break

                else:
                    print('Opção inválida. Digite uma opção válida')

            except ValueError:
                print('Opção inválida. Digite um número válido.')

        self.save_students_to_file()
        # Salva os dados atualizados.
        print('=' * 50, '\nInformação atualizada com sucesso!\n')

    def exclude_students(self):
        # Função para excluir um estudante da lista.
        print('=' * 50)
        print('Você selecionou Excluir Estudante'.center(50, '='))
        print('=' * 50)

        while True:
            # Solicita ao usuário que digite o CPF do estudante a ser excluído.
            search_term = input('\nDigite o CPF do estudante a ser excluído: ').strip()

            if not search_term:
                # Se o campo de pesquisa estiver vazio, continue pedindo ao usuário para inserir um CPF.
                continue

            students_to_remove = [student for student in self.students if search_term == student['cpf']]

            if students_to_remove:
                # Se estudantes com o CPF pesquisado forem encontrados na lista.
                for student in students_to_remove:
                    self.students.remove(student)
                    # Salva os dados atualizados no arquivo.
                self.save_students_to_file()
                print('\n', '=' * 50)
                print(f"Estudante com o CPF: '{search_term}' excluído com sucesso!")
                print('\n', '=' * 50)

            else:
                print('=' * 50)
                print(
                    f'Não encontrei nenhum estudante com o CPF: \'{search_term}\'\n'
                    'Tente digitar um CPF válido ou verifique a lista de estudantes!\n')

            continue_deleting = input('Deseja continuar excluindo? [S/N]: ').strip().lower()
            if continue_deleting != 's':
                break

    def save_students_to_file(self):
        # Função para salvar os dados dos estudantes em um arquivo JSON.

        output_dir = "./List/"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open('./List/students_data.json', 'w', encoding="utf-8") as file:
            json.dump(self.students, file, indent=4, ensure_ascii=False)

    def load_students_from_file(self):
        # Função para carregar os dados dos estudantes do arquivo JSON, se existirem.

        try:
            with open("./List/students_data.json", 'r', encoding="utf-8") as file:
                self.students = json.load(file)

        except FileNotFoundError:
            self.students = []

    def show_invalid_option(self):
        # Função para exibir uma mensagem de opção inválida.

        print("\n", "*/*" * 5, "Opção Inválida", "*/*" * 5, "\n")

    def get_valid_input(self, prompt, validation_func):
        # Função para obter uma entrada válida do usuário com base em uma função de validação.

        while True:
            user_input = input(prompt)
            if validation_func(user_input):
                return user_input
            else:
                print('Dados inválidos. Tente novamente.')

    def should_continue(self):
        # Função para determinar se o usuário deseja continuar executando a ação atual.

        while True:
            proceed = input('\nDeseja continuar? [S/N]: ').strip().lower()
            print('\n')
            if proceed in ('s', 'n'):
                return proceed == 's'
            else:
                print('Opção inválida. Digite "S" para continuar ou "N" para sair.')
