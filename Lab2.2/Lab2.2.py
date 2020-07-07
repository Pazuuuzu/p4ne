from flask import Flask, jsonify
import json
import sys
import re
import glob


tabl = {}
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    web = "Бла Бла Бла Бла Бла"
    return web

@app.route('/configs')
@app.route('/configs/')
def host():
    hosts = []
    for x in tabl.keys():
        hosts.append(x)
    return jsonify(hosts)


@app.route('/configs/<hostname>')
def ip(hostname):
    for y in tabl.keys():
        if y == hostname:

            return jsonify(tabl.get(hostname))
    return jsonify("Not found")

if __name__ == '__main__':
    way = glob.glob("C:\\test\config_files\*.txt")

    IPadd = []
    for file in way:
        with open(file) as newfile:
            for line in newfile:
                IPadd = []
                Host = re.match("^hostname (.+)", line)
                if Host:
                    host = Host.group(1)
                IP = re.match("^ ip address (([0-9]{1,3}\.){3}[0-9]{1,3}) (([0-9]{1,3}\.){3}[0-9]{1,3})", line)
                if IP:
                    IPadd.append('IP address '+"%20s" % str(IP.group(1)) + "        Mask " + "%20s" % str(IP.group(3)))

                    tabl.update({host: IPadd})


app.run(debug=True)