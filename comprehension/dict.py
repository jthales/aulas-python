# Estrutura de dados: dicionário
# Criação de um dicionário a partir de uma lista de listas

lista_completa = [[("João", "J720"), ("Maria", "M205"), ("José", "J371"), ("Cláudia", "C546"), ("Ana", "A347")], [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]], [9.0, 7.3, 5.8, 6.7, 8.5], ["Aprovado", "Aprovado", "Reprovado", "Aprovado", "Aprovado"]]

coluna = ["Notas", "Media Final", "Situação"]

cadastro  = {coluna[i]: lista_completa[i+1] for i in range(len(coluna))}
print(cadastro)