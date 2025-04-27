import matplotlib.pyplot as plt

estudantes = ['Ana', 'Bruno', 'Carlos', 'Diana']
notas = [8.5, 9.0, 7.5, 8.0]

plt.bar(estudantes, notas, color='blue')
plt.xlabel('Estudantes')
plt.ylabel('Notas')
plt.title('Notas dos Estudantes')

plt.show()