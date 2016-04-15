# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 17:20:10 2016
"""
import wx
class MyApp(wx.App):#从wx.App继承MyApp
    def OnInit(self):
        frame = wx.Frame(None,title="Hello,World!")
        frame.Show(True)
        return True
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
