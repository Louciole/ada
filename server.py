import string
from os.path import abspath, dirname
from sakura import HTTPError, HTTPRedirect
from sakura.http import baseServer
import random

server = baseServer.BaseServer
PATH = dirname(abspath(__file__))

class Ada(server):
    features = {"errors": {404: "/static/404.html"}, "orm": True}

    @server.expose
    def index(self):
        return self.file(PATH + "/static/home.html")

    @server.expose
    def default(self, target, **kwargs):
        target = target.strip('/')
        res = self.db.getSomething("url",target)
        if res and res != []:
            raise HTTPRedirect(self.response,res["og"])
        else:
            raise HTTPError(self.response,404,"Not Found")

    @server.expose
    def addLink(self, link, pref=None, **kwargs):
        if not pref:
            uid = ''.join(random.sample(B62, 7))

            while 1:
                if self.db.getSomething("url",uid):
                    uid = ''.join(random.sample(B62, 7))
                else:
                    self.db.insertDict("url",{"id": uid,"og":link})
                    return uid
        else:
            uid=pref
            while 1:
                if self.db.getSomething("url",uid):
                    uid = pref + ''.join(random.sample(B62, 3))
                else :
                    self.db.insertDict("url",{"id": uid,"og":link})
                    return uid


B62 = string.digits + string.ascii_letters
Ada(path=PATH, configFile="/server.ini")
