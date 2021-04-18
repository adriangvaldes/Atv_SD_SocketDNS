from click._compat import raw_input
import socket
import numpy as np
import pickle
from dns import dnsTranslate

HOST= '127.0.0.1'
PORT1 = 3000
PORT2 = 3001

print("------------------------------------------------")
print("ATIVIDADE SD - Adrian e Sayonara - Ilheus - BA")
print("------------------------------------------------")

def connectAndSend(serverName, msg):
    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = dnsTranslate(serverName)
    
    ClientSocket.connect(dest)
    arraySerialized = pickle.dumps(msg)

    print(f"Enviando o vetor {msg[0]} para o servidor {serverName}...")
    print(f"Procurando elemento {msg[1]}...\n")

    ClientSocket.send(arraySerialized)
    response = ClientSocket.recv(1024)

    index = pickle.loads(response)

    if(index == "Null"):
        return None
    else:
        return index

    print("\nEncerrando conexão com o servidor ...\n")

    ClientSocket.close()

array = [1,2,0,9,3,7,8,5]
splitArray = np.array_split(array, 2)
element = 10

msg = [splitArray[0], element]
msg2 = [splitArray[1], element]

index = connectAndSend(1, msg)
if (index):
    print(f"O elemento {msg[1]} se encontra na posição {index}")
else:
    index = connectAndSend(2, msg2)
    if(index):
        print(f"O elemento {msg[1]} se encontra na posição {index + 4}")
    else:
        print(f"!!!  O elemento {msg[1]} não está no array  !!!")
print("------------------------------------------------")


print("------------------------------------------------")
print("Encerrando cliente, Até mais!")
print("------------------------------------------------")


