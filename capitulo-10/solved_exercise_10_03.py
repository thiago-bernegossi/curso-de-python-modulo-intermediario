# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_10_03.py
# DATA DE CRIAÇÃO: 09-06-2025
# DATA DE PUBLICAÇÃO: 10-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 03:
# Escreva um programa que leia dados dos estados brasileiros: Sigla, Nome, Capital e PIB.
# A Sigla deve ser usada como chave para o dicionário e o valor deve ser uma tupla formada com (Nome, Capital, PIB).
# A leitura termina quando um string vazio for fornecido para a Sigla.
# Exibir os dados na tela. 

# Resolução do Exercício 03:
print('A execução do sistema informático foi iniciada.\n')

print('Olá, vamos exibir os dados dos estados do Brasil:\n')

print('A leitura dos valores foi iniciada...\n')

states = {}
while True:
    code = input('Digite a sigla do estado: ')
    if code == '':
        break
    elif code in states:
        print(f'A sigla {code} já foi digitada!')
        continue
    state = input('Digite o nome do estado: ') 
    capital = input('Digite a capital do estado: ') 
    gdp = float(input('Digite o PIB do estado: ')) 
    states[code] = (state, capital, gdp) 
print('\nA leitura dos valores foi concluída.\n')

print('O resultado é:')
for counter in states.items():
    print(counter)

print('\nO resultado é:')
print('     {:15} {:15} {:>10}'.format('Estado', 'Capital', 'PIB (R$ Bilhões)')) 
for code, values in states.items(): 
    print('({}) {:15} {:15} {:10.1f}'.format( 
        code, 
        values[0], 
        values[1], 
        values[2]) 
    )

print(f'\nA execução do sistema informático foi concluída.')