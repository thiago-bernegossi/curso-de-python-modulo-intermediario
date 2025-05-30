# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_08_01.py
# DATA DE CRIAÇÃO: 30-05-2025
# DATA DE PUBLICAÇÃO: 30-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Intermediário
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

object_n = -1

while object_n != 0:
    object_n = int(input('Digite um número inteiro: '))
    match object_n:
        case 1:
            print('Você digitou o número: 1\n')
        case 2:
            print('Você digitou o número: 2\n')
        case 3:
            print('Você digitou o número: 3\n')
        case _:
            print('Você digitou outro número...\n')

print('A execução do sistema informático foi concluída.')