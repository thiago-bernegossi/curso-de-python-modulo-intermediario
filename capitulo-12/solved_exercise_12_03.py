# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_12_03.py
# DATA DE CRIAÇÃO: 16-06-2025
# DATA DE PUBLICAÇÃO: 16-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 03:
# Escreva uma função que receba como parâmetro de entrada um número inteiro de 5 dígitos de [10000, 99999] que represente códigos de produtos vendidos em uma loja.
# A função deve calcular e retornar o dígito verificador utilizando a regra de cálculo explicada a seguir.
# Escreva o programa principal para testar a função.

# Regra do Exercício 03:
# Considere o código 31483, em que cada dígito é multiplicado por um peso começando em 2 e terminando em 6.
# Os valores obtidos são somados, e do total obtido calcula-se o resto de sua divisão por 7.

# +---------------+-----+-----+-----+-----+-----+-----------------------+
# | Dígito        |  3  |  1  |  4  |  8  |  3  |                       |
# +---------------+-----+-----+-----+-----+-----+-----------------------+
# | Peso          |  2  |  3  |  4  |  5  |  6  |                       |
# +---------------+-----+-----+-----+-----+-----+-----------------------+
# | Multiplicação |  6  |  3  | 16  | 40  | 18  | Soma todos = 83       |
# +---------------+-----+-----+-----+-----+-----+-----------------------+
# |               |     |     |     |     |     | Resto de 83 por 7 = 6 |
# +---------------+-----+-----+-----+-----+-----+-----------------------+

# Resolução do Exercício 03:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma função que leia um código de produto, calcula e retorna seu dígito verificador:\n')

def calculate_check_digit(product_code):
    string = str(product_code)
    product_weight = 2
    check_digit = 0
    for value in string:
        check_digit += product_weight * int(value)
        product_weight += 1
    return check_digit % 7

product_code = int(input('Digite o código do produto: '))

while product_code > 0:
    new_check_digit = calculate_check_digit(product_code)
    print('\nO resultado é:')
    print(f'O código do produto é {product_code} e o dígito verificador é {new_check_digit}\n')
    product_code = int(input('Digite o código do produto: '))

print(f'\nA execução do sistema informático foi concluída.')