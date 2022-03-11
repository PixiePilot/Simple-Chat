import socket

HOST = "127.0.0.1"
PORT = 42069

def log(msg):
   print(f'[CLIENT]: {msg}')


def main():
    log('init')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        log('connecting')
        s.connect((HOST, PORT))
        log('sending')
        assert s.sendall(b'Hello, world!!1!\00') is None
        log('done')
        s.close()
        log('shutting down')
