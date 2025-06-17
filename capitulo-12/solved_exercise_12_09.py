# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_12_09.py
# DATA DE CRIAÇÃO: 17-06-2025
# DATA DE PUBLICAÇÃO: 17-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 09:
# Escreva um programa que implemente uma busca binária através de uma função recursiva.
# O programa principal deve permanecer em laço lendo valores inteiros que devem ser buscados na lista.

# Casos de Teste do Exercício 09:
# Neste exercício será usada uma lista contendo valores fixos e que foi apresentada na figura 12.5.
# O objetivo é que você possa testar o programa com os valores como mostrado aqui.

# Resolução do Exercício 09:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma função recursiva que implementa uma busca binária usando uma função recursiva: \n')

def binary_search(value, list, initial_value, final_value): 
    if initial_value > final_value: 
        return False 
    middle_value = (initial_value + final_value) // 2 
    if value == list[middle_value]: 
        return True 
    elif value < list[middle_value]:
        return binary_search(value, list, initial_value, middle_value - 1)
    else:
        return binary_search(value, list, middle_value + 1, final_value)
 
fixed_values = [14, 17, 20, 22, 23, 25, 28, 29, 31, 35, 40, 45, 50, 53, 56, 59, 62, 65]
search_value = int(input('Digite um número inteiro para pesquisar na lista: '))

while search_value != 0:
    value_found = binary_search(search_value, fixed_values, 0, len(fixed_values) - 1)
    if value_found != 0:
        print(f'\nO número inteiro {search_value} já está na lista!')
    else:
        print(f'\nO número inteiro {search_value} não está na lista...')
    search_value = int(input('\nDigite outro número inteiro para pesquisar na lista: '))

print(f'\nA execução do sistema informático foi concluída.')