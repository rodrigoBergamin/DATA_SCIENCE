from collections import defaultdict, Counter

grades = { 'Joel': 80, 'Tim': 958}

try: #tratando uma exceção
    kates_grade = grades['Kate']
except KeyError:
    print('No grade for Kate')

joel_grade = grades.get('Joel', 0) #método get resgata um valor do dicionário que foi passado como parâmetro
print(joel_grade)

print(grades.items())

#usando defautl dict para encontrar palavras em um documento

word_counts = defaultdict(int)

document = [] #simulando um documento

for word in document:
    word_counts[word] += 1

#método defaultdict cria um dicionario vazio, onde é passado como parâmetro a estrutura dos valores correspondentes as chaves
dd_list = defaultdict(list) #produz listas vazias para chaves de um dicionario
dd_list[1].append(0)

print(dd_list)

dd_dict = defaultdict(dict) #
dd_dict['Rowens']['Date_of_Birth'] = 1999 #gerando um dicionario como estrutura de valor para chave correspondente
dd_dict['Rowens']['Age'] = 21
dd_dict['Cleveland']['Name'] = 'Cavaliers'
dd_dict['Cleveland']['Since'] = 1962
print(dd_dict)


#counter

c = [0,3,5,0.1,0.1,0.1,0.11,0.2,7.6,4,3,3,3,3,3,5]
x = Counter(c)
print(x)

for item, count in x.most_common(3):
    print(item ,' aparece ', count, ' vezes')


#CONJUNTOS
#set

s = set([7,4,5]) #criando um conjunto
#elementos são adicionados em ordem crescente
s.add(1)
s.add(2)
s.add(3)

print(s)

for i in range(50,100): #adicionando elementos a um conjunto set
    s.add(i)
#print(s)

print(all([True,1,{3}])) #função all percorre uma lista e retorna True caso todos os elementos sejam verdadeiros
print(any([True, False, True])) #função any retorna True caso um elemento seja verdadeiro