# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_12_08.py
# DATA DE CRIAÇÃO: 17-06-2025
# DATA DE PUBLICAÇÃO: 17-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 08:
# Escreva uma função recursiva para calcular a somatória dos termos de uma Progressão Aritmética definida pelos parâmetros Prim (primeiro termo), Razao e Qtde (quantidade de elementos).
# Esses parâmetros devem ser lidos do teclado.
# Escreva o programa principal para testar a função, que deve exibir na tela o valor dessa soma.
# Teste seu programa com os casos de teste a seguir.

# Casos de Teste do Exercício 08:
# para Prim = 7; Razao = 4; Qtde = 7 → Soma = 133
# para Prim = 12; Razao = 8; Qtde = 15 → Soma = 1020
# para Prim = 2; Razao = 3; Qtde = 6 → Soma = 57

# Resolução do Exercício 08:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma função recursiva para somar os termos de uma Progressão Aritmética:\n')

def calculateSum(first_term, ratio, number_of_terms):
    if number_of_terms > 0:
        final_value = first_term + calculateSum(first_term + ratio, ratio, number_of_terms - 1) 
        return final_value
    else: 
        return 0

first_term = int(input('Digite o primeiro termo: '))
ratio = int(input('Digite a razão: '))
number_of_terms = int(input('Digite a quantidade de termos: '))

print('\nO resultado é:')
print(f'A soma dos termos é {calculateSum(first_term, ratio, number_of_terms)} e os valores digitados foram {first_term} (primeiro termo), {ratio} (razão) e {number_of_terms} (quantidade de termos)')

print(f'\nA execução do sistema informático foi concluída.')