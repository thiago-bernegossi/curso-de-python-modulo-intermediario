# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_12_11.py
# DATA DE CRIAÇÃO: 14-06-2025
# DATA DE PUBLICAÇÃO: 14-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

def first_function():
    print('Dentro da primeira função temos os valores:', object_a, object_b)

def second_function():
    object_a = 100
    object_b = 200
    print('\nDentro da segunda função temos os valores:', object_a, object_b)

object_a = 10
object_b = 20

first_function()
second_function()

print('\nFora das duas funções temos os valores:', object_a, object_b)

print(f'\nA execução do sistema informático foi concluída.')