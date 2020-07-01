from pysnmp.hlapi import *

ip = "10.31.70.107"

snmp_object = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)

snmp_object2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

result = getCmd(SnmpEngine(),
	CommunityData("public", mpModel=0),
	UdpTransportTarget((ip, 161)),
	ContextData(),
	ObjectType(snmp_object))

result2 = nextCmd(SnmpEngine(),
	CommunityData("public", mpModel=0),
	UdpTransportTarget((ip, 161)),
	ContextData(),
	ObjectType(snmp_object2),
    lexicographicMode=False)



for i in result:
    for y in i[3]:
        print(y)

for i in result2:
    for y in i[3]:
        print(y)
