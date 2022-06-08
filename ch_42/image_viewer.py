import wx

class WinFrame(wx.Frame):

    def __init__(self):
        super().__init__(None, title='Vision')
        panel = WinPanel(self, image_size=(240, 240))
        self.Show()


class WinPanel(wx.Panel):

    def __init__(self, parent, image_size):
        super().__init__(parent)
        self.max_size = 240

        img = wx.Image(*image_size)
        self.image_ctrl = wx.StaticBitmap(self, bitmap=wx.Bitmap(img))

        browse = wx.Button(self, label='Browse')
        browse.Bind(wx.EVT_BUTTON, self.on_browse)

        self.photo_txt = wx.TextCtrl(self, size=(200, -1))

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        h_sizer = wx.BoxSizer(wx.HORIZONTAL)

        main_sizer.Add(self.image_ctrl, 0, wx.ALL, 5)
        h_sizer.Add(browse, 0, wx.ALL, 5)
        h_sizer.Add(self.photo_txt, 0, wx.ALL, 5)
        main_sizer.Add(h_sizer, 0, wx.ALL, 5)

        self.SetSizer(main_sizer)
        main_sizer.Fit(parent)
        self.Layout()

    def on_browse(self, event):
        """Browse for an image file @param event: The event object"""
        wild_card = 'JPEG files (*.jpg)|*.jpg'
        with wx.FileDialog(None, "Choose a file", wildcard=wild_card, style=wx.ID_OPEN) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.photo_txt.SetValue(dialog.GetPath())
                self.load_image()

    def load_image(self):
        """Load the image and display it to the user."""
        file_path = self.photo_txt.GetValue()
        img = wx.Image(file_path, wx.BITMAP_TYPE_ANY)

        # Scale the image and preserve its aspect ratio.
        w = img.GetWidth()
        h = img.GetHeight()
        if w > h:
            new_w = self.max_size
            new_h = self.max_size * h / w
        else:
            new_w = self.max_size
            new_h = self.max_size * w / h

        img = img.Scale(new_w, new_h)

        self.image_ctrl.SiteBitmap(wx.Bitmap(img))
        self.Refresh()
        
if __name__ == '__main__':

    app = wx.App(redirect=False)
    frame = WinFrame()
    app.MainLoop()