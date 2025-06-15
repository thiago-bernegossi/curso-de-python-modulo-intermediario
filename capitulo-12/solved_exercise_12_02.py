# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_12_02.py
# DATA DE CRIAÇÃO: 15-06-2025
# DATA DE PUBLICAÇÃO: 15-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 02:
# Escreva uma função que receba dois números inteiros A e B como parâmetros de entrada e retorne True se A for divisível por B e False caso contrário.
# Escreva o programa principal para testar a função.
  
# Resolução do Exercício 02:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos construir uma função que leia dois números inteiros e informe se o primeiro número é divisível pelo segundo número:\n')

def verify_number(object_a, object_b):
    return True if object_a % object_b == 0 else False

first_value = int(input('Digite um número inteiro: '))
second_value = int(input('Digite outro número inteiro: '))

print('\nO resultado é:')
print(f'O número {first_value} é divisível por {second_value}: {verify_number(first_value, second_value)}')

print(f'\nA execução do sistema informático foi concluída.')