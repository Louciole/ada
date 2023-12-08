import datetime

import psycopg
from psycopg.rows import dict_row
from psycopg import sql

class DB:
    def __init__(self, user, password, host, port, db):
        try:
            self.conn = psycopg.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                dbname=db,
                row_factory=dict_row
            )
        except psycopg.Error as e:
            print(f"Error connecting to PostGreSQL : {e}")
            exit()

        self.cur = self.conn.cursor()

    def getSomething(self, table, id, selector='id'):
        self.cur.execute(sql.SQL('SELECT * FROM {} WHERE {} = %s').format(sql.Identifier(table),sql.Identifier(selector)), (id,))
        r = self.cur.fetchone()
        if r:
            return r
        else:
            return

    def insertDict(self, table, dict, getId=False):
        cols = []
        vals = []
        for key in dict:
            cols.append(sql.Identifier(key))
            vals.append(dict[key])
        cols_str = sql.SQL(',').join(cols)
        vals_str = sql.SQL(','.join(['%s' for i in range(len(vals))]))
        if getId:
            sql_str = sql.SQL("INSERT INTO {} ({}) VALUES ({}) RETURNING id").format(sql.Identifier(table), cols_str, vals_str)
        else:
            sql_str = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(sql.Identifier(table), cols_str, vals_str)
        print("result",sql_str)
        self.cur.execute(sql_str,vals)
        self.conn.commit()
        if getId:
            r = self.cur.fetchone()
            self.conn.commit()
            return r['id']

    def insertReplaceDict(self, table, dict):
        cols = []
        vals = []
        for key in dict:
            cols.append(sql.Identifier(key))
            vals.append(dict[key])
        cols_str = sql.SQL(',').join(cols)
        vals_str = sql.SQL(','.join(['%s' for i in range(len(vals))]))
        sql_str = sql.SQL("INSERT INTO {} ({}) VALUES ({}) ON CONFLICT (id) DO UPDATE SET ({}) = ({})"
        ).format(sql.Identifier(table), cols_str, vals_str, cols_str, vals_str)  # warning only working for dicts containing an id
        print("result",sql_str)
        self.cur.execute(sql_str,vals*2)
        self.conn.commit()

    def init(self):
        self.cur.execute(open("./db/create_adaDB.sql", "r").read())
        self.conn.commit()

    def resetTable(self, table):
        sql_str = """delete from {} cascade;ALTER SEQUENCE {} RESTART WITH 1""".format(table, table + "_id_seq")
        self.cur.execute(sql_str)
        self.conn.commit()

    def edit(self,table, id, element, value):
        self.cur.execute(sql.SQL("UPDATE {} SET {} = %s WHERE id = %s ").format(sql.Identifier(table),sql.Identifier(element)), (value, id))
        self.conn.commit()

    def deleteSomething(self,table,id):
        sql_str = sql.SQL("delete from {} where id = %s").format(sql.Identifier(table))
        self.cur.execute(sql_str,(id,))
        self.conn.commit()
