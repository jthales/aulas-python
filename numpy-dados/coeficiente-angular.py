# Processo de regressão linear

import numpy as np

dado = np.loadtxt('./apples_ts.csv', delimiter=',', usecols=np.arange(1,88,1))

dado_transposto = dado.T

datas = np.arange(1, 88, 1)

precos = dado_transposto[:,1:6]

moscow = precos[:,0]

# Formula fechada para cácular a coeficiente angular (a) e o coeficiente linear (b)
y = moscow
x = datas
n = np.size(moscow)

a = (n*np.sum(x*y) - np.sum(x)*np.sum(y)) / (n*np.sum(x**2) - np.sum(x)**2) # a = coef angular
b = (np.sum(y) - a*np.sum(x)) / n # b = coef linear
print(f"Coeficiente angular: {a}")
print(f"Coeficiente linear: {b}")
