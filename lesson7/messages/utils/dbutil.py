# enconding: utf-8
import MySQLdb


HOST = '127.0.0.1'
PORT = 3306
USER = 'root'
PASSWORD = 'jianxiong'
DB = 'jianxiong'


def execute_fetch(sql, args=None, one=True):
    conn = MysqlConnect(host=HOST, port=PORT, user=USER, password=PASSWORD, db=DB)
    _rt = conn.execute_fetch(sql, args, one)
    conn.close()
    return _rt


def execute_commit(sql, args=None):
    conn = MysqlConnect(HOST, PORT, USER, PASSWORD, DB)
    conn.execute_commit(sql, args)
    conn.close()


class MysqlConnect(object):

    def __init__(self, host, port, user, password, db):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__db = db
        self.__conn = None
        self.__cur = None

    def connect(self):
        if self.__conn is None:
            self.__conn = MySQLdb.connect(
                host=self.__host, port=self.__port, user=self.__user, password=self.__password, db=self.__db)
        if self.__cur is None:
            self.__cur = self.__conn.cursor()

    def execute_fetch(self, sql, args=None, one=False):
        rt = None
        self.connect()
        self.__cur.execute(sql, args)
        if one:
            rt = self.__cur.fetchall()
        else:
            rt = self.__cur.fetchone()
        return rt

    def execute_commit(self, sql, args=None):
        self.connect()
        self.__cur.execute(sql, args)
        self.__conn.commit()

    def close(self):
        if self.__cur:
            self.__cur.close()
        if self.__conn:
            self.__conn.close()
