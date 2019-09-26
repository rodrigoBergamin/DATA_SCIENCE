import matplotlib.pyplot as plt

x = [1,2,9,3]
y = [3,5,7,8]

#inserindo título no gráfico
plt.title('Meu primeiro gráfico com Python')

#Eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
#
#plotando o gráfico
plt.plot(x, y, color = 'green', marker = 'o', linestyle = 'solid')
#exibindo o gráfico
plt.show()

