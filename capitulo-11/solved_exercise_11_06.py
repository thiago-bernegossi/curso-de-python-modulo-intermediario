# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_11_06.py
# DATA DE CRIAÇÃO: 11-06-2025
# DATA DE PUBLICAÇÃO: 11-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 06:
# Neste exercício vamos verificar como funciona a codificação dos arquivos texto em Python.
# Escreva um programa que grave as duas linhas de texto abaixo em um arquivo.
# Em seguida leia esse arquivo e mostre na tela o que foi lido.
# As codificações que vamos testar são ANSI e UTF-8 e elas deverão ser lidas do teclado.
# Texto a ser gravado no arquivo:
# Gravação do arquivo 
# Acentos: á, é, í, Á, É, Í, ç, Ç 

# Resolução do Exercício 06:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos testar a codificação de arquivos texto em Python, gravando e lendo um arquivo com ANSI e UTF-8, inserindo acentos e exibindo o conteúdo na tela.\n')

write = input('Digite a codificação de caracteres para a gravação do arquivo: ')
read = input('Digite a codificação de caracteres para a leitura do arquivo: ')

print('\nA gravação do arquivo foi iniciada...')

file = open('solved_exercise_11_06.txt', 'w', encoding=write)
file.write('Gravação do arquivo\n')
file.write('Acentos: á, é, í, Á, É, Í, ç, Ç\n') 
file.close()

print('A gravação do arquivo foi concluída.\n')

print('A leitura do arquivo foi iniciada...\n')

print('O resultado é:')
file = open('solved_exercise_11_06.txt', 'r', encoding=read)
line = file.readline()
print(line.rstrip())
line = file.readline()
print(line.rstrip())
file.close()

print('\nA leitura do arquivo foi concluída.')

print(f'\nA execução do sistema informático foi concluída.')