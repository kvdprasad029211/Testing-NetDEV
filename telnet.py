import getpass
import sys
import telnetlib

HOST = '117.231.125.46'
user = "admin"
password = "NOMUS"

tn = telnetlib.Telnet(HOST)

tn.read_until('Username: ')
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("vt100\n") 

tn.write("ls\n")
tn.write("exit\n")

print(tn.read_all())
