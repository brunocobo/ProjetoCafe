class Functions:
    # criei essa classes para fazer testes para as funções abaixp
    @staticmethod
    def should_continue():
        while True:
            proceed = input('\nDeseja continuar? [S/N]: ').strip().lower()
            print('\n')
            if proceed in ('s', 'n'):
                return proceed == 's'
            else:
                print('Opção inválida. Digite "S" para continuar ou "N" para sair.')

    @staticmethod
    def get_valid_input(prompt, validation_func):
        while True:
            user_input = input(prompt)
            if validation_func(user_input):
                return user_input
            else:
                print('Dados inválidos. Tente novamente.')

    @staticmethod
    def show_invalid_option():
        print("\n", "*/*" * 5, "Opção Inválida", "*/*" * 5, "\n")


