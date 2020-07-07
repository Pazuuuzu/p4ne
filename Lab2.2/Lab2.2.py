from flask import Flask
import re
import glob
import ipaddress


tabl = {}
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    web = '<h1><center>Я тут немного навоял<br><br><form action="http://127.0.0.1:5000/configs" target="_self"><button  style="width:300px;height:30px">Смотреть список хостов</button></center>'
    return web
@app.route('/configs')
@app.route('/configs/')
def host():
    hosts = str('<h2><center><form action="http://127.0.0.1:5000/" target="_self"><button  style="width:300px;height:30px">НАЗАД</button></form>')
    for x in tabl.keys():
        hosts = hosts + '<form action="http://127.0.0.1:5000/configs/'+str(x)+'" target="_self"><button  style="width:300px;height:30px">'+str(x)+'</button></form>'
    return hosts


@app.route('/configs/<hostname>')
def ip(hostname):
    v = str('<h2><center><center><form action="http://127.0.0.1:5000/configs/" target="_self"><button  style="width:300px;height:30px">НАЗАД</button></form>')
    for y in tabl.keys():
        if y == hostname:

            for z in tabl.get(hostname):
                v = v +'<br>' + str(z)
    return v



if __name__ == '__main__':
    way = glob.glob("C:\\test\config_files\*.txt")

    IPadd = []
    for file in way:
        with open(file) as newfile:
            for line in newfile:
                Host = re.match("^hostname (.+)", line)
                if Host:

                    host = Host.group(1)
                    IPadd = []
                IP = re.match("^ ip address (([0-9]{1,3}\.){3}[0-9]{1,3}) (([0-9]{1,3}\.){3}[0-9]{1,3})", line)
                if IP:

                    IPadd.append(ipaddress.IPv4Interface(str(IP.group(1)) + "/" + str(IP.group(3))))
                    tabl.update({host: IPadd})


app.run(debug=True)