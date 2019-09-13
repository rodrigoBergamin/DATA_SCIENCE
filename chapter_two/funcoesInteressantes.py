#função map
#aplica uma função a cada elemento de uma lista
#como a baixo, retorna o dobro de cada elemento

def double(x):
    return x * 2

xs = [1,2,3,4,5,6]

dobro_xs = map(double,xs)
print(list(dobro_xs)) #listando a variável dobro_xs

#filter

def is_even(x):
    return x % 2 == 0

x_evens = filter(is_even,xs) #função filter aplica uma função que filtra cada valor da lista
print(list(x_evens))

#função reduce soma todos os valores de uma lista

#zip

list2 = [1,2,3,4]
list1 = ['a','b','c']

print(zip(list1,list2)) #compactando listas em pares

