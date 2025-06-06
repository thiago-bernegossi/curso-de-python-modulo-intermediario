# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_10_04.py
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
print(f'Exibindo o número de elementos do dicionário 01: {len(dictionary_01)}\n')

dictionary_01 = {120: 'Arroz', 134: 'Feijão', 117: 'Queijo'}
print(f'Exibindo o número de elementos do dicionário 01: {len(dictionary_01)}\n')
print(f'Exibindo os elementos do dicionário 01 após adicionar três pares cujas chaves são 120, 134 e 117 e os valores são Arroz, Feijão e Queijo: \n{dictionary_01}\n')
print(f'Exibindo o tipo de objeto do dicionário 01: {type(dictionary_01)}\n')

dictionary_01[125] = 'Açúcar'
dictionary_01[133] = 'Macarrão'
print(f'Exibindo o número de elementos do dicionário 01: {len(dictionary_01)}\n')
print(f'Exibindo os elementos do dicionário 01 após adicionar dois pares cujas chaves são 125 e 133 e o valores são Açúcar e Macarrão: \n{dictionary_01}\n')
print(f'Exibindo o tipo de objeto do dicionário 01: {type(dictionary_01)}\n')

dictionary_01.clear()
print(f'Exibindo os elementos do dicionário 01 após limpar seus elementos: {dictionary_01}\n')

dictionary_01 = {120: 'Arroz', 134: 'Feijão', 117: 'Queijo', 125: 'Açúcar', 133: 'Macarrão'}
print(f'Exibindo os elementos do dicionário 01 após adicionar cinco pares cujas chaves são 120, 134, 117, 125 e 133 e os valores são Arroz, Feijão, Queijo, Açúcar e Macarrão: \n{dictionary_01}\n')

dictionary_02 = dictionary_01.copy()
print(f'Exibindo os elementos do dicionário 02 após seus elementos serem copiados do dicionário 01: \n{dictionary_02}\n')

print(f'Exibindo o identificador do dicionário 01: {id(dictionary_01)}')
print(f'Exibindo o identificador do dicionário 02: {id(dictionary_02)}\n')

value = dictionary_02.get(134)
print(f'Exibindo o valor de um par cuja chave é 134: {value}')

value = dictionary_02[125]
print(f'Exibindo o valor de um par cuja chave é 125: {value}\n')

codes = (100, 139, 145, 150)
del(dictionary_02)

dictionary_02 = {}.fromkeys(codes, 'Texto')
print(f'Exibindo os elementos do dicionário 02 cujas chaves são 100, 139, 145 e 150 e os valores são Texto: \n{dictionary_02}\n')

dictionary_01[101] = 'Vinagre'
print(f'Exibindo os elementos do dicionário 01 após adicionar um par cuja chave é 101 e o valor é Vinagre: \n{dictionary_01}\n')

dictionary_02[101] = 'Vinagre'
print(f'Exibindo os elementos do dicionário 02 após adicionar um par cuja chave é 101 e o valor é Vinagre: \n{dictionary_02}\n')

value = dictionary_01.pop(101)
print(f'Exibindo o valor de um par removido do dicionário 01 cuja chave é 101 e está armazenado na variável value: {value}')

value = dictionary_01.pop(134)
print(f'Exibindo o valor de um par removido do dicionário 01 cuja chave é 134 e está armazenado na variável value: {value}\n')

print(f'Exibindo os elementos do dicionário 01: \n{dictionary_01}\n')

value = dictionary_01.popitem()
print(f'Exibindo o valor do último par removido do dicionário 01 e está armazenado na variável value: {value}')

value = dictionary_01.popitem()
print(f'Exibindo o valor do último par removido do dicionário 01 e está armazenado na variável value: {value}')

value = dictionary_01.popitem()
print(f'Exibindo o valor do último par removido do dicionário 01 e está armazenado na variável value: {value}\n')

print(f'Exibindo os elementos do dicionário 01: {dictionary_01}\n')

dictionary_01 = {120: 'Arroz', 134: 'Feijão', 117: 'Queijo', 125: 'Açúcar', 133: 'Macarrão', 101: 'Vinagre'}
print(f'Exibindo os elementos do dicionário 01 após adicionar cinco pares cujas chaves são 120, 134, 117, 125, 133 e 101 e os valores são Arroz, Feijão, Queijo, Açúcar, Macarrão e Vinagre: \n{dictionary_01}\n')

new_value = dictionary_01.setdefault(144, 'Sal')
print(f'Exibindo os elementos do dicionário 01 após adicionar um par cuja chave é 144 e o valor é Sal: \n{dictionary_01}\n')

dictionary_01.update(((110, 'Café'), (178, 'Óleo'), (156, 'Ervilha')))
print(f'Exibindo os elementos do dicionário 01 após adicionar três pares cujas chaves são 110, 178 e 156 e os valores são Café, Óleo e Ervilha: \n{dictionary_01}\n')

keys = dictionary_01.keys()
print(f'Exibindo as chaves dos elementos do dicionário 01: \n{keys}\n')

print('Exibindo as chaves dos elementos do dicionário 01 por meio da iteração do laço de repetição for:')
for counter in keys:
    print(counter)
    
values = dictionary_01.values()
print(f'\nExibindo os valores dos elementos do dicionário 01: \n{values}\n')

print('Exibindo os valores dos elementos do dicionário 01 por meio da iteração do laço de repetição for:')
for counter in values:
    print(counter)

items = dictionary_01.items()
print(f'\nExibindo os itens dos elementos do dicionário 01: \n{items}\n')

print('Exibindo os itens dos elementos do dicionário 01 por meio da iteração do laço de repetição for:')
for counter in items:
    print(counter)

print('\nA execução do sistema informático foi concluída.')