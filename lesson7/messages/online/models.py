from django.db import models
import json
import MySQLdb
from datetime import datetime
from utils import dbutil
# Create your models here.

SQL_MESSAGES_LIST_COLLMNS = ['publish_date', 'username', 'title', 'content']
SQL_ALL = 'select publish_date,username,title,content from message3;'
SQL_Insert = 'insert into message3(publish_date,username,title,content) values(now(),%s,%s,%s)'
SQL_Update = 'update message3 set title=%s,content=%s where username=%s'
SQL_Delete = 'delete from message3 where username=%s and title=%s and content=%s'
def get_messages():
    lines = dbutil.execute_fetch(SQL_ALL)
    rt_list = []
    for line in lines:
        message = dict(zip(SQL_MESSAGES_LIST_COLLMNS, line))
        if message['publish_date']:
            message['publish_date'] = message['publish_date'].strftime('%Y-%m-%d %H:%M:%S')
        rt_list.append(message)
    return rt_list
#    return [dict(zip(SQL_MESSAGES_LIST_COLLMNS, line)) for line in rt_list]


def save_message(username, title, content):
    dbutil.execute_commit(SQL_Insert,(username, title, content))


def update_message(username, title, content):
	dbutil.execute_commit(SQL_Update,(title, content, username))


def delete_message(username, title, content):
	dbutil.execute_commit(SQL_Delete,(username, title, content))