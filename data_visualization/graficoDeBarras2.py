import matplotlib.pyplot as plt

x = [1,2,9,3]
y = [3,5,7,8]

x2 = [-1,-2,4,9]
y2 = [3,5,9,19]

titulo = 'Gráfico de barra 2'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

#Título
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x, y, label = 'Grupo 1')
plt.bar(x2, y2, label = 'Grupo 2')
plt.legend()
plt.show()