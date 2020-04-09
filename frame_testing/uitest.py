import wx
import time
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

#from demo import main

class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(HelloFrame, self).__init__(*args, **kw)

        pnl = wx.Panel(self)
        self.st = wx.StaticText(pnl, label = "Betting")
        font = self.st.GetFont()
        font.PointSize += 5
        font = font.Bold()
        self.st.SetFont(font)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        pnl.SetSizer(sizer)

        self.Centre()
        self.SetSize((1200, 800))
        self.makeMenuBar()
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")
        self.mycount = 0

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
        self.mycount += 1
        mystring = "Betting Display No: " + str(self.mycount)
        self.st.SetLabel(mystring)
        wx.MessageBox("Hello again from wxPython")

    def OnAbout(self, event):
        wx.MessageBox("This is a wxPython Hello World Sample", "About Hello World 2", wx.OK|wx.ICON_INFORMATION)
    
    def change_text(self, text):
        self.st.SetLabel(text)

    def message(self, message):
        wx.MessageBox(message)

if __name__ == '__main__':
    t = "LOLOLLOLLLLL"
    app = wx.App()
    frm = HelloFrame(None, title='Betting predictions')
    frm.change_text(t)
    frm.message("Your predictions are ready, click OK to show")
    frm.Show()
    app.MainLoop()