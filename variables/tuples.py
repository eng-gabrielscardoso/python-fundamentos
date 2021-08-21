# Tuplas são estruturas de dados que não aceitam modificação
# Aceitam repetições
# Seriam Arrays "congelados" do JS
nomes = ('Ana', 'Bia', 'Gui', 'Ana')
print(type(nomes))
print(nomes)

# Permite visualizar se um determinado elemento está em uma estrutura de dados
# Também funciona com listas
print('bia' in nomes) 

# Também é possível acessar elementos por meio de seus índices
print(nomes[0])

# Obs: para definir uma tupla deve-se ter, no mínimo, um elemento e, caso haja apenas um único elemento, esse deve estar seguido por uma vírgula, mesmo que não haja outro elemento
x = ('Gabriel')
y = ('Gabriel',)
print(type(x))
print(type(y))
# Isso ocorre pois o uso de parênteses pode estar associado a um contexto de expressão

# Formas de pegar ranges em tuplas, aplicável a listas
print(nomes[1:3])
