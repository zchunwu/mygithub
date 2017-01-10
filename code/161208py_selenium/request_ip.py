# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 10:04:10 2016

@author: zhuchunwu
"""

import requests

def getliofP():
    apiurl='http://tpv.daxiangdaili.com/ip/?tid=557576382820459&num=20&filter=on'  
    api =requests.get(apiurl)   
    api = str(api.text)
    lis1 = api.splitlines()
    return(lis1)
    
def checkP(lis1):
    checklis = []
    checkurl = 'http://whois.ipcn.org/'
    for i in lis1:
        proxies = {'http':'http://%s' %i}
        try:
            requests.get(checkurl,proxies = proxies)
            checklis.append(proxies)
            print(proxies)
        except Exception:
            print(i)
            pass
#        print(proxies)
    print(checklis)
    
lis1 = getliofP()
checkP(lis1)
        

