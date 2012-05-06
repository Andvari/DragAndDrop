'''
Created on 05.05.2012

@author: Nemo
'''

import wx

class DrgWindow(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(DrgWindow, self).__init__(*args, **kwargs)
        self.SetBackgroundColour("BLACK")

class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.pnl = wx.Panel(self)
        
        self.wnd1 = DrgWindow(self.pnl, wx.ID_ANY, pos = (0, 0), style = wx.BORDER_SUNKEN)
        self.pnl.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouseEvent)
        self.wnd1.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouseEventWnd)
        self.fDragging = False
        
        self.Center()
        self.Show()
        
    def OnMouseEvent(self, e):
        if (e.LeftUp() | e.Moving()):
            self.fDragging = False

        if (e.Dragging()):
            if (self.fDragging):
                self.wnd1.SetPosition(e.GetPosition())
                
    def OnMouseEventWnd(self, e):
        if (e.LeftDown()):
            self.fDragging = True 

        if (e.LeftUp() | e.Moving()):
            self.fDragging = False
            
        if (e.Dragging()):
            self.wnd1.SetPosition(e.GetPosition() + self.wnd1.GetPosition())
            
app = wx.App()
mw = MainWindow(None, title = "Drag and Drop", size = (600, 600))
app.MainLoop()