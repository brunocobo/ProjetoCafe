import json
import os.path
from tabulate import tabulate
from cpf_validator import cpf_validator
from cpf_validator.cpf_validator import is_valid_cpf


class ProfessorService:
    # classe de professores
    def __init__(self):
        # para iniciar a instancia dos professores
        self.professors = []
        self.load_professors_from_file()

    def add_professor(self):
        # Função para adicionar um novo professor à lista.
        print('=' * 50)
        print('Adicionar Professor'.center(50, '='))
        print('=' * 50)

        while True:
            # Solicita ao usuário informações sobre o novo professor.
            new_professor = {
                'name': str(input('Digite o nome do professor: ').strip().upper()),
                'code': int(self.get_valid_input('Digite o código do professor: ', str.isdigit)),
                'cpf': ''
            }
            while True:
                # Solicita ao usuário o CPF do novo professor e faz a validação
                new_professor['cpf'] = input('Digite o CPF do professor: ')
                if cpf_validator.is_valid_cpf(new_professor['cpf']):
                    break
                else:
                    print('=' * 50)
                    print('CPF inválido. Tente novamente!')
                    print('=' * 50)

            if not any(
                    professor['cpf'] == new_professor['cpf'] or
                    professor['code'] == new_professor['code'] or
                    professor['name'] == new_professor['name'] for professor in self.professors
            ):
                # Verifica se o CPF, o código ou o nome já estão cadastrados.
                # Se não estiverem, adiciona o novo professor à lista.
                self.professors.append(new_professor)
                # Salva os dados atualizados no arquivo.
                self.save_professors_to_file()
                print('=' * 50)
                print('\nDados válidos!\n'
                      'Professor cadastrado com sucesso!')
                print('=' * 50)

            else:
                print('=' * 50)
                if any(professor['cpf'] == new_professor['cpf'] for professor in self.professors):
                    print('CPF já cadastrado!')
                if any(professor['code'] == new_professor['code'] for professor in self.professors):
                    print('Código já cadastrado!')
                if any(professor['name'] == new_professor['name'] for professor in self.professors):
                    print('Nome já cadastrado!')
                print('Tente novemente!\n')
                print('=' * 50)

            if not self.should_continue():
                break

    def list_professor(self):
        # Função para listar professores cadastrados.
        print('=' * 50)
        print('Lista de professores Cadastrados'.center(50, '='))
        print('=' * 50)

        # para carregar as informações mais recentes
        self.load_professors_from_file()

        if not self.professors:
            # Se não houver professores cadastrados, exibe uma mensagem
            print('Sem professores cadastrados!')
        else:
            table_data = []
            for professor in self.professors:
                # Coleta as informações de cada professor e adiciona à tabela de dados.
                professor_name = professor['name']
                professor_code = professor['code']
                professor_cpf = professor['cpf']

                table_data.append([professor_code, professor_name, professor_cpf])
            headers = ['Matrícula', 'Nome Professor', 'CPF Professor']
            # Utiliza a biblioteca tabulate para imprimir os dados em formato tabular.
            print(tabulate(table_data, headers=headers, tablefmt='fancy_grid'))

        print('=' * 50)

    def update_professor(self):
        # Função para atualizar informações de um professor.
        while True:
            print('=' * 50)
            print('Atualizar Professor'.center(50, '='))
            print('=' * 50)

            search_term = input("Digite o CPF do professor: ")

            if not is_valid_cpf(search_term):
                # Valida se o CPF inserido é válido.
                print('CPF inválido. Vamos tentar novamente!')
                if not self.should_continue():
                    break
                continue

            found_professors = [professor for professor in self.professors if search_term in professor['cpf']]

            if not found_professors:
                # Se nenhum professor for encontrado com o CPF informado, exibe a mensagem.
                print('CPF não encontrado na base de dados')
                if not self.should_continue():
                    break
                continue

            print('***' * 15)
            print('Professor Encontrado')
            for idx, professor in enumerate(found_professors, start=1):
                # Exibe informações dos professores encontrados.
                print(f"({idx}) Professor: {professor['name'].upper()}, Código: {professor['code']}".upper())
                print('***' * 15)

            try:
                code_to_search = int(input('\nDigite o código do professor: ').strip())

            except ValueError:
                # Valida se o código inserido é válido.
                print('Código inválido!')
                continue

            select_professor = next((professor for professor in found_professors
                                     if code_to_search == professor['code']), None)

            if select_professor:
                # Se o professor for encontrado com o código informado, chama a função para atualizar as informações.
                self.update_professor_info(select_professor)
                if not self.should_continue():
                    break
            else:
                # Se nenhum professor for encontrado com o código informado, exibe uma mensagem.
                print(f'Nenhum professor com o código {code_to_search} foi encontrado')

    def update_professor_info(self, select_professor):
        # para atualizar informções do professor
        while True:
            print('=' * 50)
            print(f"\nAtualizando Informações para o Professor: {select_professor['name'].upper()}")

            try:
                rep = int(input('\nQual informação deseja atualizar:\n'
                                'Digite 1 para Nome\n'
                                'Digite 2 para Código\n'
                                'Digite 3 para CPF\n'
                                '\nQual opção deseja?: ').strip())
                if rep == 1:
                    # Atualiza o nome do professor.
                    print('=' * 50)
                    print('Você selecionou Nome!'.center(50, '='))
                    print('=' * 50)
                    select_professor['name'] = input('\nDigite o novo nome: ').strip().lower()
                    break

                elif rep == 2:
                    # Atualiza o código do professor.
                    print('=' * 50)
                    print('Você selecionou Código!'.center(50, '='))
                    print('=' * 50)
                    select_professor['code'] = int(input('\nDigite o novo código: '))
                    break

                elif rep == 3:
                    # Atualiza o CPF do professor.
                    print('=' * 50)
                    print('Você selecionou CPF!'.center(50, '='))
                    print('=' * 50)
                    while True:
                        new_cpf = input('\nDigite o novo CPF: ')
                        if is_valid_cpf(new_cpf):
                            select_professor['cpf'] = new_cpf
                            break
                        else:
                            print('CPF inválido. Tente novamente!')
                    break

                else:
                    print('Opção inválida. Digite uma opção válida')

            except ValueError:
                print('Opção inválida. Digite um número válido.')

        self.save_professors_to_file()
        # Salva as informações atualizadas em arquivo.
        print('=' * 50, '\nInformação atualizada com sucesso!\n')

    def exclude_professor(self):
        # para excluir um professor
        print('=' * 50)
        print('Você selecionou Excluir Professor'.center(50, '='))
        print('=' * 50)

        while True:
            search_term = input(f'Digite o CPF do professor a ser excluído: ').strip()

            if not search_term:
                continue
            professor_to_remove = [professor for professor in self.professors if search_term == professor['cpf']]

            if professor_to_remove:
                # Para remover o professor com o cpf fornecido
                for professor in professor_to_remove:
                    self.professors.remove(professor)
                self.save_professors_to_file()
                print('\n', '=' * 50)
                print(f"Professor com o CPF: '{search_term}' excluído com sucesso!")
                print('\n', '=' * 50)

            else:
                # Se nenhum professor com o CPF fornecido for encontrado, vai exibir uma msg
                print('=' * 50)
                print(
                    f'Não encontrei nenhum professor com o CPF: \'{search_term}\'\n'
                    'Tente digitar um CPF válido ou verifique a lista de professores!\n')

            continue_deleting = input('Deseja continuar excluindo? [S/N]: ').strip().lower()
            if continue_deleting != 's':
                break

    def save_professors_to_file(self):
        # para salvar o cadastro do professor em um arquivo json
        output_dir = "./List"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open('./List/professor_data.json', 'w', encoding='utf-8') as file:
            json.dump(self.professors, file, indent=4, ensure_ascii=False)

    def load_professors_from_file(self):
        # para carregar os professores da lista salva em arquivo json
        try:
            with open('./List/professor_data.json', 'r') as file:
                self.professors = json.load(file)

        except FileNotFoundError:
            self.professors = []

    def show_invalid_option(self):
        # para opçao invalida
        print('\n', '-=' * 20, 'OPÇÃO INVÁLIDA', '-=' * 20, '\n')

    def get_valid_input(self, prompt, validation_func):
        while True:
            user_input = input(prompt)
            if validation_func(user_input):
                return user_input
            else:
                print('Dados inválidos. Vamos tentar novamente!')

    def should_continue(self):
        # perguntar ao usuário se deseja continuar
        while True:
            proceed = (input('\nDeseja continuar? [S/N]: ')).strip().lower()
            print('\n')
            if proceed in ('s', 'n'):
                return proceed == 's'
            else:
                print('Opção inválida. Digite "S" para continuar ou "N" para sair.')
