# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:35:18 2016

@author: zhuchunwu
"""

#编写一个简单的com服务器
class PythonUtilities:
    _public_methods_ = ['SplitString']
    _reg_progid_ = 'PythonDemos.Utilities'
    _reg_clsid_  ='{5D3D3052-FC10-4D7D-8757-03AD95F0D5EA}'
    
    def SplitString(self,val,item = None):
        import string
        if item != None:
            item = str(item)
        return string.split(str(val),item)
        
if __name__ =='__main__':
    print('Registring COM server...')
    import win32com.server.unregister
    win32com.server.register.UseCommandLine(PythonUtilities)
    