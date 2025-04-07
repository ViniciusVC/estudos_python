

# PYTHON PARA DATA SCIENCE - NUMPY


# 2. CARACTERÍSTICAS BÁSICAS DA LINGUAGEM
print("2. CARACTERÍSTICAS BÁSICAS DA LINGUAGEM")

# 2.1 Operações matemáticas
### Operadores aritméticos: $+$, $-$, $*$, $/$, $**$, $\%$, $//$

### Adição (+)
print("### Adição (+)")
resultdo = 2 + 2
input("2 + 2 = "+str(resultdo))

### Subtração (-)
print("### Subtração (-)")
resultdo = 5 - 9
input("5 - 9 = "+str(resultdo))

### Multiplicação (*)
print("### Multiplicação (*)") 
resultdo = 2 * 4
input("2 * 4 = "+str(resultdo))

### Divisão (/)
print("### Divisão (/)")
# A operação divisão sempre retorna um número de ponto flutuante.
resultdo = 10 / 3
input("10 / 3 = "+str(resultdo))

### Divisão (//)
print("### Divisão (//)")
# Retorna inteiro.
resultdo = 10 // 3
input("10 // 3 ="+str(resultdo))

### Exponenciação (**)
print("### Exponenciação (**)")
resultdo = 2 ** 3
input("2 ** 3 = "+str(resultdo))

### Resto da divisão (%)
print("### Resto da divisão (%)")
resultdo = 10%2
input("10 % 2 = "+str(resultdo))

resultdo = 10%3
input("10 % 3 = "+str(resultdo))

### Expressões matemáticas
print("### Expressões matemáticas")
resultdo = 5 * 2 + 3 * 2
input("5 * 2 + 3 * 2 ="+str(resultdo))
resultdo = (5 * 2) + (3 * 2)
input("(5 * 2) + (3 * 2) ="+str(resultdo))
resultdo = 5 * (2 + 3) * 2
input("5 * (2 + 3) * 2 = "+str(resultdo))

### A variável _
print("### A variável _")
# No modo interativo, o último resultado impresso é atribuído à variável _


_ = 5*2
resultdo = _ + 3 * 2
print("_ = 5 * 2")
input("_ + 3 * 2 = "+str(resultdo))

10 % 2 + 3 // 10
input("10 % 2 + 3 // 10 = "+str(resultdo))

5 * (2 + 3) / 2
input("5 * (2 + 3) * 2 = "+str(resultdo))

2 ** 3 * 4
input("2 ** 3 * 4 = "+str(resultdo))

# 2.2 Variáveis
print("# 2.2 Variáveis")

ano_atual = 2019
print("ano_atual = 2019")
print(ano_atual)

ano_fabricacao = 2003
print("ano_fabricacao = 2003")
print(ano_fabricacao)

km_total = 44410.0
print("km_total = 44410.0")
print(km_total)

print("### Declaração múltipla")
ano_atual, ano_fabricacao, km_total = 2019, 2003, 44410.0
input("ano_atual="+str(ano_atual)+", ano_fabricacao="+str(ano_fabricacao)+", km_total="+str(km_total))

km_media = km_total / (ano_atual - ano_fabricacao)
km_total += km_media
print("km_total="+str(km_total))

input('valor = valor + 1" é equivalente a "valor += 1')

# 2.3 Tipos de dados
input("# 2.3 Tipos de dados")

# int
ano_atual = 2029
print(type(ano_atual))

# float
km_total = 44410.0
print(type(km_total))

# bool
zero_km = True
print(type(zero_km))

# bool
zero_km = False
print(type(zero_km))

# String de varias linhas.
input("String de varias linhas.")
carro = '''
Nome do carro: Jetta Variant
Ano de fabricação: 2003
'''
print(carro)

quilometragem = None
quilometragem
print(quilometragem)

# 2.4 Conversão de tipos
print("2.4 Conversão de tipos")

a = 10
print(float(a))

var = 3.141592
print(int(var))

## *str.format()*
print('str.format()')
      
print('Olá, {}!'.format('Valente'))

print('Olá, {}! este é seu acesso de número {}!'.format('Valente',32))

print('Olá, {nome}! este é seu acesso de número {acessos}.'.format(nome='Valente',acessos=32))

nome='Valente'
acessos = 32
print(f'Olá, {nome}! este é seu acesso de número {acessos}!')

