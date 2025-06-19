# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_13_01.py
# DATA DE CRIAÇÃO: 18-06-2025
# DATA DE PUBLICAÇÃO: 18-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 01:
# Considere que você deve aplicar um aumento percentual a todos os preços que estão em uma lista.
# Escreva um programa que leia essa lista do teclado.
# Os valores devem ser lidos enquanto não for digitado zero.
# Na sequência leia a porcentagem de aumento.
# Em seguida, usando list comprehension, faça a aplicação desse aumento a todos os valores e mostre na tela. 

# Resolução do Exercício 01:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma lista de preços, depois aplicar uma porcentagem de aumento com list comprehension e exibir os resultados:\n')

price_list = []
price = float(input('Digite o preço do produto em número real: '))

while price != 0:
    price_list.append(price)
    price = float(input('Digite o preço do produto em número real: '))

print(f'\nExibindo a lista com os preços digitados: {price_list}')
 
percentage_increase = float(input('\nDigite a porcentagem de aumento do preço (sem o símbolo %): '))
new_values = [value * (1 + percentage_increase / 100) for value in price_list]

print('\nO resultado é:')
for value in new_values:
    print(f'{value:.2f}')

print(f'\nA execução do sistema informático foi concluída.')