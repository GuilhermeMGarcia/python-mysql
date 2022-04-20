import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 2, 5, 4, 7]

titulo = 'Grafico de barras'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x, y)
plt.show()