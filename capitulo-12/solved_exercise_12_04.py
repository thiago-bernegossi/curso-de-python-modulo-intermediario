# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_12_04.py
# DATA DE CRIAÇÃO: 16-06-2025
# DATA DE PUBLICAÇÃO: 16-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 04:
# Escreva uma função que receba como parâmetro de entrada dois números reais Min e Max.
# Essa função deve ler do teclado um número real e retorná-lo caso esteja dentro do intervalo fechado [Min, Max].
# Caso contrário, a função deve exibir uma mensagem de erro e ler um novo valor.

# Resolução do Exercício 04:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma função que leia um número real e verifique se há ocorrência do mesmo em um determinado intervalo:\n')

def read_real_number(minimum_value, maximum_value):
    value = float(input('\nDigite um número real: '))
    while value < minimum_value or value > maximum_value:
        print(f'O valor {value} está fora do intervalo, compreendido entre o valor mínimo {minimum_value} e o valor máximo {maximum_value}.\n')
        value = float(input('Digite outro número real: '))
    return value
    
new_minimum_value = float(input('Digite o valor mínimo: '))
new_maximum_value = float(input('Digite o valor máximo: '))
exit_code = 'Sim'

while exit_code == 'Sim' or exit_code == "SIM" or exit_code == 's' or exit_code == 'S':
    new_value = read_real_number(new_minimum_value, new_maximum_value)
    print(f'O valor digitado é {new_value}\n')
    exit_code = input(f'Gostaria de digitar outro valor (Sim / Não): ')

print(f'\nA execução do sistema informático foi concluída.')