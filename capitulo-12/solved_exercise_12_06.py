# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_12_06.py
# DATA DE CRIAÇÃO: 16-06-2025
# DATA DE PUBLICAÇÃO: 16-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 06:
# Escreva um programa que verifique se um número inteiro lido é primo.
# Lembrando: um número primo é divisível apenas por 1 e por ele mesmo.
# A verificação do primo deve ser feita dentro de uma função.

# Resolução do Exercício 06:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma função que leia um número inteiro e informe se ele é um número primo:\n')

def verify_prime_number(prime_number): 
    if prime_number == 2:
        return True 
    elif prime_number % 2 == 0: 
        return False 
    else: 
        square_root = pow(prime_number, 0.5) 
        value = 3 
        while value <= square_root: 
            if prime_number % square_root == 0: 
                return False 
            value += 2 
        return True
 
number = int(input('Digite um número inteiro: '))

print('\nO resultado é:')
if verify_prime_number(number): 
    print(f'O número {number} é primo') 
else: 
    print(f'O número {number} não é primo')

print(f'\nA execução do sistema informático foi concluída.')