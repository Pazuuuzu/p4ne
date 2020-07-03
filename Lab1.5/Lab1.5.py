
import glob
way = glob.glob("C:\\test\config_files\*.txt")
adress = "ip address"
dh = 'dhcp'
Y = set()

for file in way:
    with open(file) as newfile:
        for line in newfile:
            if line.find(adress) == 1 and dh not in line:
                Y.add(line.replace(adress, "").strip())

for i in Y:
    print("%30s" % i)