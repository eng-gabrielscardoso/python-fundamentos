x = 0

# Não use!
# while x:
#     print(x)

# while x != -1:
#     x = float(input('Informe o número ou -1 para sair: '))

total = 0
nota = 0
quantidade = 0

while nota != -1:
    nota = float(input('Informe a nota ou -1 para sair: '))
    if nota != -1:
        quantidade += 1
        total += nota

media = total / quantidade

print(f'A média é: {media}')