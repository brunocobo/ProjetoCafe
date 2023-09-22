import json
import os

# Lista de nomes fictícios de disciplinas universitárias (em maiúsculas)
disciplinas_ficticias = [
    "INTRODUÇÃO À PROGRAMAÇÃO",
    "CÁLCULO I",
    "ÁLGEBRA LINEAR",
    "FÍSICA GERAL",
    "HISTÓRIA DA ARTE",
    "INGLÊS AVANÇADO",
    "ECONOMIA MICROECONÔMICA",
    "QUÍMICA ORGÂNICA",
    "DIREITO CONSTITUCIONAL",
    "BIOLOGIA CELULAR",
    "PSICOLOGIA SOCIAL",
    "MARKETING ESTRATÉGICO",
    "ÉTICA PROFISSIONAL",
    "SOCIOLOGIA URBANA",
    "GESTÃO DE PROJETOS",
    "ENGENHARIA DE SOFTWARE",
    "ANÁLISE DE DADOS",
    "ROBÓTICA AVANÇADA",
    "NEUROCIÊNCIA COGNITIVA",
    "TEORIA POLÍTICA CONTEMPORÂNEA",
    "DESENVOLVIMENTO WEB AVANÇADO",
    "ADMINISTRAÇÃO DE BANCO DE DADOS",
    "REDES DE COMPUTADORES",
    "SEGURANÇA DA INFORMAÇÃO",
    "SISTEMAS OPERACIONAIS",
    "INTELIGÊNCIA ARTIFICIAL",
    "ENGENHARIA DE SOFTWARE",
    "ANÁLISE DE ALGORITMOS",
    "PROGRAMAÇÃO ORIENTADA A OBJETOS",
    "COMPUTAÇÃO EM NUVEM",
    "CIÊNCIA DE DADOS",
    "ROBÓTICA",
    "GESTÃO DE PROJETOS DE TI",
    "REALIDADE VIRTUAL E AUMENTADA",
    "CIBERSEGURANÇA",
    "IOT (INTERNET DAS COISAS)",
]

# Crie um diretório para salvar os dados, se ele não existir
output_dir = "./List/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Gere dados fictícios de disciplinas
courses_data = []

for i, nome_disciplina in enumerate(disciplinas_ficticias, start=1):
    course = {
        "course": nome_disciplina,
        "code": i,
    }
    courses_data.append(course)

# Salve os dados fictícios em um arquivo JSON
with open("../../List/courses_data.json", "w", encoding="utf-8") as file:
    json.dump(courses_data, file, ensure_ascii=False, indent=4)

print("Nomes de disciplinas fictícias em maiúsculas gerados e salvos com sucesso!")

