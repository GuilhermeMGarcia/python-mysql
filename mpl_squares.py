import matplotlib.pyplot as plt


x = [1, 2, 5]
y = [3, 4, 8]

# Titulo
plt.title('Grafico simples')

# Eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo y')


plt.plot(x, y)
plt.show()