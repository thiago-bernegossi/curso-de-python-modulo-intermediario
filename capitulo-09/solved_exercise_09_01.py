# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_09_01.py
# DATA DE CRIAÇÃO: 04-06-2025
# DATA DE PUBLICAÇÃO: 04-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 01:
# Escreva um programa que leia um inteiro Qtde e crie um conjunto com elementos numéricos inteiros aleatórios dentro do intervalo fechado [1, 50].
# Mostre o conjunto gerado na tela. 
# Lembre-se que os conjuntos não podem ter elementos repetidos, então a geração de números aleatórios pode representar um problema.
# Como resolver isso?
 
# Cuidado do Exercício 01: 
# Este programa tem potencial para entrar em laço infinito caso o valor fornecido para Qtde seja maior que 50.
# Faça o teste e depois responda a pergunta: por que isso ocorre?

# Resolução do Exercício 01:
from random import randint

print('A execução do sistema informático foi iniciada.\n')

print('Olá, vamos criar um conjunto de números inteiros aleatórios:\n')

value = int(input('Digite um número inteiro: '))
while value > 50:
    print('\nO valor não pode ser superior a 50!')
    value = int(input('Digite outro número inteiro: '))

set_01 = set()
while len(set_01) < value:
    set_01.add(randint(1, 50))

print(f'\nO resultado é: {set_01}')
print(f'O conjunto contém {len(set_01)} número(s) inteiro(s) aleatório(s).')

print(f'\nA execução do sistema informático foi concluída.')