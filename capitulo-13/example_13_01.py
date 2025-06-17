# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_13_01.py
# DATA DE CRIAÇÃO: 17-06-2025
# DATA DE PUBLICAÇÃO: 17-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

example_values = [28, -17, 45, -3, 12, -39, 7, -25, 33, -9, 1, -48, 40, -11, 15, -31, 22, -4, 36, -6]

list_01 = []
for value in example_values:
    list_01.append(value * 2)
print(f'Exibindo o resultado da utilização de um laço de repetição com o método append para criar uma lista: {list_01}')

list_02 = [value * 2 for value in example_values]
print(f'\nExibindo o resultado da utilização do recurso list comprehension para criar uma lista: {list_02}')

print(f'\nA execução do sistema informático foi concluída.')