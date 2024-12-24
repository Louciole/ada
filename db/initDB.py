from sakura import Server
from os.path import abspath, dirname
import sys
from psycopg import sql

PATH = dirname(abspath(__file__))


class DBInitializer(Server):

    def initDB(self):
        self.referenceUniauth()
        self.db.cur.execute(open(self.path + "/db/schema.sql", "r").read())
        self.db.conn.commit()



initializer = DBInitializer(path=PATH[:-3], configFile="/server.ini", noStart=True)
initializer.initUniauth()
initializer.initDB()
print("DB ready")
