# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 09:33:47 2016
"""
import wx
class Frame0(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self,parent = superior,title = "Example",pos = (100,200),size = (200,100))
        self.panel = wx.Panel(self)
        self.panel.Bind(wx.EVT_LEFT_UP,self.OnClick)
    
    def OnClick(self,event):
        posm = event.GetPosition()
        wx.StaticText(parent = self.panel,label = "Hello,Worlf!",pos = (posm.x,posm.y))
if __name__ == '__main__':
    app = wx.App()
    frame = Frame0(None)
    frame.Show(True)
    app.MainLoop()
