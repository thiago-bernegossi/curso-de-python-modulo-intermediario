# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_12_02.py
# DATA DE CRIAÇÃO: 12-06-2025
# DATA DE PUBLICAÇÃO: 12-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

def read_integers():
    number = int(input('Digite um número inteiro: '))
    return number

value = read_integers()
print(f'\nO número inteiro digitado e lido pela função foi: {value}.')

print(f'\nA execução do sistema informático foi concluída.')