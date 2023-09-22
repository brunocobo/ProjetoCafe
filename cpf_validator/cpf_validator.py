class ValidatorCPF:
    @staticmethod
    def cpf_e_valido(cpf):
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False

        total = 0

        for i in range(9):
            total += int(cpf[i]) * (10 - i)
        digit_1 = (total * 10) % 11
        if digit_1 == 10:
            digit_1 = 0

        total = 0

        for i in range(10):
            total += int(cpf[i]) * (11 - i)
        digit_2 = (total * 10) % 11
        if digit_2 == 10:
            digit_2 = 0

        return cpf[-2:] == f"{digit_1}{digit_2}"

    @classmethod
    def is_valid_cpf(cls, param):
        pass


def is_valid_cpf(param: object) -> object:
    return ValidatorCPF.cpf_e_valido(param)
