# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 11:07:47 2016

@author: zhuchunwu
"""

from selenium import webdriver

url = 'http://www.baidu.com'

driver = webdriver.Firefox()
driver.get(url)