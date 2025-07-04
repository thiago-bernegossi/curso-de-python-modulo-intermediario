# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_11_04.py
# DATA DE CRIAÇÃO: 11-06-2025
# DATA DE PUBLICAÇÃO: 11-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 04:
# Escreva um programa que permaneça que leia um arquivo de entrada, sabendo que esse arquivo tem um número inteiro em cada linha.
# Todos os números lidos devem ser mostrados na tela.
# Mostrar também a soma dos valores, a quantidade, a média aritmética, o menor valor e o maior valor.
# Usar aqui o mesmo arquivo de entrada do exercício anterior.
# Usar um iterador for e o arquivo como iterável. 

# Resolução do Exercício 04:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos ler um arquivo que contém uma sequência de números inteiros e depois calcular algumas operações matemáticas a partir deles:\n')

list_of_numbers = []
for line in open('solved_exercise_11_04.txt', 'r'):
    list_of_numbers.append(int(line))

print('O resultado é:')
print(f'Exibindo os elementos presentes no arquivo: {list_of_numbers}')

sum = sum(list_of_numbers)
print(f'Exibindo a soma dos valores presentes no arquivo: {sum}')
print(f'Exibindo a quantidade de elementos presentes no arquivo: {len(list_of_numbers)}')
print(f'Exibindo a média aritmética dos valores presentes no arquivo: {sum / len(list_of_numbers)}')
print(f'Exibindo o menor valor entre os elementos do arquivo: {min(list_of_numbers)}')
print(f'Exibindo o maior valor entre os elementos do arquivo: {max(list_of_numbers)}')

print(f'\nA execução do sistema informático foi concluída.')