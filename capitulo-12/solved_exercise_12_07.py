# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_12_07.py
# DATA DE CRIAÇÃO: 17-06-2025
# DATA DE PUBLICAÇÃO: 17-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 07:
# Escreva um programa que utilize uma função recursiva para realizar uma contagem regressiva.
# Este programa deve ler do teclado um inteiro que representa a quantidade de toques dessa contagem regressiva.
# Quando a contagem chegar em zero o programa deve exibir na tela a mensagem "NO AR!!!".

# Resolução do Exercício 07:
from time import sleep

print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma função que leia um número inteiro e realiza uma contagem regressiva:\n')

def countdown(count):
    if count == 0:
        print('NO AR!!!')
    else: 
        print(count)
        sleep(1)      
        countdown(count-1)

countdown_touches = int(input('Digite a quantidade de toques da contagem regressiva: '))

print('\nO resultado é:')
print(f'Atenção para o toque de {countdown_touches} segundos...')
countdown(countdown_touches)

print(f'\nA execução do sistema informático foi concluída.')