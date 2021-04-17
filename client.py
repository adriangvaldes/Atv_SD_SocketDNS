from click._compat import raw_input
import socket
import numpy as np
import pickle

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT1 = 3000     # Porta que o Servidor esta
PORT2 = 3003     # Porta que o Servidor esta
       
def connectAndSend (host, port, msg):
  ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
  dest = (host, port)
  ClientSocket.connect(dest)
  arraySerialized = pickle.dumps(msg)

  print ('Enviando', msg, '...')

  ClientSocket.send (arraySerialized)
  response = ClientSocket.recv(1024)
  data = pickle.loads(response)

  if (data == 'Null'):
    print('Elemento não está no server!!')
  else:
    print ('Elemento está na posição:', data)
  

  
  print ('Encerrando sessão...')

  ClientSocket.close()


array = [1, 2, 0, 9, 3, 7, 8, 5]

splitArray = np.array_split(array, 2)

print ('Para sair use CTRL+X\n')

msg = [splitArray[0], 9]
msg2 = [splitArray[1], 9]

# Sending to Server 1
connectAndSend(HOST, PORT1, msg) 
connectAndSend(HOST, PORT2, msg2) 

# Sending to Server 2
# connectAndSend(HOST, PORT2, splitArray[1])


