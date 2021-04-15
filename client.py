from click._compat import raw_input
import socket
import numpy as np
import pickle

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT1 = 3000     # Porta que o Servidor esta
PORT2 = 3001     # Porta que o Servidor esta
       
def connectAndSend (host, port, array):
  tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  dest = (host, port)
  tcp.connect(dest)
  arraySerialized = pickle.dumps(array)
  print ('Enviando', array, '...')
  tcp.send (arraySerialized)
  tcp.close()
  print ('Encerrando sessão...')


array = [1, 2, 0, 9, 3, 7, 8, 5]

splitArray = np.array_split(array, 2)

print ('Para sair use CTRL+X\n')

# Sending to Server 1
connectAndSend(HOST, PORT1, splitArray[0]) 

# Sending to Server 2
connectAndSend(HOST, PORT2, splitArray[1])


# tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# while True:
#   tcp.listen(2)
#   con, cliente = tcp.accept()
#   print ('Concetado por', cliente)
#   while True:
#       msg = con.recv(4096)
#       arrayRecieved = pickle.loads(msg)
#       if not msg: break
#       print (cliente)
#       print (arrayRecieved)
#       break
#   print ('Finalizando conexao do cliente'), cliente
#   con.close()
#   break

