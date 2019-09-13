conj = set()
info = []
caes = {
    'Micael': {
        'idade':2,
        'raca':'Pastor Alemão'        
    },
    'Tauros': {
        'idade':3,
        'raca':'Pitbull'
    },
    'Dino': {
        'idade': 7,
        'raca': 'Pastor Suiço'
    }
}

def addOnSet (dicionario, conjunto):
    for nome, dado in caes.items():
        conj.add(nome)
        print(nome,dado)

addOnSet(caes,conj)
print(conj)
print(info)

print(caes.items())