import wx


class MyFrame(wx.Frame):
    """The frame of the application."""
    def __init__(self):
        """Initialize the frame attributes."""
        super().__init__(None, title="Hello Wind")
        panel = MyPanal(self)
        self.Show()


class MyPanal(wx.Panel):
    """The widgets for the application."""
    def __init__(self, parent):
        """Initialize the widget attributes."""
        super().__init__(parent)

        button_1 = wx.Button(self, label="press me")
        button_1.Bind(wx.EVT_BUTTON, self.on_button_1)

        button_2 = wx.Button(self, label="hit me")
        button_2.Bind(wx.EVT_BUTTON, self.on_button_2)

        # Stacks up the buttons horizontally or vertically.
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(
            button_1, proportion=1, flag=wx.ALL | wx.CENTER | wx.EXPAND, border=5
        )
        main_sizer.Add(button_2, 0, wx.ALL, 5)

        self.SetSizer(main_sizer)

    def on_button_1(self, event):
        """The event of button_1."""
        print("You clicked the first button.")

    def on_button_2(self, event):
        """The event of button_2."""
        print("You clicked the second button.")


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
