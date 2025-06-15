# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_12_13.py
# DATA DE CRIAÇÃO: 15-06-2025
# DATA DE PUBLICAÇÃO: 15-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

def calculate_sum(number):
    return number + 2

print(f'O resultado da soma é: {calculate_sum(10)}\n')

print(f'O resultado da soma é: {(lambda object_x: object_x + 2)(10)}\n')

print(f'O resultado da soma seguida de uma divisão é: {(lambda object_x, object_y, object_z: (object_x + object_y) / object_z)(350, 50, 20)}')

print(f'\nA execução do sistema informático foi concluída.')