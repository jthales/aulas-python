lista = [
    { "cargo": "Segurança", "quantidade": 5, "salario": 3000 },
    { "cargo": "Docente", "quantidade": 16, "salario": 6000 },
    { "cargo": "Diretoria", "quantidade": 1, "salario": 12500 },
]
# Saber o total de funcionários e a diferença entre o maior e o menor salário e a média salarial

# Calcular total de funcionários
total_funcionarios = 0

for funcionario in lista:
    total_funcionarios += funcionario["quantidade"]
    
print(f"Total de funcionários: {total_funcionarios}")

# Calcular o maior e o menor salário
maior_salario = 0
menor_salario = lista[0]["salario"]

for funcionario in lista:
    if funcionario["salario"] > maior_salario:
        maior_salario = funcionario["salario"]
    elif funcionario["salario"] < menor_salario:
        menor_salario = funcionario["salario"]
        
diferenca_salario = maior_salario - menor_salario
print(f"Diferença entre o maior e o menor salário: {diferenca_salario}")

# Calcular a média salarial
soma_salarios = 0
for funcionario in lista:
    soma_salarios += funcionario["salario"] * funcionario["quantidade"]
    
media_salarial = soma_salarios / total_funcionarios
print(f"Média salarial: {media_salarial}")

