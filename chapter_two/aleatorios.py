import random
random.seed(10)
four_uniform_randoms = [round(random.random(), 4) for i in range(3)]
print(four_uniform_randoms)

naleatorios = [random.randint(1,25) for i in range(10)]

print(naleatorios)

novalista = [1,1,1,1,2,3,8,4,6,7,8,8,8,8]
print(novalista)
naleatorios2 = random.sample(novalista,14)
print(naleatorios2)