import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [3, 2, 5, 4, 7]
x2 = [2, 4, 6, 8, 10]
y2 = [1, 4, 7, 5, 8]

titulo = 'Grafico de barras'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x, y, label = 'Grupo 1')
plt.bar(x2, y2, label = 'Grupo 2')
plt.legend()
plt.show()