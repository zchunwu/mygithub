# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 14:25:23 2017

@author: zhuchunwu
"""

import tkinter as tk
import requests
import json
import pymysql

class getTrans():
    def __init__(self,word):
        self.word = word
        self.savedata = []
        self.tran = str()

    def start(self):
        json = self.getJson()
       # print(json)
        reslut = self.showWord(json)
        self.formatTran()
        self.saveData()
        return(reslut)

    def getJson(self):
        transUrl = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index'
        payload = {'type':'AUTO','i':str(self.word),'doctype':'json','ue':'UTF-8'}
        page = requests.post(transUrl,data = payload)
        response = str(page.text)
        return json.loads(response)

    def showWord(self,json):
        try:
            for i in json['smartResult']['entries']:
                self.savedata.append(i)
            return(self.savedata)
        except Exception:
            return('-')

    def formatTran(self):
        for i in self.savedata:
            self.tran = self.tran + str(i) + '\n'

    def saveData(self):
        con = pymysql.connect(
                                host = 'localhost',
                                user = 'root',
                                password = '1995',
                                db = 'english',
                                charset = 'utf8mb4'
                                )
        try:

            if len(self.tran) != 0:
                with con.cursor() as c:
                    sql = 'INSERT INTO transwords (word,translation) VALUES(%s,%s)'
                    c.execute(sql,(self.word,self.tran) )
                    con.commit()
            else:
                pass
        except Exception:
            pass

class app():
    def __init__(self):
        self.app = tk.Tk()
        self.text = str()
        self.f = []

    def button1(self):
        word = str(self.in_txt.get())
        inst = getTrans(word)
        result = inst.start()
        for i in result:
            self.tframe.insert(1.0,str(i)+'\n\n')
#        for i in range(1,len(result)):
#            inde = str(i)+'.0'
#            inde = float(inde)
#            self.tframe.insert(inde,result[i]+'\n')


#        print('g')
#        print(self.in_txt.get())

    def start(self):
        ################
        for i in ['white','white','white']:
            self.f.append(tk.Frame(width = 20, height = 200,bg = i))
        self.in_txt = tk.Entry(self.f[0])
        self.tframe = tk.Text(self.f[2],width=21,height=20)
        self.button = tk.Button(self.f[1],text = 'DO',command = self.button1)

        ###############
        self.tframe.pack()
        self.button.pack()
        self.in_txt.pack()
        for i in [0,1,2]:
            self.f[i].pack()
        self.app.mainloop()



if __name__ == '__main__':
    app = app()
    app.start()
