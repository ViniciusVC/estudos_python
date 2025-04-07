

# PYTHON PARA DATA SCIENCE - NUMPY

# 3. TRABALHANDO COM LISTAS
print("3. TRABALHANDO COM LISTAS")

#Listas são sequências **mutáveis** que são utilizadas para armazenar coleções de itens, geralmente homogêneos. Podem ser construídas de várias formas:
#```
#- Utilizando um par de colchetes: [ ], [ 1 ]
#- Utilizando um par de colchetes com itens separados por vírgulas: [ 1, 2, 3 ]
#```


Acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
print(Acessorios)
input("Pressione Enter para continuar...")

### Lista com tipos de dados variados
Carro_1 = ['Jetta Variant', 'Motor 4.0 Turbo', 2003, 44410.0, False, ['Rodas de liga', 'Travas elétricas', 'Piloto automático'], 88078.64]
Carro_2 = ['Passat', 'Motor Diesel', 1991, 5712.0, False, ['Central multimídia', 'Teto panorâmico', 'Freios ABS'], 106161.94]
print(Carro_1)
input("Pressione Enter para continuar...")
print(Carro_2)
input("Pressione Enter para continuar...")

Carros = [Carro_1, Carro_2]
print(Carros)
input("Pressione Enter para continuar...")

print("# 3.2 Operações com listas")

