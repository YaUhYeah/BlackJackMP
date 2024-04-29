import socket
from _thread import start_new_thread
from player import Player
import pickle

server = "127.0.0.1"
port = 11166
players = [Player(0,0,50,50,(255,255,0), 1),Player(100,100,50,50,(255,0,0), 1)]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection Server started fr")


def threaded_client(connection, plr):

    connection.send(pickle.dumps(players[plr]))
    while True:
        try:
            data = pickle.loads(connection.recv(2048))
            players[plr] = data

            if not data:
                print("Disconnected")
                break
            else:
                if plr == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("Received ", data)
                print("Sending ", reply)
            connection.sendall(pickle.dumps(reply))
        except:
            break
    print("Connection closed")
    connection.close()


num_player = 0

while True:
    conn, addr = s.accept()
    print("Client connected on ", addr)
    start_new_thread(threaded_client, (conn, num_player))
    num_player += 1
