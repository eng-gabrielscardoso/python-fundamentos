# Em todos os módulos do Python é criado um namespace, onde ficam armazenados todos os métodos do escopo do módulo que podem ser referenciados externamente ao módulo. Logo, para acessar saudacao(), na chamada do método deve estar associado o módulo. Nesse caso: basic.saudacao()

# No Python, por convenção utiliza-se o padrão snake case para nomes de funções
# No Python, argumentos são opcionais
# No Python não há sobrecarga de funções


def saudacao(nome="Pessoa"):
    print('Olá', nome)

# def saudacao():
    # print('Bom dia!')


def soma(a=0, b=0):
    return a + b
