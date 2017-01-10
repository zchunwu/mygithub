# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 10:01:08 2016

@author: zhuchunwu
"""

from selenium import webdriver

PROXY = "60.169.78.218:808"

# Create a copy of desired capabilities object.
desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER.copy()
# Change the proxy properties of that copy.
desired_capabilities['proxy'] = {
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "noProxy":None,
    "proxyType":"MANUAL",
    "class":"org.openqa.selenium.Proxy",
    "autodetect":False
}

# you have to use remote, otherwise you'll have to code it yourself in python to 
# dynamically changing the system proxy preferences
driver = webdriver.Remote("http://www.baidu.com", desired_capabilities)