# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_12_09.py
# DATA DE CRIAÇÃO: 14-06-2025
# DATA DE PUBLICAÇÃO: 14-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

def create_output(*values, separator=', '):
    output = separator.join(values)
    return output

print(create_output('Abacaxi', 'Ameixa', 'Laranja', 'Limão', 'Maçã', 'Uva'))
print(create_output(f'\nAbacaxi', 'Ameixa', 'Laranja', 'Limão', 'Maçã', 'Uva', separator='... '))
print(create_output(f'\nAbacaxi', 'Ameixa', 'Laranja', 'Limão', 'Maçã', 'Uva', separator=' --- '))
print(create_output(f'\nAbacaxi', 'Ameixa', 'Laranja', 'Limão', 'Maçã', 'Uva', '---'))

print(f'\nA execução do sistema informático foi concluída.')