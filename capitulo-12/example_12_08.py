# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_12_08.py
# DATA DE CRIAÇÃO: 13-06-2025
# DATA DE PUBLICAÇÃO: 13-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

def summation(*numbers):
    value = 0
    for number in numbers:
        value += number
    return value

print(f'5 + 3 + 1 = {summation(5, 3, 1)}\n')
print(f'10 + 10 = {summation(10, 10)}\n')
print(f'5 + 5 + 5 + 5 + 5 = {summation(5, 5, 5, 5, 5)}')

print(f'\nA execução do sistema informático foi concluída.')