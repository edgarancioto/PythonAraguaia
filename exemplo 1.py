import numpy as np

respostas = []
while True:
    variavel = input("Homem ('h'), Mulher ('m'), encerrar ('x')")
    if variavel == 'h' or variavel == 'm':
        respostas.append(variavel)
    else:
        break

num_respostas = len(respostas)
qnt_homens = sum([1 for resposta in respostas if resposta == 'h'])
qnt_mulheres = num_respostas - qnt_homens

gramas = qnt_homens * 350 + qnt_mulheres * 250
kgs = int(np.ceil(gramas / 1000))
print(f"No churras vai ter {qnt_homens} homens, {qnt_mulheres} mulheres, então será necessário comprar {kgs} de carne")





