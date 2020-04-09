import wx
import time
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from demo import main

class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        info = main()
        info_string = ""
        for line in info:
            info_string += str(line)
            info_string += "\n"
        
        super(HelloFrame, self).__init__(*args, **kw)
        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        st = wx.StaticText(pnl, label = info_string, style=wx.ALIGN_LEFT)
        font = wx.Font(10, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        st.SetFont(font)
        vbox.Add(st, flag=wx.ALL, border=15)
        pnl.SetSizer(vbox)
        
        self.Centre()
        self.SetSize((800, 800))
        self.makeMenuBar()
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")
            

    def makeMenuBar(self):
        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
        "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&file")
        menuBar.Append(helpMenu, "&help")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def OnExit(self, event):
        self.Close(True)

    def OnHello(self, event):
        wx.MessageBox("Hello again from wxPython")

    def OnAbout(self, event):
        wx.MessageBox("This is a wxPython Hello World Sample", "About Hello World 2", wx.OK|wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App()
    frm = HelloFrame(None, title='Betting predictions')
    frm.Show()
    app.MainLoop()