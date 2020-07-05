import ipaddress
import glob
import re
way = glob.glob("C:\\test\config_files\*.txt")
prob = '____________________________________________'
IPadd = []
Interface = []
Hostname = []

for file in way:
    with open(file) as newfile:
        for line in newfile:
            IP = re.match("^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)",line)
            Inter = re.match("^interface (.+)", line)
            Host = re.match("^hostname (.+)", line)
            if IP:
                IPadd.append(ipaddress.IPv4Interface(str(IP.group(1)) + "/" + str(IP.group(2))))
            if Inter:
                Interface.append(Inter.group(0))
            if Host:
                Hostname.append(Host.group(0))

for i in IPadd :
    print(i)
print( '', prob,'', sep='\n')
for x in Interface :
    print(x)
print( '', prob,'', sep='\n')
for z in Hostname :
    print(z)