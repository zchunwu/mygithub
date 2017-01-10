# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 20:00:06 2016

@author: zhuchunwu
"""
import os
from selenium import webdriver as wd
from pyquery import PyQuery as pq
import pymysql
import time


class CD():    # change name to html and download what is need then delete txt
    def __init__(self, fold):
        self.fold = fold
        self.driver = wd.Chrome()
        self.db = pymysql.connect(
                        host='localhost',
                        user='root',
                        password='1995',
                        db='ex_dtb',
                        charset='utf8mb4'
                        )

    def GINFO(self):  # get information
        os.chdir(self.fold)
        Nlist = os.listdir(self.fold)
        for i in Nlist:
            Cname = i[:-3]+'html'
            os.rename(i, Cname)
            Fname = str(self.fold) + '\\'+str(Cname)
            self.DINFO(Fname)
            os.remove(Fname)
            print('delete   ' + Fname[-11:])

    def DINFO(self, Fname):  # get the detail information from every files
        info = []
        self.driver.get(Fname)
        doc = pq(self.driver.page_source)
        info.append(Fname[-11:-5])
        info.append(doc('.p_date').text())
        info.append(doc('.h3_22_m_blue').text())
        info.append(doc('b > span').text())
        info.append(doc('p > span').text())
#        print(info)
        print('get '+Fname[-11:])
        self.ADDTODB(info)

    def ADDTODB(self, info):
        with self.db.cursor() as cursor:
            sql = "INSERT INTO content(num,inde,time,titl,content,url,pageurl) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (info[0], info[0], info[1], info[2], info[4], info[3], info[0]))
            self.db.commit()
            print('INSERT')

a = CD(r'H:\data1')
a.GINFO()


'''
################
driver = wd.Chrome()
driver.get(r'F:\项目式文件管理2\1607python学习\161220bjfy\124162.html')
page = driver.page_source

################
doc = pq(page)
time  = doc('.p_date').text()
title = doc('.h3_22_m_blue').text()
typ1  = doc('b > span').text()
content = doc('p > span').text()

################
'''
