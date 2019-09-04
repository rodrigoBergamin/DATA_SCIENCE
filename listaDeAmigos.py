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
  users[u]["friends"].append(users[f]["nome"])
  users[f]["friends"].append(users[u]["nome"])

print(users[0])