# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_09_05.py
# DATA DE CRIAÇÃO: 03-06-2025
# DATA DE PUBLICAÇÃO: 03-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Intermediário
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

set_01 = set()
print(f'Exibindo o número de elementos do conjunto 01: {len(set_01)}')
print(f'Exibindo os elementos do conjunto 01: {set_01}')
print(f'Exibindo o tipo de objeto do conjunto 01: {type(set_01)}\n')

set_01.add(85)
print(f'Exibindo os elementos do conjunto 01 após adicionar um elemento cujo valor é 85: {set_01}\n')

set_01.add(190)
set_01.add(32)
set_01.add(76)
print(f'Exibindo os elementos do conjunto 01 após adicionar três elementos cujos valores são 190, 32 e 76: {set_01}\n')

set_01.add(32.4)
print(f'Exibindo os elementos do conjunto 01 após adicionar um elemento cujo valor é 32.4: {set_01}\n')

set_01.clear()
print(f'Exibindo os elementos do conjunto 01 após limpar seus elementos: {set_01}\n')

set_01 = {36, 77, 81, 43, 18}
print(f'Exibindo os elementos do conjunto 01 após adicionar cinco elementos cujos valores são 36, 77, 81, 43 e 18: {set_01}\n')

set_02 = set_01.copy()
print(f'Exibindo os elementos do conjunto 02 após seus elementos serem copiados do conjunto 01: {set_02}\n')

print(f'Exibindo o identificador do conjunto 01: {id(set_01)}')
print(f'Exibindo o identificador do conjunto 02: {id(set_02)}\n')

set_01.clear()
set_02.clear()

set_01 = {26, 32, 45, 58, 63}
set_02 = {19, 34, 58, 67, 82}
print(f'Exibindo os elementos diferentes entre o conjunto 01 e o conjunto 02: {set_01.difference(set_02)}\n')

set_02 = {19, 34, 58, 67, 82, 63}
print(f'Exibindo os elementos diferentes entre o conjunto 01 e o conjunto 02: {set_01.difference(set_02)}\n')

set_03 = set_01.difference(set_02)
print(f'Exibindo os elementos diferentes entre o conjunto 01 e o conjunto 02: {set_03}\n')

set_01.difference_update(set_02)
print(f'Exibindo os elementos diferentes entre o conjunto 01 e o conjunto 02 e atualizando o conjunto 01: {set_01}\n')

print(f'Exibindo os elementos do conjunto 01: {set_01}')
print(f'Exibindo os elementos do conjunto 02: {set_02}\n')

set_02.discard(58)
print(f'Exibindo os elementos do conjunto 02 após remover um elemento cujo valor é 58: {set_02}\n')

print(f'Exibindo os elementos do conjunto 01: {set_01}')
print(f'Exibindo os elementos do conjunto 02: {set_02}\n')

set_01.add(82)
set_01.add(34)
print(f'Exibindo os elementos do conjunto 01 após adicionar dois elementos cujos valores são 82 e 34: {set_01}\n')

print(f'Exibindo os elementos comuns entre o conjunto 01 e o conjunto 02: {set_01.intersection(set_02)}')

set_03 = set_01.intersection(set_02)
print(f'Exibindo os elementos comuns entre o conjunto 01 e o conjunto 02: {set_03}\n')

set_01.intersection_update(set_02)
print(f'Exibindo os elementos comuns entre o conjunto 01 e o conjunto 02 e atualizando o conjunto 01: {set_01}\n')

print(f'Exibindo os elementos do conjunto 01: {set_01}')
print(f'Exibindo os elementos do conjunto 02: {set_02}\n')

set_01.add(50)
set_01.add(88)
set_01.add(17)
print(f'Exibindo os elementos do conjunto 01 após adicionar três elementos cujos valores são 50, 88 e 17: {set_01}')
print(f'Exibindo os elementos do conjunto 02: {set_02}\n')

set_01.discard(34)
set_01.discard(82)
print(f'Exibindo os elementos do conjunto 01 após remover dois elementos cujos valores são 34 e 82: {set_01}\n')

print(f'Verificando se há uma interseção nula entre o conjunto 01 e o conjunto 02: {set_01.isdisjoint(set_02)}\n')

print(f'Exibindo os elementos do conjunto 01: {set_01}')
print(f'Exibindo os elementos do conjunto 02: {set_02}\n')

print(f'Exibindo os elementos comuns entre o conjunto 01 e o conjunto 02: {set_01.intersection(set_02)}\n')

print(f'Verificando se o conjunto 01 é subconjunto do conjunto 02: {set_01.issubset(set_02)}')

set_02.add(50)
set_02.add(88)
set_02.add(17)
print(f'Verificando se o conjunto 01 é subconjunto do conjunto 02: {set_01.issubset(set_02)}\n')

print(f'Verificando se o conjunto 01 contém o conjunto 02: {set_01.issuperset(set_02)}')
print(f'Verificando se o conjunto 02 contém o conjunto 01: {set_02.issuperset(set_01)}\n')

print(f'Exibindo os elementos do conjunto 01: {set_01}')
set_01.pop()
print(f'Exibindo os elementos do conjunto 01 após remover um elemento: {set_01}')
set_01.pop()
print(f'Exibindo os elementos do conjunto 01 após remover outro elemento: {set_01}')
set_01.pop()
print(f'Exibindo os elementos do conjunto 01 após remover mais um elemento: {set_01}\n')

print(f'Exibindo os elementos do conjunto 02: {set_02}')
set_02.remove(17)
print(f'Exibindo os elementos do conjunto 02 após remover um elemento cujo valor é 17: {set_02}\n')

print(f'Verificando se o conjunto 02 contém um elemento cujo valor é 99: {99 in set_02}')
print(f'Verificando se o conjunto 02 contém um elemento cujo valor é 50: {50 in set_02}\n')

set_02.remove(50)
print(f'Exibindo os elementos do conjunto 02 após remover um elemento cujo valor é 50: {set_02}')

set_01 = {50, 16, 39, 88, 67}
set_03 = set_01.union(set_02)
print(f'Exibindo os elementos do conjunto 03 após os elementos do conjunto 01 serem unidos com os elementos do conjunto 02: {set_03}\n')

print(f'Exibindo a quantidade de elementos do conjunto 01: {len(set_01)}')
print(f'Exibindo a quantidade de elementos do conjunto 02: {len(set_02)}')
print(f'Exibindo a quantidade de elementos do conjunto 03: {len(set_03)}\n')

print(f'Exibindo os elementos comuns entre o conjunto 01 e o conjunto 02: {set_01.intersection(set_02)}\n')

print(f'Exibindo os elementos que não se sobrepõe entre o conjunto 01 e o conjunto 02: {set_01.symmetric_difference(set_02)}\n')

set_03 = set_01.copy()
print(f'Exibindo os elementos do conjunto 03: {set_03}\n')

set_03.symmetric_difference_update(set_02)
print(f'Exibindo os elementos que não se sobrepõe entre o conjunto 03 e o conjunto 02 e atualizando o conjunto 03: {set_03}\n')

print(f'Exibindo os elementos do conjunto 01: {set_01}')
print(f'Exibindo os elementos do conjunto 02: {set_02}\n')

set_01.update(set_02)
print(f'Atualizando os elementos do conjunto 01 após serem unidos com os elementos do conjunto 02: {set_01}')

print('\nA execução do sistema informático foi concluída.')