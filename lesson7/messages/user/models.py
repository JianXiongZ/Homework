from django.db import models
import MySQLdb
# Create your models here.


HOST = '127.0.0.1'
PORT = 3306
DB = 'jianxiong'
USER = 'root'
PASSWORD = 'jianxiong'
SQL = 'select username, password, age, tel from user'
SQL_insert = 'insert into user(username,password,age,tel) values(%s,%s,%s,%s)'
SQL_update = 'update user set password=%s,age=%s,tel=%s where username=%s'
SQL_DELETE = 'delete from user where username=%s'


class Connect(object):
    """docstring for Models"""

    def __init__(self, host, port, db, user, password):

        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.password = password
        self.con = None
        self.cour = None

    def connect_database(self):
        if self.con is None:
            con = MySQLdb.connect(host=self.host, port=self.port, db=self.db,
                                  user=self.user, password=self.password)
        if self.cour is None:
            cour = con.cursor()

    def select_sql(self, sql, one=False):
        self.cour.execute(sql)
        if one:
            rt = cour.fetchall()  # one is true
        else:
            rt = cour.fetchone()  # ont is false
        return rt

    def close(self):
        if self.con is not None:
            cour.close()
        if self.cour is not None:
            con.close()

    def modify_sql(self, sql, stub):
        self.cour.execute(sql, stub)
        self.con.commit()


def select_database(one, sql):
    connect = Connect(HOST, PORT, USER, PASSWORD, DB)
    connect.connect_database()
    connect.select_sql(one, sql)
    connect.close()


def modify_database(one, sql):
    connect = Connect(HOST, PORT, USER, PASSWORD, DB)
    connect.connect_database()
    connect.modify_sql(one, sql)
    connect.close()


class Four_method(object):
    """docstring for Four_method"""

    def __init__(self, users):
        self.users = users

    def validate(self, name, password):
        for user in self.users:
            temp = ('username', 'password', 'age', 'tel')
            user = dict(zip(temp, user))
        if user['username'] == name and user['password'] == password:
            return True
        return False

    def list_user(self, users):
        user_list = []
        for user in self.users:
            temp = ('username', 'password', 'age', 'tel')
            user = dict(zip(temp, user))
            user_list.append(user)
        return user_list

    def validate_save_user(self, function, name, password, age, tel):
        for user in self.users:
            if user[0] == name:
                return False, 'user is exited'
        else:
            function(sql, (name, password, age, tel))
            return True, 'add success'

    def update_user(self, name):
        for user in self.users:
            if user[0] == name:
                return user[1], user[2], user[3]

    def modify_update_user(self, function, sql, username, password, age, tel):
        function(sql, (password, age, tel, username))

    def delete_user(self, function, sql, username):
        function(sql, username)
