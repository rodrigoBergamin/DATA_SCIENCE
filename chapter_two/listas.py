x = [-4,1,-2,3]
y = sorted(x, key = abs, reverse=True) #organiza a lista com base no valor absoluto do maior para o menor
#onde abs retorna o valor absoluto do número passado e reverse=True faz com q retorne do maior para o menor
print(y)

#diferença entre o método sort e sorted: sort aplicará a alteração no elemento original, sorted aplicará alteração apenas na nova variável


#LIST COMPREENSHIONS

even_numbers = [z for z in range(5) if z % 2 == 0]
print(even_numbers)

squares = [i*i for i in range(5)] #retornando uma lista com quadrados dos números
#lê-se do fim para o início, retorn i*i para i no alcance de 0 a 4
print(squares)

square_dict = {n:n * n for n in range(5)} #gerando um dicionário com lists compreenshions

square_set = {n * n for n in [1,-1]}
print(square_set) #criando um conjunto set com list compreenshions, OBS: conjuntos sets não repetem valores

zeroes = [0 for _ in even_numbers]

print(zeroes)

pairs = [(x,y)
    for x in range(10)
    for y in range(10)] #gerando um array com tuplas, de 0 a 9, onde para cada elemento de x, percorra de 0 a 9 elementos em y

print(pairs)

increasing_pairs = [(x,y)
    for x in range(2)
    for y in range(x + 1, 10)]

print(increasing_pairs)

