# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_12_15.py
# DATA DE CRIAÇÃO: 15-06-2025
# DATA DE PUBLICAÇÃO: 15-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

product_list = {'121': 23.90, '189': 14.33, '152': 36.95, '175': 19.35} 

print(f'Exibindo a lista de produtos ordenada pelas chaves e sem os valores: {sorted(product_list)}\n')

print(f'Exibindo a lista de produtos ordenada pelas chaves e com os valores: {sorted(product_list.items())}\n')

print(f'Exibindo a lista de produtos ordenada pelos valores e com as chaves: {sorted(product_list.items(), key=lambda x: x[1])}')

print(f'\nA execução do sistema informático foi concluída.')