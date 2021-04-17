import socket
import pickle
import numpy as np

HOST = '127.0.0.1'       # Endereco IP do Servidor          
PORT = 3003     # Porta que o Servidor esta


tcp = socket.socket()
orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

print('Bindado no endereço: ', orig, '\n')
print('Esperando conexão do cliente...')

while True :
    con, cliente = tcp.accept()
    print ('Conectado por', cliente)
    while True:
        msg = con.recv(4096)
        array, elementToFind = pickle.loads(msg)
        
        if not msg: break
        
        print (cliente)
        print (array, 'Elemento: ', elementToFind)

        # con.send(bytes('Welcome to the Server 1', 'utf-8'))

        if(elementToFind in array):
            index = np.where( array == elementToFind)
            print(index[0][0])
            data = pickle.dumps(index[0][0])

            con.send(data)
        else:
            print('Element not in the array')
            data = pickle.dumps('Null')
            con.send(data)
        break
    # print ('Finalizando conexao do cliente...', cliente)
   