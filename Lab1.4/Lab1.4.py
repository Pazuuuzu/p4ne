import random
import ipaddress


class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self, address, mask):
        ipaddress.IPv4Network.__init__(self, (address, mask), strict=False)
    def reg(self):
        return self.is_global and not (self.is_multicast or
                                       self.is_link_local or
                                       self.is_loopback or
                                       self.is_private or
                                       self.is_reserved or
                                       self.is_unspecified)

    def sort(self):
        return int(self.netmask) * 2 ** 32 + int(self.network_address)

def sortfunc(x):
    return x.sort()

ListResult = []

for i in range(1,100):
    address = random.randint(0x0A000000, 0xFFFF0000)
    mask = random.randint(8, 24)
    net = IPv4RandomNetwork(address, mask)
    if net.reg() and net not in ListResult:
     ListResult.append(net)

for n in sorted(ListResult, key=sortfunc):
    print("%20s" % n)