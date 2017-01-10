# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 20:26:15 2016

@author: zhuchunwu
"""

#可以不用webdriver，因为这个没有验证码

import pymysql
from selenium import webdriver
import time
from pyquery import PyQuery as pq


class getText():
    def __init__(self):
        self.snum = int()
        self.enum = int()
        self.db = pymysql.connect(
                                host = 'localhost',
                                user = 'root',
                                password = '1995',
                                db = 'ex_dtb',
                                charset = 'utf8mb4'
                                )
        self.result = tuple()
        self.index  = tuple()
        self.title  = str()
        self.content= str()
        self.time   = str()
        self.type   = str()
        self.driver = webdriver.Chrome()

    def start(self,stime = 5,pnum = 100000,looptime = 1):
        i = 1
        self.snum = self.getsnum() + 20
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        while i < 100:
            self.enum =self.snum + i * pnum
            while self.snum <= self.enum:
              #  print(self.snum,self.enum)
                time.sleep(stime)
                inst.loadurl()
                inst.get_text()
                inst.save_text()
                self.snum += 1
     #       self.driver.close()
            print('end with %s' % self.enum)
            i += 1
            self.snum = self.enum + 1
            print('start sleeping')
            time.sleep(60)
            print('start download %s' % self.snum)


    def loadurl(self):
        with self.db.cursor() as cursor:
            sql = "SELECT inde,pageurl FROM listofbjfy where inde = %s "
            cursor.execute(sql,(self.snum))
            self.result = cursor.fetchone()
       #     print(self.result)

    def get_text(self):
        self.driver.get(self.result[1])
        page = self.driver.page_source
        while len(page) < 80000:
            print('too fast sleep')
            time.sleep(300)
            self.driver.get(self.result[1])
            page = self.driver.page_source
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print(self.result[0])
      #  print(page)
        doc  = pq(page)
        self.time  = doc('.p_date').text()
        self.title = doc('.h3_22_m_blue').text()
        self.type  = doc('b > span').text()
        self.content = doc('p > span').text()


    def save_text(self):
        with self.db.cursor() as cursor:
            sql = "INSERT INTO content(num,inde,time,titl,content,url,pageurl) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,(self.snum,self.result[0],self.time,self.title,self.content,self.type,self.result[1]))
            self.db.commit()

    def getsnum(self):
        with self.db.cursor() as cursor:
            sql = "SELECT inde pageurl FROM content order by inde desc limit 1 "
            cursor.execute(sql)
            self.index = cursor.fetchone()
            return self.index[0]


if __name__ == '__main__':
    inst = getText()
    inst.start()

#    i = 1
#    snum = 18711
#    while i < 100:
#        enum = snum + i*300
#        inst = getText(snum,enum)
#        inst.start(3)
#        print('end with %s' % enum)
#        i += 1
#        snum = enum + 1
#        print('start sleeping')
#        time.sleep(1200)
#        print('start download %s' % snum)
