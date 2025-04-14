# PYTHON PARA DATA SCIENCE - PANDAS

# para rodar este arquivo, rode o seguinte comando no terminal ou prompt de comando:
# python pandas_aula_3.4.py

# 3.4 Iterando em dicionários

# Retorna uma lista contendo as chaves (keys) do dicionário.
dados = {'Crossfox': 72832.16, 'DS5': 124549.07, 'Jetta Variant': 88078.64, 'Fusca': 150000, 'Passat': 106161.95}
print(dados)

input("Pressione Enter para continuar...")

# Retorna uma lista contendo as chaves (keys) do dicionário.
print('Todas as chaves do dicionário')
print(dados.keys())

print('Todas as chaves do dicionário')
for key in dados.keys():
  print(dados[key])

input("Pressione Enter para continuar...")

print('Todos os valores do dicionário')
print(dados.values())

# Retorna uma lista contendo uma tupla para cada par chave-valor (key-value) do dicionário.
print('Tupla por chave-valor')
print(dados.items())

input("Pressione Enter para continuar...")

# For em todos os itens do dicionario DADOS:
print('todos os itens')
for item in dados.items():
  print(item)

# For de chave valor em todos os itens:
print('Key e Value de todos os itens')
for key, value in dados.items():
  print(key, value)

# For mostra chave apenas dos itens que o valor é maior que 100000:
print('Item valor maior que 100000')
for key, value in dados.items():
  if(value > 100000):
    print(key)

input("Pressione Enter para continuar...")
dadosExercicio = {
    'Crossfox': {'valor': 72000, 'ano': 2005}, 
    'DS5': {'valor': 125000, 'ano': 2015}, 
    'Fusca': {'valor': 150000, 'ano': 1976}, 
    'Jetta': {'valor': 88000, 'ano': 2010}, 
    'Passat': {'valor': 106000, 'ano': 1998}
}
#somente os nomes dos veículos com ano de fabricação maior ou igual a 2000.
print('Veículos com ano de fabricação maior ou igual a 2000.')
for item in dadosExercicio.items():
  if(item[1]['ano'] >= 2000):
    print(item[0])