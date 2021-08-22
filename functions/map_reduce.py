from functools import reduce

def soma(a, b):
    return a + b

def soma_nota(delta):
    def mais_um_e_meio(nota):
        return nota + delta
    return mais_um_e_meio 

notas = [6.5, 7.2, 5.8, 8.4]

# Primeira estratégia, mais procedimental e imperativa
# for i, n in enumerate(notas):
#     # print(i, n)
#     notas[i] = n + 1.5

# for i in range(len(notas)):
#     notas[i] = notas[i] + 1.5

# Segunda estratégia, mais funcional
# notas_finais = map(mais_um_e_meio, notas)
# print(notas_finais)

# Terceira estratégia, com funções parciais
# notas_finais = map(soma_nota(1.5), notas)
# print(notas_finais)

total = reduce(soma, notas, 0)
print(total)