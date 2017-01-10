# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 09:17:56 2016

@author: zhuchunwu
"""
from selenium import webdriver
#from selenium.webdriver.common.proxy import *
myproxy = '218.19.46.131:808'
url = 'http://whois.ipcn.org/'
desired_capabilities = webdriver.DesiredCapabilities.CHROME.copy()
desired_capabilities['proxy'] ={
                'proxyType':'MANUAL',
                'httpProxy':myproxy,
                'ftpProxy' :myproxy,
                'sslProxy' :myproxy,
                'noProxy'  :None,
                "class":"org.openqa.selenium.Proxy",
                "autodetect":False
                }
driver = webdriver.Remote(url,desired_capabilities)
#driver = webdriver.Chrome(proxy = proxy)
#driver.get(url)
