# Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:
lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

for lista in lista_de_listas:
    soma = sum(lista)
    print(f"A soma da lista {lista} é {soma}.")
    
    
# Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

lista_terceiros = [tupla[2] for tupla in lista_de_tuplas]
print(lista_terceiros)

# Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas:
aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

aluguel_apartamento = [valor for tipo, valor in aluguel if tipo == 'Apartamento']
print(aluguel_apartamento)