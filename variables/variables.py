# Não há palavras reservadas para definição de variáveis no Python (infelizmente)
# Para declarar uma variável basta seguir a estrutura: <identificador> = <valor>
# O tipo é atribuído de maneira implícita

a = 3
b = 4.4
print(a+b)

texto = 'Sua idade é '
idade = 19
# Má estratégia
# print(texto + str(idade))
print(f'{texto} {idade}')

# O + não serve para concatenação
# O Python também tem algumas peculiaridades como a da linha abaixo
print(3 * 'bom dia\n')

# Como não há palavras reservadas para definição de constantes no Python (infelizmente) utiliza-se, por convenção, uppercase para definição de constantes
PI = 3.14159
r = float(input('Informe o raio da circunferência: '))
area = PI * (r * r)
print(f'A área é igual a {area}')

# Para consultar o tipo de uma variável utiliza-se o type()
type(area)