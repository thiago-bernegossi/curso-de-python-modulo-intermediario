# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_10_01.py
# DATA DE CRIAÇÃO: 08-06-2025
# DATA DE PUBLICAÇÃO: 08-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 01:
# Escreva um programa que leia do teclado o código de um produto e seu preço unitário.
# O código é um string e o preço é real. Acrescente o par código:preço em um dicionário.
# O laço termina quando for fornecido um string vazio para o código.
# Ao final, exibir código e preço, um produto em cada linha. 

# Resolução do Exercício 01:
print('A execução do sistema informático foi iniciada.\n')

print('Olá, vamos exibir o preço unitário de um produto de acordo com o respectivo código:\n')

print('A leitura dos valores foi iniciada...\n')

products = {}
code = input('Digite o código do produto: ')
while code != '':
    price = float(input('Digite o preço unitário do produto: '))
    products[code] = price
    code = input('Digite o código do produto: ')

print('\nA leitura dos valores foi concluída.\n')

print('O resultado é:')
for code in products.keys():
    print(f'O produto {code} custa R$ {products[code]}')

print(f'\nA execução do sistema informático foi concluída.')