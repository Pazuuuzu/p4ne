from pysnmp.hlapi import *

ip = "10.31.70.107"
port = 161
community = 'public'
snmp_object = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_object2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

result = getCmd(SnmpEngine(),
	CommunityData(community, mpModel=0),
	UdpTransportTarget((ip, port)),
	ContextData(),
	ObjectType(snmp_object))

result2 = nextCmd(SnmpEngine(),
	CommunityData(community, mpModel=0),
	UdpTransportTarget((ip, port)),
	ContextData(),
	ObjectType(snmp_object2),
    lexicographicMode=False)



for i in result:
    for y in i[3]:
        print(y)

for i in result2:
    for y in i[3]:
        print(y)
