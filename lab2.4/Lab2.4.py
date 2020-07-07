import requests, json

from flask import Flask
from flask import jsonify
from flask import render_template

def nticket():
    url = 'https://devnetapi.cisco.com/sandbox/apic_em/api/v1/ticket'
    payload = {"username": "devnetuser", "password": "Cisco123!"}
    header = {"content-type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    return response.json()['response']['serviceTicket']

def host(ticket):
    url = "https://devnetapi.cisco.com/sandbox/apic_em/api/v1/host"
    header = {"content-type": "application/json", "X-Auth-Token":ticket }
    response = requests.get(url, headers=header, verify=False)
    return response.json()


def device(ticket):
    url = "https://devnetapi.cisco.com/sandbox/apic_em/api/v1/network-device"
    header = {"content-type": "application/json", "X-Auth-Token": ticket }
    response = requests.get(url, headers=header, verify=False)
    return response.json()

def topolog(ticket):
    url = "https://devnetapi.cisco.com/sandbox/apic_em/api/v1/topology/physical-topology"
    header = {"content-type": "application/json","X-Auth-Token": ticket }
    response = requests.get(url, headers=header, verify=False)
    return response.json()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("topology.html")

@app.route("/api/topology")
def topology():
    ticket = nticket()
    return jsonify(topolog(ticket)['response'])
@app.route("/api/device")
def device2():
    ticket = nticket()
    return jsonify(device(ticket))
@app.route("/api/host")
def host2():
    ticket = nticket()
    return jsonify(host(ticket))

if __name__ == '__main__':
    ticket = nticket()
    app.run(host='127.0.0.1', port=4007,debug=True)