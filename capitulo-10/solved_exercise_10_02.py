# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_10_02.py
# DATA DE CRIAÇÃO: 09-06-2025
# DATA DE PUBLICAÇÃO: 09-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 02:
# Escreva um programa que leia do teclado o código de um produto e seu preço unitário.
# O código é um string e o preço é real. Acrescente o par código:preço em um dicionário.
# O programa deve verificar se o código já está no dicionário e neste caso deve emitir uma mensagem de erro.
# O laço termina quando for fornecido um string vazio para o código.
# Ao final, exibir código e preço, um produto em cada linha. 

# Resolução do Exercício 02:
print('A execução do sistema informático foi iniciada.\n')

print('Olá, vamos exibir o preço unitário de um produto de acordo com o respectivo código:\n')

print('A leitura dos valores foi iniciada...\n')

products = {}
while True:
    code = input('Digite o código do produto: ')
    if code == '':
        break
    elif code in products:
        print(f'O código {code} já foi digitado!')
        continue
    price = float(input('Digite o preço unitário do produto: '))
    products[code] = price
print('\nA leitura dos valores foi concluída.\n')

print('O resultado é:')
for code in products.keys():
    print(f'O produto {code} custa R$ {products[code]}')

print(f'\nA execução do sistema informático foi concluída.')