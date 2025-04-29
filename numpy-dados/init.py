import numpy as np

dado = np.loadtxt('./apples_ts.csv', delimiter=',', usecols=np.arange(1,88,1))

# Saber quantias dimensões tem o array (2D) = Linhas e colunas (3D) = Linhas, colunas e profundidade
print(f"O Array tem {dado.ndim} dimensões.")

# Saber quantos dados temos na tabela.
print(f"O Array tem {dado.size} dados.")

# Saber quantas linhas e colunas tem o array
print(f"O Array tem {dado.shape[0]} linhas e {dado.shape[1]} colunas.")

# Visualizar dado transposto
dado_transposto = dado.T
print(f"O Array transposto tem {dado_transposto.shape[0]} linhas e {dado_transposto.shape[1]} colunas.")