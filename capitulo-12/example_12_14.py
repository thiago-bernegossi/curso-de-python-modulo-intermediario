# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_12_14.py
# DATA DE CRIAÇÃO: 15-06-2025
# DATA DE PUBLICAÇÃO: 15-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def calculate_square_root(number):
    return number ** 2

print(f'As raízes quadradas calculadas são: {list(map(calculate_square_root, numbers))}\n')

print(f'As raízes cúbicas calculadas são: {list(map((lambda object_x:  object_x ** 3), numbers))}')

print(f'\nA execução do sistema informático foi concluída.')