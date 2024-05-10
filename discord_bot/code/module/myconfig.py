import discord
import json

class myconfig:
    def __init__(self) -> None:
        
        self.json = {}
        self.prefix = ""
        self.helpchannel = 0
        self.helpmessage = {"message":"","embed":{}}
        self.guidechannel = 0
        self.guidemessage = {"message":"","embed":{}}
        self.joinchannel = 0
        self.joinmessage = {"message":"","embed":{}}
        self.embedtemp = ""
        self.serverid = 0
        self.username = ""
        pass
    def load(self,path):
        with open(path,"r",encoding="utf-8") as f:
            self.json = json.load(f)
        self.prefix = self.json["prefix"]
        self.helpchannel = self.json["helpchannel"]
        self.helpmessage = self.json["helpmessage"]
        self.guidechannel = self.json["guidechannel"]
        self.guidemessage = self.json["guidemessage"]
        self.joinchannel = self.json["joinchannel"]
        self.joinmessage = self.json["joinmessage"]
        self.embedtemp = self.json["embedtemp"]
        self.serverid = self.json["serverid"]
        self.username = self.json["username"]
        pass
    def save(self,path):
        self.json["prefix"] = self.prefix
        self.helpchannel = self.helpchannel
        self.helpmessage = self.helpmessage
        self.json["guidechannel"] = self.guidechannel
        self.json["guidemessage"] = self.guidemessage
        self.json["joinchannel"] = self.joinchannel
        self.json["joinmessage"] = self.joinmessage
        self.json["embedtemp"] = self.embedtemp
        self.json["serverid"] = self.serverid
        self.json["username"] = self.username
        with open(path,"w",encoding="utf-8") as f:
            json.dump(self.json,f,indent=4,ensure_ascii=False)
        pass
