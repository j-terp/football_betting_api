import wx
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from demo import main

class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(HelloFrame, self).__init__(*args, **kw)

        pnl = wx.Panel(self)
        text = main()
        st = wx.StaticText(pnl, label = text)
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        pnl.SetSizer(sizer)

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
    self.st_RouteInfo.SetLabel("Hello")
    frm.Show()
    app.MainLoop()