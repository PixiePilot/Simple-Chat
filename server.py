'''
Cooperatively written by Wolfy & Lyza
'''

import socket
import threading
import asyncio
from typing import Sized

HEADER = 128 # Expected messages sizes by client / server
PORT = 42069
SERVER_ADRESS = socket.gethostbyname(socket.gethostname()) # Global ip in this case due to the host 
EXISTANCE = True # it sudoko without this
FORMAT = 'utf-8'
ADDR = (SERVER_ADRESS, PORT)
DISCONNECT = 'disconnect69' # disconnection package
SHUTDOWN = 'mexicanbomber69' # Shutdown package
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDR)

class User: # The assigned class to a connected user 
    user_id = None
    conn = None
    addr = None
    thread = None
    connected = False
    def __init__(self,conn,addr,user_id) -> None:
        self.user_id = user_id
        self.conn = conn
        self.addr = addr
        self.thread = threading.Thread(target=self.listen(),args =())
        self.thread.start()


    def listen(self):
        self.connected = True
        while True:
            msg_length = self.conn.recv(HEADER).decode(FORMAT)
            if msg_length != '':
                msg_length = int(msg_length)
                data = self.conn.recv(msg_length).decode(FORMAT)
                print(data)
                if data == DISCONNECT:
                    break
                elif data == SHUTDOWN: # poop code
                    existance()
                    break
                else:
                    data = self.function_encode(data)
                    sendall(data)
        self.cleanup()

    def function_encode(self,msg): # making the size 128 ( padding ) 
        size_as_str = str(len(msg))
        padding = ' ' * (HEADER - len(size_as_str))
        header = padding + size_as_str
        msg = header + msg

        return  msg

    def cleanup(self):
        self.conn.close()
        self.connected = False
        # self.thread.join() would deadlock!
    def user_send(self,message):
        self.conn.send(message.encode(FORMAT))
    def __repr__(self):
        return f'{str(self.user_id)}: {self.addr}' # the id in the list 

def sendall(data):# Make teacher go insane :D 
    global user_list
    print(user_list)
    user_list[0].thread.join() # To join the thread to get the error
    for user in user_list:
        print(1)
        user.user_send(data)
    pass
def existance():
    global EXISTANCE
    EXISTANCE = False


def start():
    global user_list
    user_list = []
    server_socket.listen()
    print(f'[SERVER IS LISTENING TO: {ADDR}]')

    while EXISTANCE:
        try:
            conn, addr = server_socket.accept()
            user_list.append(User(conn,addr,len(user_list)))
            print(f'[ACTIVE CONNECTIONS]: {len(user_list)}')

        except socket.error:
            print(f'[SERVER] Connection timed out.')
            pass
        finally: # No 
            if len(user_list) > 0:
                server_socket.settimeout(5)
            else:
                server_socket.settimeout(None)
            for user in user_list:
                if not user.connected:
                    user_list.remove(user)

            
    for user in user_list: # Self cleaning :O
        user.thread.join()
if __name__ == '__main__':
    start()


#multiplayer coding 
