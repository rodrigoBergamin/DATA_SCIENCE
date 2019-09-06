def double(x):
    #função que retorna o dobro de um valor
    return x * 2

def apply_to_one(f):
    #passando a função f como parâmetro para apply_to_one, que carrega dentro de si o parametro 1
    return f(1)

my_double = double #instanciando a função double na variável my_double
x = apply_to_one(my_double) #passando a função my_double como parâmetro para apply_to_one que retorna my_double com parâmetro 1
print(x)