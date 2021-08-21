# for i in range(10):
#     print(i)

# for i in range(1, 11):
#     print(i)

# for i in range(1, 100, 7):
#     print(i)

# nums = [2, 4, 6, 8]
# for n in nums:
#     print(n, end="\n")

# texto = 'Python é massa'
# for letra in texto :
#     print(letra, end='\n')

produto = {
    'nome': 'Caneta',
    'preço': 8.8,
    'desconto': 0.5
}

# for key in produto:
    # print(f'{key}: {produto[key]}.', end="\n")

for (key, value) in produto.items():
    print(key,':', value, end="\n")
