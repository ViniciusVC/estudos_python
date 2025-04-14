# PYTHON PARA DATA SCIENCE - PANDAS

# para rodar este arquivo, rode o seguinte comando no terminal ou prompt de comando:
# python pandas_aula_4.py

# 4. FUNÇÕES E PACOTES
# Funções são unidades de código reutilizáveis que realizam uma tarefa específica, podem receber alguma entrada e também podem retornar alguma resultado.

# 4.1 Built-in function
# A linguagem Python possui várias funções integradas que estão sempre acessíveis. Algumas já utilizamos em nosso treinamento: type(), print(), zip(), len(), set() etc.

dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
print(dados)

input("Pressione Enter para continuar...")

# Somando os valores do dicionário:
valores = []
for valor in dados.values():
  valores.append(valor)
print(valores)

# Soma dos valores de um dicionário.
soma = 0
for valor in dados.values():
  soma += valor
print(soma)

# Listar todos os valores de um dicionário.
print(list(dados.values()))

# Soma dos valores de um dicionário.
print(sum(dados.values()))

input("Pressione Enter para continuar...")

print('help(sum)')

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