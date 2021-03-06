# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:47:53 2016

@author: zhuchunwu
"""

import win32com
class easyExcel:  
      """A utility to make it easier to get at Excel.    Remembering 
      to save the data is your problem, as is    error handling. 
      Operates on one workbook at a time."""  
      def __init__(self, filename=None):
              self.xlApp = win32com.client.Dispatch('Excel.Application')  
              
              if filename:  
                  self.filename = filename  
                  self.xlBook = self.xlApp.Workbooks.Open(filename)  
              else:  
                  try:
                      self.xlBook = self.xlApp.Workbooks.Add()  
                      self.filename = ''    
                  except Exception:
                      pass
              
      def save(self, newfilename=None):  
          if newfilename:  
              self.filename = newfilename  
              self.xlBook.SaveAs(newfilename)  
          else:  
              self.xlBook.Save()      
      def close(self):  
          self.xlBook.Close(SaveChanges=0)  
          del self.xlApp  
      def getCell(self, sheet, row, col):  
          "Get value of one cell"  
          sht = self.xlBook.Worksheets(sheet)  
          return sht.Cells(row, col).Value  
      def setCell(self, sheet, row, col, value):  
          "set value of one cell"  
          sht = self.xlBook.Worksheets(sheet)  
          sht.Cells(row, col).Value = value  
      def getRange(self, sheet, row1, col1, row2, col2):  
          "return a 2d array (i.e. tuple of tuples)"  
          sht = self.xlBook.Worksheets(sheet)  
          return sht.Range(sht.Cells(row1, col1), sht.Cells(row2, col2)).Value  
      def addPicture(self, sheet, pictureName, Left, Top, Width, Height):  
          "Insert a picture in sheet"  
          sht = self.xlBook.Worksheets(sheet)  
          sht.Shapes.AddPicture(pictureName, 1, 1, Left, Top, Width, Height)  
      def cpSheet(self, before):  
          "copy sheet"  
          shts = self.xlBook.Worksheets  
          shts(1).Copy(None,shts(1))
          
      def show(self):
          self.xlApp.Visible = 1
        
a = easyExcel()
a.show()

