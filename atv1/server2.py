import socket
import pickle
import numpy as np

HOST = '127.0.0.1'
PORT = 3001

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

print("Waiting new conection ...\n")

while True:
    con, cliente = tcp.accept()
    print('Conectado por', cliente)
    while True:
        msg = con.recv(4096)
        array, elementToFind = pickle.loads(msg)

        if not msg: break
        print("Array recebido: ", array, "\nElemento a buscar: ", elementToFind)

        if(elementToFind in array):
            index = np.where(array == elementToFind)
            print(f"Elemento encontrado na posição: {index[0][0]} do array")
            data = pickle.dumps(index[0][0])

            con.send(data)
        else:
            print('Elemento não encontrado no array')
            data = pickle.dumps('Null')
            con.send(data)
            print("Finalizando conexao do cliente...", cliente)
            con.close()

        print("Finalizando conexao do cliente...", cliente)
        print("\n\n\n----------------------------------------------\nWaiting new conection...\n")
        con.close()
        break
    