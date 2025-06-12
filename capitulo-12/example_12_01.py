# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_12_01.py
# DATA DE CRIAÇÃO: 12-06-2025
# DATA DE PUBLICAÇÃO: 12-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

def displays_hyphens():
    print('---')

list_01 = [10, 20, 30, 40, 50]
for value in list_01:
    print(value)
    displays_hyphens()

print('\n')

list_02 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for value in list_02:
    print(value)
    displays_hyphens()

print(f'\nA execução do sistema informático foi concluída.')