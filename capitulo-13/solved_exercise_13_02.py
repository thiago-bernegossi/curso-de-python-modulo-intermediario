# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_13_02.py
# DATA DE CRIAÇÃO: 18-06-2025
# DATA DE PUBLICAÇÃO: 18-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 02:
# Escreva um programa que converta uma lista de temperaturas registradas na escala Fahrenheit para graus na escala Celsius.
# Exiba os valores resultantes com uma casa decimal.
# A conversão é feita com uso da seguinte fórmula:
# Celsius = (Fahrenheit − 32) * 5 / 9 

# Resolução do Exercício 02:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar um conversor de temperaturas registradas na escala Fahrenheit para a escala Celsius:\n')

temperature_Fahrenheit = [83, 91, 79, 95, 104, 100, 98]
temperature_Celsius = [(lambda fahrenheit: (fahrenheit - 32) * 5 / 9)(value) for value in temperature_Fahrenheit]

print('O resultado é:')
for converted_value in temperature_Celsius:
    print(f'{converted_value:.1f}', end='   ')

print(f'\n\nA execução do sistema informático foi concluída.')