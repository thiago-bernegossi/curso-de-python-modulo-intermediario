# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_09_01.py
# DATA DE CRIAÇÃO: 31-05-2025
# DATA DE PUBLICAÇÃO: 31-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Intermediário
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

set_01 = {16, 8, 21, 30, 41, 28}
print(f'Exibindo o número de elementos do conjunto 01: {len(set_01)}')
print(f'Exibindo os elementos do conjunto 01: {set_01}')
print(f'Exibindo o tipo de objeto do conjunto 01: {type(set_01)}\n')

set_01 = {16, 8, 21, 30, 41, 28, 8}
print(f'Exibindo os elementos do conjunto 01: {set_01}\n')

set_01 = {16, 8, 21, 30, 41, 28, '8'}
print(f'Exibindo os elementos do conjunto 01: {set_01}\n')

set_01 = {16, 8, 21, 30, 41, 28, 8.0}
print(f'Exibindo os elementos do conjunto 01: {set_01}\n')

set_01 = {16, 8, 21, 30, 41, 28, 8.0000000001}
print(f'Exibindo os elementos do conjunto 01: {set_01}\n')

set_02 = set()
print(f'Exibindo o número de elementos do conjunto 02: {len(set_02)}')
print(f'Exibindo os elementos do conjunto 02: {set_02}')
print(f'Exibindo o tipo de objeto do conjunto 02: {type(set_02)}\n')

set_03 = {}
print(f'Exibindo o número de elementos do conjunto 03: {len(set_03)}')
print(f'Exibindo os elementos do conjunto 03: {set_03}')
print(f'Exibindo o tipo de objeto do conjunto 03: {type(set_03)}\n')

set_04 = set([4, 9, 14, 21])
print(f'Exibindo o número de elementos do conjunto 04: {len(set_04)}')
print(f'Exibindo os elementos do conjunto 04: {set_04}')
print(f'Exibindo o tipo de objeto do conjunto 04: {type(set_04)}\n')

set_01 = {1, 2, 3, 4}
print(f'Exibindo o número de elementos do conjunto 01: {len(set_01)}')
print(f'Exibindo os elementos do conjunto 01: {set_01}')
print(f'Exibindo o tipo de objeto do conjunto 01: {type(set_01)}\n')

set_02 = set([10, 20, 30])
print(f'Exibindo o número de elementos do conjunto 02: {len(set_02)}')
print(f'Exibindo os elementos do conjunto 02: {set_02}')
print(f'Exibindo o tipo de objeto do conjunto 02: {type(set_02)}\n')

set_03 = set()
print(f'Exibindo o número de elementos do conjunto 03: {len(set_03)}')
print(f'Exibindo os elementos do conjunto 03: {set_03}')
print(f'Exibindo o tipo de objeto do conjunto 03: {type(set_03)}')

print('\nA execução do sistema informático foi concluída.')