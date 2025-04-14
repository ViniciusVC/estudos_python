# PYTHON PARA DATA SCIENCE - PANDAS

# para rodar este arquivo, rode o seguinte comando no terminal ou prompt de comando:
# python pandas_aula_2.py

# 2.1 TRABALHANDO COM TUPLAS

# 2.1 Criando tuplas
# Tuplas são sequências imutáveis que são utilizadas para armazenar coleções de itens, geralmente heterogêneos. Podem ser construídas de várias formas:

# Criando uma tupla vazia
()

# Criando uma tupla de numeros separados por virgula.
1,2,3
print(1,2,3)

# Criando uma tupla
nome = 'Passat'
valor = 153000
nomeValor = (nome, valor)
print(nomeValor)

# Criando uma tupla
nomes_carros=tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])
print(nomes_carros)

print("type(nomes_carros)")
print(type(nomes_carros))

input("Pressione Enter para continuar...")

# 2.2 Seleções em tuplas

print("Tupla nomes_carros:")
print(nomes_carros)
print("Primeiro item:")
print(nomes_carros[0])
print("Segundo item:")
print(nomes_carros[1])
print("Ultimo item:")
print(nomes_carros[-1])
print("Intervalo entre 1 a 2:")
print(nomes_carros[1:3])

input("Pressione Enter para continuar...")

print("for:")
for item in nomes_carros:
    print(item)

input("Pressione Enter para continuar...")
# Desempacotamento de tuplas
print("Desempacotamento de tuplas!")
carro_1, carro_2, carro_3, carro_4 = nomes_carros
print(carro_1)
print(carro_2)
print(carro_3)
print(carro_4)

# ignorando alguns itens.
print("ignorando alguns itens.")
_, A, _, B = nomes_carros
print(A)
print(B)

_, C, *_ = nomes_carros
print(C)

input("Pressione Enter para continuar...")

carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']
valores = [88078.64, 106161.94, 72832.16, 124549.07]
print("list(zip(carros, valores))")
for i in zip(carros, valores):
    print(i)

input("Pressione Enter para continuar...")
for carro, valor in zip(carros, valores):
    print(carro, valor)

input("Pressione Enter para continuar...")
for carro, valor in zip(carros, valores):
  if(valor>100000):
    print(carro)