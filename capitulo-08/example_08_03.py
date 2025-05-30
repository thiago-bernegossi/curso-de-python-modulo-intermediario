# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_08_03.py
# DATA DE CRIAÇÃO: 30-05-2025
# DATA DE PUBLICAÇÃO: 30-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Intermediário
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

codes = [103, 117, 121, 135, 161, 189, 200, 284, 216]
final_list = []

print('Exemplo de uso clássico de if:')

for code in codes:
    if 120 <= code and code <= 200:
        final_list.append(code)
print(f'A lista final é {final_list}\n')

final_list = []

print('Exemplo de uso conciso (em linha única) de if:')

for code in codes:
    final_list.append(code) if 120 <= code and code <= 200 else 0
print(f'A lista final é {final_list}')

print('\nA execução do sistema informático foi concluída.')