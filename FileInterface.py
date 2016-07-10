import json

def getValue(name):
    with open('values') as jsonData:
        jsonParsed = json.load(jsonData)
    if name in jsonParsed:
        return jsonParsed[name]
    else:
        return None

def setValue(name, value):
    with open('values', 'r+') as f:
        jsonParsed = json.load(f)
        jsonParsed[name] = value
        f.seek(0)
        f.write(json.dumps(jsonParsed))
        f.truncate()
    return
