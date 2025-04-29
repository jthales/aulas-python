notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],'Cláudia': [5.5, 6.6, 8.0], 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}

# Try é o bloco que tenta executar o código, se ocorrer um erro, ele pula para o except.
try:
    nome = input("Digite o nome do(a) estudante: ")
    resultado = notas[nome]

# Except é o tratamento de erro, ou seja, se ocorrer um erro, ele executa o bloco except.
except KeyError:
    print(f"O estudante '{nome}' não foi encontrado.")

# Else é quando não ocorre erro, ou seja, o bloco try executa com sucesso.
else:
    print(f"As notas de {nome} são: {resultado}")
    
# Finally é igual o .add do Angular, ele sempre executa, mesmo que ocorra erro ou não.
finally:
    print("Fim do programa.")