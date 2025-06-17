# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_13_02.py
# DATA DE CRIAÇÃO: 17-06-2025
# DATA DE PUBLICAÇÃO: 17-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

example_values = [18, -42, 5, -29, 33, -11, 48, -7, 2, -36, 40, -1, 25, -15, 10, -49, 21, -3, 30, -8]

list_01 = []
for value in example_values:
    list_01.append(value * 2)
print(f'Exibindo o resultado da utilização de um laço de repetição com o método append para criar uma lista: {list_01}')

list_02 = [value * 2 for value in example_values]
print(f'\nExibindo o resultado da utilização do recurso list comprehension para criar uma lista: {list_02}')

list_03 = []
for value in example_values:
    if value > 0:
        list_03.append(value * 2)
print(f'\nExibindo o resultado da utilização de um laço de repetição com o método append para criar uma lista apenas com os valores positivos: {list_03}')

list_04 = [value * 2 for value in example_values if value > 0]
print(f'\nExibindo o resultado da utilização do recurso list comprehension para criar uma lista apenas com os valores positivos: {list_04}')

print(f'\nA execução do sistema informático foi concluída.')