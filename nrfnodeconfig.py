from struct import *
import socket

import wx
from wx.lib.wordwrap import wordwrap

s = socket.socket()         # Create a socket object
host = "10.38.18.105" # Get local machine name
port = 12345                # Reserve a port for your service.
s.connect((host, port))

class MyApp(wx.App):
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)

        self.frame = wx.Frame(None, wx.ID_ANY, title='Nrf Sensor Node OTA Config tool')
        self.panel = wx.Panel(self.frame, wx.ID_ANY)
        self.box = wx.BoxSizer(wx.VERTICAL)

        b = wx.Button(self.panel, -1, "Turn on OneWire", (10,35))
        self.Bind(wx.EVT_BUTTON, self.OneWireOn, b)
        b = wx.Button(self.panel, -1, "Turn off OneWire", (10,60))
        self.Bind(wx.EVT_BUTTON, self.OneWireOff, b)

        m_text = wx.StaticText(self.panel, -1, "Node ID:", (10,10))

        self.nodeid = wx.TextCtrl(self.panel, 201, pos=(70,10), size=wx.Size(60,20))

        self.frame.Show()

    def OneWireOn(self, evt):
        nodeid = int(self.nodeid.GetValue())
        data = pack('HcBB', nodeid, 'C', 14,1)
        s.send(data)

    def OneWireOff(self, evt):
        nodeid = int(self.nodeid.GetValue())
        data = pack('HcBB', nodeid, 'C', 14,0)
        s.send(data)

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
