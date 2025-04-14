# PYTHON PARA DATA SCIENCE - PANDAS

# para rodar este arquivo, rode o seguinte comando no terminal ou prompt de comando:
# python pandas_aula_5.py

# 5. PANDAS BÁSICO
# Pandas é uma ferramenta de manipulação de dados de alto nível, construída com base no pacote Numpy. O pacote pandas possui estruturas de dados bastante interessantes para manipulação de dados e por isso é muito utilizado por cientistas de dados.

# Series
# Series são arrays unidimensionais rotulados capazes de armazenar qualquer tipo de dado. Os rótulos das linhas são chamados de index.
# A forma básica de criação de uma Series é a seguinte:
# s = pd.Series(dados, index = index)

# DataFrames
# DataFrame é uma estrutura de dados tabular bidimensional com rótulos nas linha e colunas. 
# Como a Series, os DataFrames são capazes de armazenar qualquer tipo de dados.
# df = pd.DataFrame(dados, index = index, columns = columns)

#5.1 Estruturas de dados

import pandas as pd

# Criando uma Series a partir de uma lista
carros = ['jetta variant', 'passat', 'crossfox']
carros
pd.Series(carros)
print(pd.Series(carros))

input("_________________________ Pressione Enter para continuar...")

dados = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False, 'Valor': 88078.64},
    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False, 'Valor': 106161.94},
    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False, 'Valor': 72832.16}
]
dataset = pd.DataFrame(dados)
print(dataset)

input("_________________________ Pressione Enter para continuar...")
dataset = pd.read_csv('db.csv', sep = ';', index_col = 0)
print(dataset)
input("_________________________ Pressione Enter para continuar...")

print('Exercicio')
dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}
def km_media(dataset, ano_atual):
    result = {}
    for item in dataset.items():
        media = item[1]['km'] / (ano_atual - item[1]['ano'])
        item[1].update({ 'km_media': media })
        result.update({ item[0]: item[1] })

    return result

carros = pd.DataFrame(km_media(dados, 2019)).T
print(carros)