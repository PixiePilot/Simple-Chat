import socket

HOST = "127.0.0.1"
PORT = 42069

def log(msg):
   print(f'[SERVER]: {msg}')

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        log('init')
        s.bind((HOST, PORT))
        s.listen()
        log('ready')
        conn, addr = s.accept()
        with conn:
            log(f'Connected to {addr}')
            recvd = []
            b = conn.recv(4096)
            while b not in {b'\00',b''}:
                recvd.append(b)
                print(b)
                b = conn.recv(4096)
            recvd = b''.join(recvd).decode('utf-8')
            log(f'recieved{recvd}')
