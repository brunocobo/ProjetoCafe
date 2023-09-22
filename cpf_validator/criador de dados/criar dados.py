import random
import json
from unidecode import unidecode
from faker import Faker
import os

# Verifica se o diretório existe, senão o cria
output_dir = "../../List/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

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


def generate_valid_cpf():
    while True:
        cpf = ''.join([str(random.randint(0, 9)) for _ in range(11)])
        if ValidatorCPF.cpf_e_valido(cpf):
            return cpf


students_data = []

fake = Faker()


for i in range(1, 101):
    student = {
        "name": unidecode(fake.name()),
        "enroll": i,
        "cpf": generate_valid_cpf()
    }
    students_data.append(student)


with open("../../List/students_data.json", "w", encoding="utf-8") as file:
    json.dump(students_data, file, ensure_ascii=False, indent=4)



