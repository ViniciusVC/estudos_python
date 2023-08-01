# Aula de Python 01

# Obs.: Instale jupyter notbook na sua máquina local.

nome = "Gabriel" # Declarar variavel e atribuir uma string.
print(nome) # Mostre o conteudo da variavel nome.

nome = "Filipe" # Atribuir outra string a variavel nome.
print("Mostre o conteudo da variavel nome:")
print(nome)

idade = 37
print("Mostre o conteudo da variavel idade :")
print(idade)

print("Mostrara o calculo idade+3 :")
print(idade+3)

# Vamos criar uma função em Python (identação obrigatoria)
def mais_um_ano(idade):
  print("Rodou a funcao")
  return idade +1
  
# Chamar a função que foi criada
mais_um_ano(40)

filme1 = "Toy Story 17"
filme2 = "A Xuxa xontra o Baixo Astral"
filme3 = "Matrix 1"
# Instanciar uma lista
filmes = ["Toy Story", filme2, filme3]
print(filmes)

# Outra função em Python.
def imprime_filmes(filmes_que_quero_imprimir):
  print("Os filmes que quero imprimir são :")
  print(filmes_que_quero_imprimir[-1]) # Ultimo idem da lista.
  print(filmes_que_quero_imprimir[0]) # Primeiro item da lista

# Chamar função imprime_filmes  
imprime_filmes(filmes)

# Criando um FOR.
for filme in filmes:
  print(filme)
  print("...")
print("saiu do for")

# Outra função
def imprime_filmes_vertical(filmes_que_quero_imprimir):
  for filme in filmes_que_quero_imprimir:
    print(filme)

# Chamar função
imprime_filmes_vertical(filmes)

# criar um dicionario (JSON/Objeto)
dados = {"nome":"Vinicius",
         "idade":40,
         "empresa":"Oi"}
print("Mostrar todo o dicionário")
print(dados)
print("Apenas coluna nome")
print(dados["nome"])



