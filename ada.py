import random
from os.path import abspath, dirname

import cherrypy
from configparser import ConfigParser

from db import db_service as db

import string

class Ada(object):
    @cherrypy.expose
    def index(self):
        return open(PATH + "/ressources/home.html")

    @cherrypy.expose
    def default(self, target, **kwargs):
        res = table.get(target)
        if res:
            raise cherrypy.HTTPRedirect(res)
        else:
            raise cherrypy.HTTPError("404")

    @cherrypy.expose
    def addLink(self, link, pref=None):
        if not pref:
            uid = ''.join(random.sample(B62, 7))

            while 1:
                if table.get(uid):
                    uid = ''.join(random.sample(B62, 7))
                else:
                    table[uid] = link
                    return uid
        else:
            uid=pref
            while 1:
                if table.get(uid):
                    uid = pref + ''.join(random.sample(B62, 3))
                else :
                    table[uid] = link
                    return uid

config = ConfigParser()
PATH = dirname(abspath(__file__))

# TODO delete below

B62 = string.digits + string.ascii_letters

table = {}


# TODO delete before


def importConf():
    try:
        config.read(PATH + '/ada.ini')
    except:
        print("please create a ada.ini file")


if __name__ == '__main__':
    importConf()
    db = db.DB(user=config.get('DB', 'DB_USER'), password=config.get('DB', 'DB_PASSWORD'),
               host=config.get('DB', 'DB_HOST'), port=int(config.get('DB', 'DB_PORT')), db=config.get('DB', 'DB_NAME'))

    cherrypy.config.update({'server.socket_host': config.get('server', 'IP'),
                            'server.socket_port': int(config.get('server', 'PORT')), 'tools.staticdir.on': True,
                            'tools.staticdir.dir': abspath(PATH + '/ressources'),
                            'error_page.404': PATH + "/ressources/404.html"})
    cherrypy.quickstart(Ada())
