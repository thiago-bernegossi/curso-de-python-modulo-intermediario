# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_11_01.py
# DATA DE CRIAÇÃO: 11-06-2025
# DATA DE PUBLICAÇÃO: 11-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 01:
# Escreva um programa que permaneça em laço lendo números inteiros até que seja digitado 0.
# Todos os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha.
# Usar o método .write(). 

# Resolução do Exercício 01:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos construir um arquivo que irá exibir uma sequência de números inteiros que foram digitados e gravados:\n')

file = open('solved_exercise_11_01.txt', 'w')
value = int(input('Digite um número inteiro: '))
while value != 0:
    file.write(f'{value}\n')
    value = int(input('Digite um número inteiro: '))
file.close()

print(f'\nA execução do sistema informático foi concluída.')