# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_12_03.py
# DATA DE CRIAÇÃO: 12-06-2025
# DATA DE PUBLICAÇÃO: 12-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

from random import randint

print('A execução do sistema informático foi iniciada.\n')

def load_list():
    new_list = []
    for item in range(10):
        new_list.append(randint(1, 1000))
    return new_list

print('Exibindo a primeira lista gerada...')
first_values = load_list()

print('O resultado é:')
print(first_values)

print('\nExibindo a segunda lista gerada...')
second_values = load_list()

print('O resultado é:')
print(second_values)

print(f'\nA execução do sistema informático foi concluída.')