import numpy as np
import matplotlib.pyplot as plt

dado = np.loadtxt('./apples_ts.csv', delimiter=',', usecols=np.arange(1,88,1))

# Saber quantias dimensões tem o array (2D) = Linhas e colunas (3D) = Linhas, colunas e profundidade
# print(f"O Array tem {dado.ndim} dimensões.")

# Saber quantos dados temos na tabela.
# print(f"O Array tem {dado.size} dados.")

# Saber quantas linhas e colunas tem o array
# print(f"O Array tem {dado.shape[0]} linhas e {dado.shape[1]} colunas.")

# Visualizar dado transposto
dado_transposto = dado.T

datas = np.arange(1, 88, 1)

precos = dado_transposto[:,1:6]

moscow = precos[:,0]
kaliningrad = precos[:,1]
petersburg = precos[:,2]
krasnodar = precos[:,3]
ekaterinburg = precos[:,4]


moscow_ano1 = moscow[0:12] 
moscow_ano2 = moscow[12:24]
moscow_ano3 = moscow[24:36]
moscow_ano4 = moscow[36:48]

# plt.plot(np.arange(1, 13, 1), moscow_ano1)
# plt.plot(np.arange(1, 13, 1), moscow_ano2)
# plt.plot(np.arange(1, 13, 1), moscow_ano3)
# plt.plot(np.arange(1, 13, 1), moscow_ano4)
# plt.title("Preços de maçãs em Moscow")

# plt.xlabel("Meses")
# plt.ylabel("Preço (RUB)")
# plt.legend(["Ano 1", "Ano 2", "Ano 3", "Ano 4"])

# np.array_equal(moscow_ano1, moscow_ano2) # Verifica se os arrays são iguais

# np.allclose(moscow_ano1, moscow_ano2, 0.1) # Verifica se os arrays são iguais com uma tolerância de 0.1
# np.allclose(moscow_ano1, moscow_ano2, 10) # Verifica se os arrays são iguais com uma tolerância de 10

sum(np.isnan(kaliningrad)) # Verifica quantos valores NaN existem no array
# print(f"Kaliningrad tem {sum(np.isnan(kaliningrad))} valores NaN.")

# Ajusta o NaN com a Média dos preços de Kaliningrad
kaliningrad[4] = np.mean([kaliningrad[3], kaliningrad[5]])

# plt.plot(datas, kaliningrad)

# Inserindo uma reta aos dados

# y=ax+b

# x = datas
# y = 0.52*x+80



# plt.plot(datas, moscow)
# plt.plot(x, y)

# Valor de ajuste da reta forma dificil
# soma = np.sqrt(np.sum(np.power(moscow-y, 2)))

# Valor de ajuste da reta forma facil
# print(np.linalg.norm(moscow-y))

# plt.show()

# Formula fechada para cácular a coeficiente angular (a) e o coeficiente linear (b)
Y = moscow
x = datas
n = np.size(moscow)

a = (n*np.sum(x*Y) - np.sum(x)*np.sum(Y)) / (n*np.sum(x**2) - np.sum(x)**2) # a = coef angular
b = np.mean(Y) - a*np.mean(x) # b = coef linear
print(f"Coeficiente angular: {a}")
print(f"Coeficiente linear: {b}")

y = a*x + b # y = ax + b
np.linalg.norm(moscow-y) # Valor de ajuste da reta forma facil
print(f"Valor de ajuste da reta: {np.linalg.norm(moscow-y)}")

plt.plot(datas, moscow)
plt.plot(x, y)
plt.plot(41.5, 41.5*a+b, '*r') # Ponto de interseção da reta com o eixo y
plt.plot(100, 100*a+b, '*r') # Ponto de interseção da reta com o eixo y

plt.show()