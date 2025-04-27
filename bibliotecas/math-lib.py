# importando 2 métodos da mesma biblioteca
from math import pi, pow

raio = float(input("Digite o raio da área circular em metros: "))

area = pi*pow(raio,2)
valor = area * 25.00

print(f"Você precisará pagar R$ {round(valor,2)} por uma área de {round(area,2)} metros de grama")