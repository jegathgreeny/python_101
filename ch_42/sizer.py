
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
        button_2 = wx.Button(self, label="damn it..hit me")

        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(button, proportion=1, flag=wx.ALL | wx.CENTER | wx.EXPAND, border=5)
        main_sizer.Add(button_2, 0, wx.ALL, 5)
        self.SetSizer(main_sizer)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
