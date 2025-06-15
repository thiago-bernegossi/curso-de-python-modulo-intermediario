# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_12_12.py
# DATA DE CRIAÇÃO: 15-06-2025
# DATA DE PUBLICAÇÃO: 15-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos construir uma função que leia um número inteiro e retorne o seu fatorial:\n')

def display_factorial(number):
    if number <= 1:
        return 1
    else:
        return number * display_factorial(number - 1)
    
number = int(input('Digite um número inteiro: '))
final_value = display_factorial(number)

print(f'\nO fatorial de {number} é: {final_value}')

print(f'\nA execução do sistema informático foi concluída.')