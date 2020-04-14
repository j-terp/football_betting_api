import wx
import threading
import  time

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None)
        panel = wx.Panel(self)
        btn1 = wx.Button(panel, label="test1")
        btn1.Bind(wx.EVT_BUTTON, self.onButton1)

        btn2 = wx.Button(panel, label="test2")
        btn2.Bind(wx.EVT_BUTTON, self.onButton2)

        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(btn1)
        sizer.Add(btn2)

        panel.SetSizer(sizer)


        self.maxPercent = 100
        self.percent = 0

    def onButton1(self, evt):
        self.StartThread(self.DoWork1)
        """
        while True:
         time.sleep(1)
         print("hello")
         """

    def onButton2(self, evt):
        self.StartThread(self.DoWork2)

    def StartThread(self, func, *args):
        thread = threading.Thread(target=func, args=args)
        thread.setDaemon(True)
        thread.start()

    def showProgress(self):
        self.progress = wx.ProgressDialog("sum in progress", "please wait", maximum=self.maxPercent, parent=self, style=wx.PD_SMOOTH|wx.PD_AUTO_HIDE)

    def destoryProgress(self):
        self.progress.Destroy()

    def updateProgress(self, percent):
        keepGoing = True
        time.sleep(1)
        while keepGoing and self.percent < percent:
            self.percent += 1
            (keepGoing, skip) = self.progress.Update(self.percent)
            time.sleep(0.1)


    def doSomething(self, take_time, taskPercent, say_something):
        time.sleep(take_time)
        (keepGoing, skip) = self.progress.Update(taskPercent, say_something+" done!")


    def DoWork1(self):
        self.StartThread(self.showProgress)

        taskPercent = 25
        self.StartThread(self.updateProgress, taskPercent)
        self.doSomething(5, taskPercent, "1st")

        taskPercent +=25
        self.StartThread(self.updateProgress, taskPercent)
        self.doSomething(5, taskPercent, "2nd")

        taskPercent +=25
        self.StartThread(self.updateProgress, taskPercent)
        self.doSomething(5, taskPercent, "3rd")

        taskPercent +=25
        self.StartThread(self.updateProgress, taskPercent)
        self.doSomething(5, taskPercent, "4th")

        self.destoryProgress()

    def DoWork2(self):
        self.StartThread(self.showProgress)

        taskPercent = 25
        self.doSomething(5, taskPercent, "1st")

        taskPercent +=25
        self.doSomething(5, taskPercent, "2nd")

        taskPercent +=25
        self.doSomething(5, taskPercent, "3rd")

        taskPercent +=25
        self.doSomething(5, taskPercent, "4th")

        self.destoryProgress()


if __name__ == '__main__':

    app = wx.App(0)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()