from __future__ import division
users = [
  {"id":566, "nome":"Rodrigo"},
  {"id":21, "nome":"Cristina"},
  {"id":3258, "nome":"Alessandra"},
  {"id":2, "nome":"Diana"},
  {"id":69, "nome":"Clarice"},
  {"id":33, "nome":"Alberto"},
  {"id":3369, "nome":"Diogo"},
  {"id":125, "nome":"Leonardo"},
  {"id":852, "nome":"Linus"},
  {"id":987, "nome":"Thomas"},
  
]

friendship = [ (0,1),(1,2),(0,3),(1,3),(2,5),(2,3),(2,4),(3,6),(8,9),(5,7),(6,8),(7,9), (0,9), (0,8)]

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

print(new_list)

'''add = lambda x, y, z: x + y + z   // recebe argumentos e manipula esses argumentos

print(add(3, 5, 8)) exemplo de lambda, função anonima
'''