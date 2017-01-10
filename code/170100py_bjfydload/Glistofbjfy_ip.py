# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:14:00 2016

@author: zhuchunwu
"""

from pyquery import PyQuery as pq
import pymysql
import time
import urllib

def addintodb(inde,i,num,pageurl):
    global db
 #   print(db)
    with db.cursor() as cursor:
        sql = 'INSERT INTO listofbjfy(inde,i,num,pageurl) VALUES(%d,%d,%d,\'%s\')' % (inde,i,num,pageurl)
#        print(sql)
        cursor.execute(sql)
        db.commit()

def get_ip():
    f = urllib.request.urlopen('http://api.xicidaili.com/free2016.txt')
    iplist=f.readlines()
#    print(iplist)
    return(iplist)

def change_ip(iplist,inde):
    time.sleep(2)
    k = inde % 100
    ip = iplist[k].decode('utf-8')
    return(ip[0:-2])

db = pymysql.connect(host='localhost',user='root',passwd='1995',db='ex_dtb',port=3306,charset='utf8mb4')
list1 =[x for x in range(11,1000)]
sturl = 'http://www.bjcourt.gov.cn/cpws/index.htm?st=1&q=&sxnflx=0&ajlb=&jbfyId=&zscq=&ay=&ah=&startCprq=&endCprq=&page='
inde = 200
for i in list1:
    url = sturl + str(i)
    if inde % 100 == 0:
        iplist = get_ip()
    ip = change_ip(iplist,inde)
#    print(ip)
    proxy_handler = urllib.request.ProxyHandler({'http':''})
    page = pq(url,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'},proxy = ip)
#    print(page)
    num = 1
    for each in page('.p5_0 a').items():
        time.sleep(1)
        pageurl = 'http://www.bjcourt.gov.cn' + each.attr.href
        k = addintodb(inde,i,num,pageurl)
        inde  += 1
        num   += 1
db.close()
