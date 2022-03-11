'''all of the code related to handlight client functions like sending, receiving and (eventually) UI'''

import socket as sock    # sockets
import time              # timeout handling

ADDR = '207.180.217.143'  # target ip
#ADDR = '127.0.0.1'       # 
PORT = 42069              # target port
ADDR_TUPLE = (ADDR, PORT) # target destination
ENCODING = 'utf-8'        # agreed upon encoding

# the header of any message is the size of the message in bytes + padding
HEADER_SIZE = 128

DISCONNECT = 'disconnect69'
SHUTDOWN   = 'mexicanbomber69'

def log(msg) -> None:
   print(f'[CLIENT]: {msg}')

def make_header(size: int) -> str:
    '''creates header with specified size information'''
    size_as_str = str(size)
    padding = ' ' * (HEADER_SIZE - len(size_as_str))
    return  padding + size_as_str

def make_message(msg: str) -> bytes:
    '''makes message packet from string'''
    return bytes(make_header(len(msg)) + msg, ENCODING)

def get_message(sock) -> str:
    '''parses packet sent by the server and decodes it'''
    # timeouts raise exceptions, so no need to handle here
    header = sock.recv(HEADER_SIZE)
    msg_len = int(header)
    return sock.recv(msg_len).decode(ENCODING)

def main(listen_only=True):
    '''top-level client function'''
    with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as s:
        log('connecting')
        s.connect(ADDR_TUPLE)
        if not listen_only:
            log('sending')
            s.sendall(make_message('Hello, all!'))
            s.sendall(make_message('go ---- ----!'))
            s.sendall(make_message('words, words..'))
            s.sendall(make_message('more words!'))
            s.sendall(make_message('<3'))
        t_end = time.time() + 4
        log('receiving')
        while time.time() < t_end:
            recvd = get_message(s)
            if recvd != '':
                log(f'recieved {recvd}')
        #__import__('time').sleep(10)
        #s.sendall(make_message(SHUTDOWN))
        #s.sendall(make_message(DISCONNECT))
        log('closing')
        s.close()
        log('closed')