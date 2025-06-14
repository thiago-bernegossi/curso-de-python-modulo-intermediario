# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_12_10.py
# DATA DE CRIAÇÃO: 14-06-2025
# DATA DE PUBLICAÇÃO: 14-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

def data_packing(*values):
    return sum(values)

print(data_packing(1, 2, 3, 4, 5))
print(f'\n{data_packing(5, 5, 5, 5, 5)}')

def data_unpacking(object_a, object_b, object_c):
    return (object_a + object_b) / object_c

new_sum = [5, 10, 15]
print(f'\n{data_unpacking(*new_sum)}')

print(f'\nA execução do sistema informático foi concluída.')