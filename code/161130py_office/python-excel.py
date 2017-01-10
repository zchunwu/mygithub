# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 13:43:25 2016

@author: zhuchunwu
python-excel win32com
"""

#出了个问题，以下代码直接运行报错，但是在console里运行可以，可以复制过去运行
from win32com.client import Dispatch
#import win32com.client
#import pythoncom

xlApp = Dispatch('Excel.Application')

xlApp.Visible = 1
try:
    xlApp.Workbooks.add()  #忽略这个错误
except Exception:
    xlApp.ActiveSheet.Cells(1,1).Value = 1
xlApp.Application.Quit()


#import win32com
#from win32com.client import Dispatch,constants
#e = win32com.client.Dispatch('Excel.Application')
#e.Visible = 1
#excel = e.WorkBooks.add()
##
#import win32com
#from win32com.client import Dispatch,constants
#
#w = win32com.client.Dispatch('Word.Application')
#w.Visible = 1
#
#doc = w.Documents.Add()
#
