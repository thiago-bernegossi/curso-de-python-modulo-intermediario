# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_09_02.py
# DATA DE CRIAÇÃO: 03-06-2025
# DATA DE PUBLICAÇÃO: 03-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Intermediário
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

text_01 = 'Qualquer Texto'
print(f'Exibindo os elementos da variável text_01: {text_01}')
print(f'Exibindo o tipo de objeto da variável text_01: {type(text_01)}\n')

set_01 = set(text_01)
print(f'Exibindo os elementos da variável set_01: {set_01}\n')

tuple_01 = (26, 73, 41)
set_02 = set(tuple_01) 
print(f'Exibindo os elementos da variável set_02: {set_02}\n')

list_01 = [32, 34]
set_03 = set(list_01)
print(f'Exibindo os elementos da variável set_03: {set_03}\n')

tuple_01 = (26, 73, 41, 73)
set_02 = set(tuple_01) 
print(f'Exibindo os elementos da variável set_02: {set_02}\n')

set_04 = set(set_01)
print(f'Exibindo os elementos da variável set_01: {set_01}')
print(f'Exibindo o identificador da variável set_01: {id(set_01)}')
print(f'Exibindo o tipo de objeto da variável set_01: {type(set_01)}\n')

print(f'Exibindo os elementos da variável set_04: {set_04}')
print(f'Exibindo o identificador da variável set_04: {id(set_04)}')
print(f'Exibindo o tipo de objeto da variável set_04: {type(set_04)}\n')

set_04 = set_01
print(f'Exibindo os elementos da variável set_01: {set_01}')
print(f'Exibindo o identificador da variável set_01: {id(set_01)}')
print(f'Exibindo o tipo de objeto da variável set_01: {type(set_01)}\n')

print(f'Exibindo os elementos da variável set_04: {set_04}')
print(f'Exibindo o identificador da variável set_04: {id(set_04)}')
print(f'Exibindo o tipo de objeto da variável set_04: {type(set_04)}')

print('\nA execução do sistema informático foi concluída.')