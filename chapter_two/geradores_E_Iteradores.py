def lazy_range(n):
    #uma versão preguiçosa de range
    i = 0
    while i < n:
        i += 1
        yield i


#yield x return, yield mantém o estado da função, isto é, guarda a memória, return reinicia a função toda vez q ela é chamada

for i in lazy_range(5):
    print(i)

'''
def createGenerator():
    for i in range(0,3):
        yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!

for i in mygenerator:
    print(i)

'''

lazy_evens_below = (i for i in lazy_range(20) if i%2 == 0) #criando geradores
print(lazy_evens_below)