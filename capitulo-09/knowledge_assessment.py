# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: knowledge_assessment.py
# DATA DE CRIAÇÃO: 04-06-2025
# DATA DE PUBLICAÇÃO: 04-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Intermediário
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Questão 01-) Considere a definição do conjunto C e a impressão de seus elementos como segue:
C = set([2, 4, 8, 3, 9, 27, 4, 16, 64])
for elemento in C:
    print(elemento)
# Como será apresentada a sequência de elementos impressos?
# Resposta: c. Numa ordem decidida pelo interpretador Python.

# Questão 02-) Considere a definição dos dois conjuntos A e B que segue:
A = set('tiotimolina')
B = set('asimov')
# Qual é o resultado das operações A & B, A - B e A ^ B?
# Resposta: a. {'a', 'i', 'o', 'm'}, {'n', 't', 'l'}, {'l', 's', 't', 'n', 'v'}