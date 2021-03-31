import json

def loadClients():
    dataClients = [{
        "name": "Felisbelo Silva",
        "id": 1,
        "email": "felisbelo@email.com"
        },
        {
        "name": "Maria Joaquina",
        "id": 2,
        "email": "mjoaquina@email.com"
        },
        {
        "name": "Robert Joseph",
        "id": 3,
        "email": "robertj@email.com"
        },
        {
        "name": "Tobias Malaquias",
        "id": 4,
        "email": "tobmalaq@email.com"
        },
    ]   
    return dataClients

clients = loadClients()

for client in clients:
  if client['id'] == 2:
   clientByid = client
   print (clientByid)

