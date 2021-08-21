# PEP - Python Enhancement Proposals: Propostas de melhorias do Python
# São definições de estilo de codificação do Python
# Proposta interessante que é implementada em outras linguagens, mas que parece ter maior força entre a comunidade do Python (+1 ponto)

# def soma(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total

def resultado_final(**kwargs):
    status = 'aprovado' if kwargs['nota'] >= 7 else 'reprovado'
    return f'{kwargs["nome"]} foi {status}'
    # print(kwargs['nome'])
    # print(kwargs['nota'])