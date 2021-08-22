# É possível armazenar uma função dentro de uma variável
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

# somar = soma
# print(somar(3,4))

def operacao_aritmetica(fn, op1, op2):
    return fn(op1, op2)

# resultado = operacao_aritmetica(soma, 1, 1)
# print(resultado)

# resultado = operacao_aritmetica(subtracao, 2, 1)
# print(resultado)

def soma_parcial(a):
    def concluir_soma(b):
        return a + b
    return concluir_soma

# Essa "enrolação" serve para tardar uma função, em casos de alto volume de processamento, justamente para tornar o processo vais veloz
# fn = soma_parcial(10)
resultado  = soma_parcial(10)(12)
print(resultado)
