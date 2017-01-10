# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:00:58 2016

@author: zhuchunwu
"""
import win32com.client
xl = win32com.client.Dispatch('Excel.Application') #创建一个com对象（用progID）

xl.Visible = 1 #使xl可见