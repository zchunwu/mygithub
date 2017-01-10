# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:49:20 2016

@author: zhuchunwu
"""

from selenium import webdriver
from selenium.webdriver.common.proxy import *

myProxy = '113.18.193.20:80'

url='http://whois.ipcn.org/'

proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'ftpProxy': myProxy,
    'sslProxy': myProxy,
    'noProxy': '' # set this value as desired
    })

driver = webdriver.Firefox(proxy=proxy)

# for remote
caps = webdriver.DesiredCapabilities.FIREFOX.copy()
proxy.add_to_capabilities(caps)

driver = webdriver.Remote(desired_capabilities=caps)
driver.get(url)
