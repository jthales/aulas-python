lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 2, 66]

tamanho = len(lista)
maior = max(lista)
menor = min(lista)
soma = sum(lista)

print(f"A lista possui {tamanho} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valores presentes nela é igual a {soma}.")

tabuada = lambda x: [x * i for i in range(1, 11)]
print(f"A tabuada de 5 é: {tabuada(5)}")


lista_multiplos = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
mult_3 = list(filter(lambda x: x % 3 == 0, lista_multiplos))
print(f"Os números múltiplos de 3 são: {mult_3}")