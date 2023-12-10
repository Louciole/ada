from configparser import ConfigParser
import os

import db_service as db


config = ConfigParser()

def importConf():
    try:
        config.read('./ada.ini')
    except:
        print("please create a ada.ini file")


if __name__ == '__main__':
    importConf()
    db = db.DB(user=config.get('DB', 'DB_USER'), password=config.get('DB', 'DB_PASSWORD'),
               host=config.get('DB', 'DB_HOST'), port=int(config.get('DB', 'DB_PORT')), db=config.get('DB', 'DB_NAME'))
    db.init()
    db.insertDict("url",{"id": "carbon","og":"https://carbonlab.dev"})
    print(db.getSomething("url","carbon"))
    db.resetTable("url")
    print("DB ready")
