#TODO: Logging module in case master asks for logs. 
#TODO: Test cases for this class. 
from pexpect import pxssh


class Client(object):
    def __init__(self, **kwargs):
        self.host_name = kwargs['host_name']
        self.user_name = kwargs['user_name']
        self.password = kwargs['password']
        self.session = self.connect()

    def connect(self):
        try: 
            s = pxssh.pxssh()
            s.login(self.host_name, 
                    self.user_name, 
                    self.password)
            return s
        except Exception, e: 
            print e

    def send_command(self, command):
        self.session.sendline(command)
        self.session.prompt()
        return self.session.before
