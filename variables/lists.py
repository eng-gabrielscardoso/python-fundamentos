# São estruturas de dados que permitem modificação e elementos repetidos
# São bastante dinâmicas e lembram os Arrays
nums = [1, 2, 3]
print(type(nums))
# Método para empurrar um novo elemento no último índice
nums.append(4)
# Método para visualizar o número de elementos de uma lista
print(len(nums))
nums[3] = 100
print(nums[3])
# Método para dar um replace em um determinado índice da lista
nums.insert(0, -1)
print(nums)
print(nums[-1])