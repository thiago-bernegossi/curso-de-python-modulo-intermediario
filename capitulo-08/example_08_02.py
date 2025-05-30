# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_08_02.py
# DATA DE CRIAÇÃO: 30-05-2025
# DATA DE PUBLICAÇÃO: 30-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Intermediário
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

object_x = 10
object_y = 9

if object_x >= object_y:
    print(f'O valor de X é {object_x}\n')
else:
    print(f'O valor de Y é {object_y}\n')

print(f'O valor de X é {object_x}\n') if object_x >= object_y else print(f'O valor de Y é {object_y}\n')

object_y = 11

print(f'O valor de X é {object_x}\n') if object_x >= object_y else print(f'O valor de Y é {object_y}\n')

print('A execução do sistema informático foi concluída.')