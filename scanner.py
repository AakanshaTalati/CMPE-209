# A sample file to demonstrate scanning. This entire class can be replaced with 
# a couple of lines of code using the python-nmap module. 
import socket
from threading import *

class Scanner(object):
    
    def __init__(self, host_name, list_of_ports):
        if host_name:
            self.target = host_name

        if list_of_ports:
            self.target_ports = list_of_ports

        self.print_lock = Semaphore(value = 1)

    
    def port_scan(self):
        try: 
            target_ip = socket.gethostbyname(self.target_host)
        except:
            print "Cannot resolve hostname {}".format(self.target_host)
            return 
        
        try:
            target_name = socket.gethostbyaddr(target_ip)
            print "\n Scan results for: {}".format(target_name[0])
        except:
            print "\n Scan results for: {}".format(target_ip)

        socket.setdefaulttimeout(1)

        for port in self.target_ports:
            print "\n Scanning port: {}".format(port)
            t = Thread(target = self.connect_scan, args = (port))
            t.start()

    def connect_scan(self, target_port):
        try: 
            conn_socket = socket(AF_INET, SOCK_STREAM)
            conn_socket.connect((self.target_host, port))
            
            conn_socket.send("Test String\r\n")
            results = conn_socket.recv(100)

            self.print_lock.acquire()
            print "\n Open port: {}".format(port)
            print "\n Results: {}".format(str(results))
        except:
            self.print_lock.acquire()
            print "\n Closed port: {}".format(port)
        finally:
            self.print_lock.release()
            conn_socket.close()

