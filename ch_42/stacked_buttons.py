import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Hello Wind")
        panel = MyPanal(self)
        self.Show()


class MyPanal(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        button = wx.Button(self, label="press me")
        button_1 = wx.Button(self, label="hit me")
        button_2 = wx.Button(self, label="damn it..hit me")


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
