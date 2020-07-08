import paramiko, time
import re

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_connection.connect('10.31.72.160',username='restapi',password='j0sg1280-7@' ,look_for_keys=False, allow_agent=False)
session = ssh_connection.invoke_shell()

session.send("terminal length 0\n")
session.send("show interface \n")
time.sleep(3)
out = session.recv(10000)
z = out.decode()
r = z.split('\n')

inter = []

for line in r:
    Interface =  re.match("GigabitEthernet(.+)", line) or re.match("Loopback(.+)", line)or re.match("(.+)packets input(.+)", line)or re.match("(.+)packets output(.+)", line)
    if Interface:
        inter.append(Interface.group(0))


for i in inter:
    print(i)
session.close()