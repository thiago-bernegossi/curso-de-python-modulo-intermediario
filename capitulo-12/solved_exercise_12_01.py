# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_12_01.py
# DATA DE CRIAÇÃO: 15-06-2025
# DATA DE PUBLICAÇÃO: 15-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 01:
# Escreva uma função que recebe um número inteiro como parâmetro de entrada e retorna o texto "PAR" ou "ÍMPAR".
# Use-a em um programa principal.
  
# Resolução do Exercício 01:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos construir uma função que leia um número inteiro e informe se o número é par ou ímpar:\n')

def verify_number(number):
    return 'PAR'if number % 2 == 0 else 'ÍMPAR'

number = int(input('Digite um número inteiro: '))

print('\nO resultado é:')
print(f'O número inteiro digitado e lido pela função é: {verify_number(number)}')

print(f'\nA execução do sistema informático foi concluída.')