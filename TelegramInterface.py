from datetime import datetime
import NetworkInterface as ni
import FileInterface as fi

def getUpdates():
    data = {"offset": fi.getValue("offset")}
    jsonData = ni.runPostMethod("getUpdates", data)
    if jsonData['ok'] == False:
        errStr = "Error has occured.\n\tError_Code: " + str(jsonData["error_code"]) + "\n\tDescription: " + jsonData["description"]
        print(errStr)
        sendMessage(fi.getValue("MyChatID"), errStr)
        return None
    results = jsonData["result"]
    if len(results) == 0:
        return None
    else:
        fi.setValue("offset", results[len(results)-1]["update_id"]+1)
        return results

def sendMessage(chatID, msg):
    data = {'chat_id': chatID, 'text': msg}
    response = ni.runPostMethod("sendMessage", data)
    if response["ok"] == False:
        print("Sending functionality is compromised\n\tError_Code: " + str(response["error_code"]) + "\n\tDescription: " + response["description"])
    return

def main():
    print("I dont know what to put here, will decide later")

if __name__ == "__main__":
    main()
