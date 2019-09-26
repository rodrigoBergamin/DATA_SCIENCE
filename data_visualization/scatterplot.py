import matplotlib.pyplot as plt

x = [1,2,9,3]
y = [3,5,7,8]


titulo = 'Scatterplot'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

#Título
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#plotando
plt.scatter(x,y, label='Meus pontos', color='red')
plt.plot(x,y)
plt.legend()
plt.show()
