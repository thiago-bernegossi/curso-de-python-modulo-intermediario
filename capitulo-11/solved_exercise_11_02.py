# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_11_02.py
# DATA DE CRIAÇÃO: 11-06-2025
# DATA DE PUBLICAÇÃO: 11-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 02:
# Escreva um programa que permaneça em laço lendo números reais até que seja digitado 0.
# Todos os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha, com três casas decimais.
# Usar o método .writelines().

# Resolução do Exercício 02:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos construir um arquivo que irá exibir uma sequência de números reais que foram digitados e gravados:\n')

list_of_numbers = []
value = float(input('Digite um número real: '))
while value != 0:
    list_of_numbers.append(f'{value:.3f}\n')
    value = float(input('Digite um número real: '))

print('\nO resultado é:')
print(list_of_numbers)

file = open('solved_exercise_11_02.txt', 'w')
file.writelines(list_of_numbers)
file.close()

print(f'\nA execução do sistema informático foi concluída.')