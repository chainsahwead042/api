from flask import Flask, jsonify
from pysnmp.hlapi import *

app = Flask(__name__)

# Example function to fetch PDU metrics via SNMP
def get_pdu_metrics(ip='192.168.1.100', community='public'):
    # Replace with actual OIDs of your PDU
    metrics = {}
    oids = {
        "temperature": "1.3.6.1.4.1.534.1.5.1.0",
        "fan_speed": "1.3.6.1.4.1.534.1.5.2.0",
        "power_usage": "1.3.6.1.4.1.534.1.5.3.0"
    }
    
    for key, oid in oids.items():
        iterator = getCmd(SnmpEngine(),
                          CommunityData(community, mpModel=0),
                          UdpTransportTarget((ip, 161)),
                          ContextData(),
                          ObjectType(ObjectIdentity(oid)))
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        if errorIndication or errorStatus:
            metrics[key] = None
        else:
            metrics[key] = int(varBinds[0][1])
    return metrics

@app.route("/metrics")
def metrics():
    data = get_pdu_metrics()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
