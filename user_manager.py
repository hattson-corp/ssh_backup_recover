import subprocess
import argparse
import os 

class listuser:
    def __init__(self): 
        self.passwdFile = subprocess.check_output('getent passwd', shell=True).decode().split("\n")
        self.passwdFile.pop()
        self.users = []
        for line in self.passwdFile:
            sLine = int(line.split(":")[2])
            if sLine >= 1000:
                self.users.append(line.split(":")[0])

    def return_users(self):
        return self.users

parser = argparse.ArgumentParser()
def userList():
    obj = listuser()
    a = obj.return_users()
    for i in a:
        print("[+] Username : "+str(i))
parser.add_argument('-u', '--user', help='Show List of all users .')
parser.add_argument('-b', '--backup', help='Create a backup file into backup.txt file .')
parser.add_argument('-r','--recover',help='Recover users from backup.txt file . > python3 user_manager.py -r file.txt(contain user names only) -p password (password for all user) ')
parser.add_argument('-p','--password',help='Password for all users ')
arg = parser.parse_args()
user = arg.user
backup = arg.backup
recover = arg.recover
password = arg.password

if backup:
    listUser = listuser().return_users()
    path = os.path.abspath(os.getcwd())
    if os.path.isfile(f"{path}/backup.txt"):
        try:
            os.remove(f"{path}/backup.txt")
        except:
            pass
    for user in listUser:
        try:
            with open(f"{path}/backup.txt" , "a+") as out:
                out.write(f"{user}\n")
                print(f"[+] User {user}  => backup.txt ")
        except:
            print(f"[X] Failed backingup  user {user}")

if recover and password:
    path = os.path.abspath(os.getcwd())
    with open(f"{path}/{recover}", "r") as listUser:
        for user in listUser.readlines():
            try:
                work = subprocess.check_output('useradd -m  -p $(echo "{}" | openssl passwd -1 -stdin) {}'.format( password.strip().rstrip(), user.strip().rstrip()), shell=True).decode()
                print(f"[+] User {user} {work} ")
            except:
                print(f"[X] Failed creating user {user}")




if user:
    userList()
