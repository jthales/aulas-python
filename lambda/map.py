notas = [6.0, 7.0, 8.0, 9.0, 10.0]
qualitativo = 0.5

notas_qualitativas = list(map(lambda x: x + qualitativo, notas))
print(notas_qualitativas)