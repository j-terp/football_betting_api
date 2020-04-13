
import wx 
import time 
class progress_bar(wx.Frame): 
            
    def __init__(self, parent, title, lenght): 
            super(progress_bar, self).__init__(parent, title = title,size = (400,300))  
            self.InitUI(lenght) 
                
    def InitUI(self, lenght):    
        self.count = 0 
        pnl = wx.Panel(self) 
        vbox = wx.BoxSizer(wx.VERTICAL)
                
        hbox1 = wx.BoxSizer(wx.HORIZONTAL) 
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
                
        self.gauge = wx.Gauge(pnl, range = lenght, size = (250, 25), style =  wx.GA_HORIZONTAL) 
                
        hbox1.Add(self.gauge, proportion = 1, flag = wx.ALIGN_CENTRE) 
                
        vbox.Add((0, 30)) 
        vbox.Add(hbox1, flag = wx.ALIGN_CENTRE) 
        vbox.Add((0, 20)) 
        vbox.Add(hbox2, proportion = 1, flag = wx.ALIGN_CENTRE) 
        pnl.SetSizer(vbox) 
                
        self.SetSize((300, 200)) 
        self.Centre() 
            

    def increment(self, val):
        self.gauge.SetValue(val)
        
        self.gauge.UpdateWindowUI()
    
    def mainloop(self):
        ex.MainLoop()

if __name__ == "__main__":		
    ex = wx.App() 
    mywin = progress_bar(None,'Web scraping progress', 7)
    mywin.Show()
    mywin.increment(7)
    mywin.mainloop()




"""for y in range(5):
    time.sleep(1)
    mywin.gauge.SetValue(y)
    wx.Yield()
    mywin.gauge.UpdateWindowUI()
    """
