# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_12_04.py
# DATA DE CRIAÇÃO: 13-06-2025
# DATA DE PUBLICAÇÃO: 13-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

from random import randint

print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos construir uma lista de números inteiros aleatórios entre 01 e 1000:\n')

def load_list(value):
    new_list = []
    for item in range(value):
        new_list.append(randint(1, 1000))
    return new_list

numbers = int(input('Digite a quantidade desejada de valores: '))
values = load_list(numbers)

print(f'\nExibindo uma lista de números inteiros com os valores: {values}')
print(f'\nExibindo o número de elementos da lista: {numbers}')

print(f'\nA execução do sistema informático foi concluída.')