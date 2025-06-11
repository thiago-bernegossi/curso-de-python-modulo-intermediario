# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_11_05.py
# DATA DE CRIAÇÃO: 11-06-2025
# DATA DE PUBLICAÇÃO: 11-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 05:
# Escreva um programa que leia um arquivo de entrada carregando seus dados em um dicionário e ao final exibindo-os na tela.
# A figura 11.1 mostra do lado esquerdo a natureza dos dados que serão lidos e do lado direito mostra o formato do arquivo.
# Esse formato é conhecido como CSV. Arquivos CSV são muito usados em diversas áreas da computação, em especial em Análise de Dados.
# O que caracteriza um arquivo CSV é que cada linha tem um conjunto de dados de alguma forma relacionados e separados por um caractere delimitador.
# No arquivo deste exercício o delimitador é um ponto-e-vírgula ";".
# Neste caso, cada linha tem: código de produto (int), a quantidade em estoque (int), preço (float).
# Use o código como chave para o dicionário e o valor deve ser em formato de tupla.

# Resolução do Exercício 05:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos ler um arquivo CSV separado por “;”, armazenar cada linha como tupla (código, quantidade, preço) em um dicionário indexado pelo código-fonte e, em seguida, exibir tudo na tela.\n')

product_stock = {}
for line in open('solved_exercise_11_05.csv'):
    list = line.rstrip().split(';')
    code = int(list[0])
    quantity = int(list[1])
    price = float(list[2])
    product_stock[code] = (quantity, price)

print('O resultado é:')
print(f'Exibindo os elementos presentes no arquivo: {product_stock}\n')

print(f'Exibindo os elementos presentes no arquivo em formato de tabela:')
total_products = 0 
for code, values in product_stock.items(): 
    total = values[0] * values[1]
    total_products += total
    print(f' {code}: {values[0]:5d} x {values[1]:6.2f} = {total:8.2f}')
print(' ' * 22, f'{total_products:8.2f}')

print(f'\nA execução do sistema informático foi concluída.')