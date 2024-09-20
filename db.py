'''
自己写一个数据库链接操作的类
'''
from os import truncate

import pymysql
from requests import delete


class DBTool():
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',database="test_journal"
                                    ,user='root',password='123456'
                                    ,charset='utf8')
        self.cursor = self.conn.cursor()

    def queryAll(self):
        self.cursor.execute('select * from journal')
        return self.cursor.fetchall()

    def queryOne(self, title):
        self.cursor.execute('select * from journal where title=%s', title)
        return self.cursor.fetchone()

    def insert(self, title, author,abstract):
        flag=False
        try:
            self.cursor.execute('insert into journal values (null,"{}","{}","{}")'.
                                format(title, author,abstract))
            self.conn.commit()
            flag=True
        except Exception as e:print(e)
        return flag
if __name__ == '__main__':
    dbTool = DBTool()


