
import wx 
import time 
import threading
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
        self.MainLoop()

def test():
    while True:
        print("Hello")
        time.sleep(1)

def open_gauge(val):
    ex = wx.App() 
    mywin = progress_bar(None,'Web scraping progress', 7)
    mywin.Show()
    mywin.gauge.SetValue(val)
        
    mywin.gauge.UpdateWindowUI()

if __name__ == "__main__":		
    ex = wx.App() 
    mywin = progress_bar(None,'Web scraping progress', 7)
    mywin.Show()
    print("Got to here")
    y = threading.Thread(target=ex.MainLoop, args=())
    y.setDaemon(1)
    x = threading.Thread(target=mywin.increment, args=(3,))
    x.setDaemon(1)
    #t = threading.Thread(target=ex.MainLoop, args=())
    #t.setDaemon(1)
    #y = threading.Thread(target=mywin.increment, args=(5) )
    #y.setDaemon(1)
    #t.start()
    y.run()
    x.run()
    print("Got to here")
    mywin.increment(3)
    x.run()
    time.sleep(3)
    #x = threading.Thread(target=mywin.increment, args=(5,))
    #x.setDaemon(1)
    #x.run()
    #ex.MainLoop()
    time.sleep(5)
    #y.start()
    #for y in range(7):
        #mywin.increment(y)






"""for y in range(5):
    time.sleep(1)
    mywin.gauge.SetValue(y)
    wx.Yield()
    mywin.gauge.UpdateWindowUI()
    """
