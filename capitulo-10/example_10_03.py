# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_10_03.py
# DATA DE CRIAÇÃO: 05-06-2025
# DATA DE PUBLICAÇÃO: 05-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Intermediário
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

dictionary_01 = {}
print(f'Exibindo o número de elementos do dicionário 01: {len(dictionary_01)}')
print(f'Exibindo os elementos do dicionário 01: {dictionary_01}')
print(f'Exibindo o tipo de objeto do dicionário 01: {type(dictionary_01)}\n')

dictionary_01['x'] = 120
print(f'Exibindo os elementos do dicionário 01 após adicionar um par cuja chave é x e o valor é 120: {dictionary_01}\n')

dictionary_01['x'] = 250
print(f'Exibindo os elementos do dicionário 01 após alteração: {dictionary_01}\n')

dictionary_01['x'] = 90
print(f'Exibindo os elementos do dicionário 01 após alteração: {dictionary_01}\n')

dictionary_01['y'] = 521
print(f'Exibindo os elementos do dicionário 01 após adicionar um par cuja chave é y e o valor é 521: {dictionary_01}\n')

sum_01 = dictionary_01['x'] + dictionary_01['y']
print(f'O resultado da soma dos valores contidos nas duas chaves é: {sum_01}\n')

dictionary_01['x'] = dictionary_01['x'] + 100
print(f'O resultado da soma dos dois valores é: {dictionary_01['x']}\n')

dictionary_01['x'] += 100
print(f'O resultado da soma dos dois valores é: {dictionary_01['x']}\n')

key = 'x'
key = 'y'
key = 'z'
dictionary_01[key] = 0
print(f'Exibindo o número de elementos do dicionário 01: {len(dictionary_01)}')
print(f'Exibindo os elementos do dicionário 01: {dictionary_01}')
print(f'Exibindo o tipo de objeto do dicionário 01: {type(dictionary_01)}\n')

dictionary_02 = {}
print(f'Exibindo o número de elementos do dicionário 02: {len(dictionary_02)}')
print(f'Exibindo os elementos do dicionário 02: {dictionary_02}')
print(f'Exibindo o tipo de objeto do dicionário 02: {type(dictionary_02)}\n')

dictionary_02[110] = 45.6
print(f'Exibindo os elementos do dicionário 02 após adicionar um par cuja chave é 100 e o valor é 45.6: {dictionary_02}\n')

dictionary_02[9.2] = 'Texto'
print(f'Exibindo os elementos do dicionário 02 após adicionar um par cuja chave é 9.2 e o valor é Texto: {dictionary_02}\n')

dictionary_02[(0, 1, 2)] = 281.9
print(f'Exibindo os elementos do dicionário 02 após adicionar um par cuja chave é uma tupla e o valor é 281.9: {dictionary_02}')

print('\nA execução do sistema informático foi concluída.')