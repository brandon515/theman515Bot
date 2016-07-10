import TelegramInterface as ti
import FileInterface as fi
import NetworkInterface as ni
import WordAction
import time

def parseMessage(jsonData):
    message = jsonData["message"]
    text = message["text"]
    cmdArray = []
    if "entities" in message:
        entArray = message["entities"]
        for ent in entArray:
            if ent["type"] == "bot_command":
                offset = ent["offset"]
                length = ent["length"]
                cmdArray.append(text[offset+1:offset+length])
    for cmd in cmdArray:
        returnMessage = None
        sender = message["chat"]["id"]
        if cmd == "status":
            returnMessage = "FUELED UP READY TO GO"
            print(str(sender) + " has requested the status of this machine")
        elif cmd == "ip":
            if sender == fi.getValue("MyChatID"):
                returnMessage = "External IP: " + ni.getExternalIP() + "\nInternal IP: " + ni.getInternalIP()
                print(str(sender) + " has requested the ip address of this machine, that number should be " + str(fi.getValue("MyChatID")))
        elif cmd == "word":
            returnMessage = WordAction.ex()
            print(str(sender) + " has requested a pashto word, I dont know what they would do this.")
        if returnMessage != None:
            ti.sendMessage(sender, returnMessage)
            print(str(sender) + " has been sent the message \"" + returnMessage + "\"")
    return

def parseEditedMessage(jsonData):
    return

def parseInlineQuery(jsonData):
    return

def parseChosenInlineResult(jsonData):
    return

def parseCallbackQuery(jsonData):
    return

def main():
    while True:
        updateArray = ti.getUpdates()
        if updateArray == None:
            time.sleep(1)
            continue
        for update in updateArray:
            if "message" in update:
                parseMessage(update)
            elif "edited_message" in update:
                parseEditedMessage(update)
            elif "inline_query" in update:
                parseInlineQuery(update)
            elif "chosen_inline_result" in update:
                parseChosenInlineResult(update)
            elif "callback_query" in update:
                parseCallbackQuery(update)
            else:
                print("new format that is not recognized by this program")
    return

if __name__ == "__main__":
    main()
