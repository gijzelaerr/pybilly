
import os

class UnixUser:
    def __init__(self, username, uid, gid, home, shell, fullname, forward):
        self.username = username
        self.uid = uid
        self.gid = gid
        self.home = home
        self.shell = shell
        self.fullname = fullname
        self.forward = forward

def email(home):
    forward = os.path.join(home, ".forward")
    if os.access(forward, os.R_OK):
            return open(forward).readline().strip()
    return False

def details(username):
    passwd = open('/etc/passwd')
    for line in passwd.readlines():
        file_username, password, uid, gid, details, home, shell = line.split(':')
        fullname = details.split(',')[0]
        forward = email(home)
        if file_username == username:
            return UnixUser(username, uid, gid, home, shell, fullname, forward)
    raise Exception("user doesn't exists")


if __name__ == '__main__':
    print details('manager').fullname
    print details('fake').fullname
