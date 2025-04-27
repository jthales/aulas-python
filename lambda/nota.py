# nota = float(input("Digite a nota do aluno: "))

# def qualitativo(x):
#     return x + 0.5

# qualitativo(nota)


# nota_lambda = float(input("Digite a nota do aluno: "))
# qualitativo_lambda = lambda x: x + 0.5

# qualitativo_lambda(nota_lambda)


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = lambda x, y, z: (x + y + z) / 3
media_estudante = media(n1, n2, n3)
print(f"A média ponderável do aluno é: {media_estudante}")