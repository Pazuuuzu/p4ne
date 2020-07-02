class Subnet:
    def __init__(self, n="0.0.0.0", p="/0"):
        self.network = n
        self.prefix = p
    def __str__(self):
        return self.network + self.prefix
    def getnet(self):
        return self.network
    def getprefix(self):
        return self.prefix


n1 = Subnet("192.168.1.0", "/24")
print(n1.getnet())
print(n1.getprefix())


class Add_gw(Subnet):
    def __init__(self, n = '0.0.0.0', p = '/0', gw = '0.0.0.0'):
        Subnet.__init__(self, n ,p)
        self.gateway = gw
    def getgw(self):
        return self.gateway

N2 = Add_gw('10.31.71.172', '/24', '10.31.71.1')
print(N2)
print(N2.getgw())