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
        font = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.st.SetFont(font)
        #font.PointSize = 5
        #font = font.Bold()
        #self.st.SetFont(font)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        pnl.SetSizer(sizer)

        self.Centre()
        self.SetSize((800, 400))
        self.makeMenuBar()
        self.CreateStatusBar()
        self.mycount = 0

    def makeMenuBar(self):
        fileMenu = wx.Menu()
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        helpMenu = wx.Menu()
        self_destruct_menu = wx.Menu()
        self_destruct = self_destruct_menu.Append(wx.ID_EXECUTE)

        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&Quit")
        menuBar.Append(helpMenu, "&Help")
        menuBar.Append(self_destruct_menu, "&Execute order 66")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.OnSelf_destruct, self_destruct)

    def OnExit(self, event):
        self.Close(True)

    def OnAbout(self, event):
        wx.MessageBox("These are your betting predictions for which team will win, A stands for away team, H stands for home team and D stands for draw!")

    def OnSelf_destruct(self, event):
        mystring = "It will be done my lord!"

        wx.MessageBox(mystring)
                                
        self.Close(True)
    
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