# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 14:18:16 2016
@author: zhuchunwu
"""

from pyquery import PyQuery as pq
import pymysql
import time
from selenium import webdriver
import win32ui
import pickle

def addintodb(inde,i,num,pageurl):
    global db
    with db.cursor() as cursor:
        sql = 'INSERT INTO listofbjfy(inde,i,num,pageurl) VALUES(%d,%d,%d,\'%s\')' % (inde,i,num,pageurl)
        cursor.execute(sql)
        db.commit()
def getsnum():
    with db.cursor() as cursor:
        sql = "SELECT inde,i FROM listofbjfy order by inde desc limit 1 "
        cursor.execute(sql)
        index = cursor.fetchone()
        return index

def picklecode(page):
    with open('code.pkl','wb') as f:
        pickle.dump(page,f)

driver = webdriver.Chrome()
db = pymysql.connect(host='localhost',user='root',passwd='1995',db='ex_dtb',port=3306,charset='utf8mb4')
sturl = 'http://www.bjcourt.gov.cn/cpws/index.htm?st=1&q=&sxnflx=0&ajlb=&jbfyId=&zscq=&ay=&ah=&startCprq=&endCprq=&page='

index = getsnum()
print(index)
m = 1
snum = index[1] + 1
while m < 100:
    newinde = getsnum()
    enum = snum + 490 * m
    list1 =[x for x in range(snum,enum)]
    inde = newinde[0] + 1
    for i in list1:
        print(i)
        url = sturl + str(i)
        driver.get(url)
#        if i == 18903:
#            time.sleep(10)
        elem = driver.page_source
       # print(elem)
        print('length:'+str(len(elem)))
        if len(elem) < 6000:
            win32ui.MessageBox('input  code')
#            picklecode(elem)
            time.sleep(8)
            elem = driver.page_source
        elif len(elem) < 70000:
            curtime = time.strftime('%H:%M:%S',time.localtime())
            print('too fast,sleeping at %s' % curtime)
            time.sleep(600)
            driver.get(url)
            elem = driver.page_source
            while len(elem) < 70000:
                curtime = time.strftime('%H:%M:%S',time.localtime())
                print('sleep again at %s' % curtime)
                time.sleep(600)
                driver.get(url)
                elem = driver.page_source
     #   print('length:'+str(len(elem)))
        page = pq(elem)
        num = 1
        for each in page('.p5_0 a').items():
            pageurl = 'http://www.bjcourt.gov.cn' + each.attr.href
            k = addintodb(inde,i,num,pageurl)
            inde  += 1
            num   += 1
    m += 1
    snum = enum
    print('end with %d,sleeping' % i )
  #  driver.close()
    time.sleep(10)
db.close()

##5336
