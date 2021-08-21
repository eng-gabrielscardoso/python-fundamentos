# O Python utiliza estrutura de bloco por meio de identação
# Logo, a tabulação deve seguir uma lógica estrita
# Nota pessoal: nesse caso, ponto para o Python, pois obriga o engenheiro a ser organizado, ter boas práticas e estar atento ao código pois isso pode impactar diretamente na condição do software

nota = float(input('Informe a nota do aluno: '))
if nota >= 9:
    print('Quadro de honra')
elif nota >= 7 and nota < 9:
    print('Quadro de menções')
elif nota >= 5 and nota < 7:
    print('Indiferente')
else:
    print('Reprovados')