# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_12_05.py
# DATA DE CRIAÇÃO: 16-06-2025
# DATA DE PUBLICAÇÃO: 16-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 05:
# Escreva um programa que leia quatro notas de um aluno, calcule a média e mostre a situação do aluno que será 'APROVADO' ou 'REPROVADO'.
# O programa deve ler as quatro notas separadas por um espaço em branco em uma mesma linha de digitação.
# As notas lidas devem ser separadas, convertidas para número real e inseridas em uma lista, junto com a média e a situação do aluno.
# Isso tudo deverá ser feito dentro de uma função.
# Médias a partir de 7.0 indicam aprovação; menos que isso reprovação.
# A ordem das notas na digitação deve ser: P1 P2 P3 NT.
# Escreva o programa principal para testar sua função.
# A saída deste programa deve mostrar todas as notas, a média e a situação (você é livre para elaborar o layout de saída).

# Cálculo da Média do Exercício 05:
# MF = 0.3 * P1 + 0.3 * P2 + 0.3 * P3 + 0.1 * NT

# Resolução do Exercício 05:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma função que leia quatro notas, calcule e retorne a média e a situação final do(a) aluno(a):\n')

def calculate_average(grade_values):
    grade_values = grade_values.split()
    for value in range(len(grade_values)):
        grade_values[value] = float(grade_values[value])
    average = (grade_values[0] + grade_values[1] + grade_values[2]) * 0.3 + grade_values[3] * 0.1
    student_situation = 'APROVADO' if average >= 7 else 'REPROVADO'
    grade_values.append(average)
    grade_values.append(student_situation)
    return grade_values
 
new_grade_values = input('Digite os valores das notas (P01 P02 P03 NT): ')
result = calculate_average(new_grade_values)
print(f'O valor da Prova 01 (P01) é: {result[0]:.1f}', end='')
print(f'\nO valor da Prova 02 (P02) é: {result[1]:.1f}', end='') 
print(f'\nO valor da Prova 03 (P03) é: {result[2]:.1f}', end='')
print(f'\nO valor da Nota de Trabalho (NT) é: {result[3]:.1f}', end='')

print('\n\nO resultado é:')
print(f'O valor da média do(a) aluno(a) é: {result[4]:.1f}', end='')
print(f'\nA situação do(a) aluno(a) é: {result[5]}')

print(f'\nA execução do sistema informático foi concluída.')