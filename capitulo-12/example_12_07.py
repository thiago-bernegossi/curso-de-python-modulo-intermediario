# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_12_07.py
# DATA DE CRIAÇÃO: 13-06-2025
# DATA DE PUBLICAÇÃO: 13-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

def difference(object_a, object_b):
    return object_a - object_b

first_value = 25
second_value = 5

print(f'25 - 5 = {difference(first_value, second_value)}\n')
print(f'25 - 5 = {difference(object_b = second_value, object_a = first_value)}\n')
print(f'5 - 25 = {difference(object_b = first_value, object_a = second_value)}')

print(f'\nA execução do sistema informático foi concluída.')