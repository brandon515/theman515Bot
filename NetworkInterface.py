import json
import requests
import FileInterface as fi
import socket

def runPostMethod(method, payload=None):
    url = fi.getValue("base_url")
    apiKey = fi.getValue("api_key")
    completeUrl = url + apiKey + "/" + method
    try:
        response = requests.get(completeUrl, payload)
        jsonResponse = json.loads(response.text)
    except ValueError:
        print(method + " produced invalid JSON")
        jsonResponse = None
    except requests.exceptions.SSLError:
        print(method + " recvieved an SSL Error")
        jsonResponse = None
    return jsonResponse

def getExternalIP():
    ip = requests.get('https://api.ipify.org').text
    return ip

def getInternalIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",53))
    ip = str(s.getsockname()[0])
    s.close()
    return ip

