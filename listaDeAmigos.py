from __future__ import division
from collections import Counter

users = [
  {"id":0, "nome":"Rodrigo"},
  {"id":1, "nome":"Cristina"},
  {"id":2, "nome":"Alessandra"},
  {"id":3, "nome":"Diana"},
  {"id":4, "nome":"Clarice"},
  {"id":5, "nome":"Alberto"},
  {"id":6, "nome":"Diogo"},
  {"id":7, "nome":"Leonardo"},
  {"id":8, "nome":"Linus"},
  {"id":9, "nome":"Thomas"},
  
]

friendship = [(0,1),(1,2),(0,3),(1,3),(2,5),(2,3),(2,4),(3,6),(8,9),(5,7),(6,8),(7,9),(0,9),(0,8)]

for user in users:
  user["friends"] = []

for u,f in friendship:
  users[u]["friends"].append(users[f])
  users[f]["friends"].append(users[u])


def number_of_friends(user): #quantos amigos o usuário tem?
  return len(user["friends"]) #retornando o tamanho da lista de amigos do usuário

total_connections = sum(number_of_friends(user) for user in users) #retornará o total de conexões de cada usuário em users
num_users = len(users) #tamanho da lista de usuários
avg_connections = total_connections/num_users #total de conexões de todos os usuários divido pelo número de usuários


num_friends_by_id = [ (user['id'],  number_of_friends(user))
  for user in users]

new_list = sorted(num_friends_by_id, #método sorted, que retornará um novo array ordenado pelo
       key= lambda u: u[1], #número de amigos de cada usuário
       reverse=True) #em ordem decrescente

#print(new_list)

'''add = lambda x, y, z: x + y + z   // recebe argumentos e manipula esses argumentos

print(add(3, 5, 8)) exemplo de lambda, função anonima
'''

#criando uma função de Pessoas que eu talvez conheça

def friends_of_friends(user):
  return[foaf['id']
    for friend in user["friends"]
    for foaf in friend["friends"]]

print (friends_of_friends(users[0]))

def not_the_same(user, other_user):
  return user['id'] != other_user['id'] #não são os mesmos se possuirem ids diferentes

def not_friends(user, other_user):
  return all(
    not_the_same(friend, other_user) 
    for friend in user['friends']
  )

def friend_of_friend_ids(user):
  return Counter(foaf['id'] for friend in user['friends'] #para cada um dos meus amigos
for foaf in friend['friends'] #que contam *their* amigos
   if not_the_same(user,foaf) and not_friends(user, foaf)) #e que não são meus amigos

print(friend_of_friend_ids(users[0]))