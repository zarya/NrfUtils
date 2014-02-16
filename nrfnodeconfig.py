#!/usr/bin/python

from struct import *
import socket

import wx
from wx.lib.wordwrap import wordwrap
import wx, wx.html
import sys

s = socket.socket()         # Create a socket object
host = "10.38.18.105" # Get local machine name
port = 12345                # Reserve a port for your service.
s.connect((host, port))

aboutText = """<p>Sorry, there is no information about this program. It is
running on version %(wxpy)s of <b>wxPython</b> and %(python)s of <b>Python</b>.
See <a href="http://wiki.wxpython.org">wxPython Wiki</a></p>"""

class HtmlWindow(wx.html.HtmlWindow):
    def __init__(self, parent, id, size=(600,400)):
        wx.html.HtmlWindow.__init__(self,parent, id, size=size)
        if "gtk2" in wx.PlatformInfo:
            self.SetStandardFonts()

    def OnLinkClicked(self, link):
        wx.LaunchDefaultBrowser(link.GetHref())
        sys.stdout.flush()
        time.sleep( interval )

class AboutBox(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "About Nrf Sensor netork config tool",
            style=wx.DEFAULT_DIALOG_STYLE|wx.THICK_FRAME|wx.RESIZE_BORDER|
                wx.TAB_TRAVERSAL)
        hwin = HtmlWindow(self, -1, size=(400,200))
        vers = {}
        vers["python"] = sys.version.split()[0]
        vers["wxpy"] = wx.VERSION_STRING
        hwin.SetPage(aboutText % vers)
        btn = hwin.FindWindowById(wx.ID_OK)
        irep = hwin.GetInternalRepresentation()
        hwin.SetSize((irep.GetWidth()+25, irep.GetHeight()+10))
        self.SetClientSize(hwin.GetSize())
        self.CentreOnParent(wx.BOTH)
        self.SetFocus()

class MyApp(wx.App):
    def showMessageDlg(self, msg, title, style):
        """"""
        dlg = wx.MessageDialog(parent=None, message=msg, 
                               caption=title, style=style)
        dlg.ShowModal()
        dlg.Destroy()

    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)

        self.frame = wx.Frame(None, wx.ID_ANY, title='Nrf Sensor Node OTA Config tool')
        self.panel = wx.Panel(self.frame, wx.ID_ANY)
        self.box = wx.BoxSizer(wx.VERTICAL)

        menuBar = wx.MenuBar()
        menu = wx.Menu()
        m_about = menu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, m_about)
        menuBar.Append(menu, "&Help")
        self.frame.SetMenuBar(menuBar)

        m_text = wx.StaticText(self.panel, -1, "Node ID:", (10,10))
        self.nodeid = wx.TextCtrl(self.panel, 201, pos=(70,10), size=wx.Size(60,20))

        m_text = wx.StaticText(self.panel, -1, "New node ID:", (140,10))
        self.newnodeid = wx.TextCtrl(self.panel, 201, pos=(230,10), size=wx.Size(60,20))

        b = wx.Button(self.panel, -1, "Set", (300,5))
        self.Bind(wx.EVT_BUTTON, self.SetID, b)
 

        b = wx.Button(self.panel, -1, "1W On", (10,35))
        self.Bind(wx.EVT_BUTTON, self.OneWireOn, b)
        b = wx.Button(self.panel, -1, "1W Off", (10,60))
        self.Bind(wx.EVT_BUTTON, self.OneWireOff, b)

        #OnDhtOn
        b = wx.Button(self.panel, -1, "DHT On", (100,35))
        self.Bind(wx.EVT_BUTTON, self.OnDhtOn, b)
        b = wx.Button(self.panel, -1, "DHT Off", (100,60))
        self.Bind(wx.EVT_BUTTON, self.OnDhtOff, b)

        b = wx.Button(self.panel, -1, "P0 On", (210,35))
        self.Bind(wx.EVT_BUTTON, self.OnPulseConfig, b)
        b = wx.Button(self.panel, -1, "P0 Off", (210,60))
        self.Bind(wx.EVT_BUTTON, self.OnPulseConfig, b)
        b = wx.Button(self.panel, -1, "P1 On", (300,35))
        self.Bind(wx.EVT_BUTTON, self.OnPulseConfig, b)
        b = wx.Button(self.panel, -1, "P1 Off", (300,60))
        self.Bind(wx.EVT_BUTTON, self.OnPulseConfig, b)

        b = wx.Button(self.panel, -1, "A0 On", (10,100))
        self.Bind(wx.EVT_BUTTON, self.OnAnalogConfig, b)
        b = wx.Button(self.panel, -1, "A0 Off", (100,100))
        self.Bind(wx.EVT_BUTTON, self.OnAnalogConfig, b)
        b = wx.Button(self.panel, -1, "A1 On", (210,100))
        self.Bind(wx.EVT_BUTTON, self.OnAnalogConfig, b)
        b = wx.Button(self.panel, -1, "A1 Off", (300,100))
        self.Bind(wx.EVT_BUTTON, self.OnAnalogConfig, b)
        b = wx.Button(self.panel, -1, "A2 On", (10,125))
        self.Bind(wx.EVT_BUTTON, self.OnAnalogConfig, b)
        b = wx.Button(self.panel, -1, "A2 Off", (100,125))
        self.Bind(wx.EVT_BUTTON, self.OnAnalogConfig, b)
        b = wx.Button(self.panel, -1, "A3 On", (210,125))
        self.Bind(wx.EVT_BUTTON, self.OnAnalogConfig, b)
        b = wx.Button(self.panel, -1, "A3 Off", (300,125))
        self.Bind(wx.EVT_BUTTON, self.OnAnalogConfig, b)
        b = wx.Button(self.panel, -1, "A4 On", (10,150))
        self.Bind(wx.EVT_BUTTON, self.OnAnalogConfig, b)
        b = wx.Button(self.panel, -1, "A4 Off", (100,150))
        self.Bind(wx.EVT_BUTTON, self.OnAnalogConfig, b)
        b = wx.Button(self.panel, -1, "A5 On", (210,150))
        self.Bind(wx.EVT_BUTTON, self.OnAnalogConfig, b)
        b = wx.Button(self.panel, -1, "A5 Off", (300,150))
        self.Bind(wx.EVT_BUTTON, self.OnAnalogConfig, b)
        b = wx.Button(self.panel, -1, "A6 On", (10,175))
        self.Bind(wx.EVT_BUTTON, self.OnAnalogConfig, b)
        b = wx.Button(self.panel, -1, "A6 Off", (100,175))
        self.Bind(wx.EVT_BUTTON, self.OnAnalogConfig, b)
        b = wx.Button(self.panel, -1, "A7 On", (210,175))
        self.Bind(wx.EVT_BUTTON, self.OnAnalogConfig, b)
        b = wx.Button(self.panel, -1, "A7 Off", (300,175))
        self.Bind(wx.EVT_BUTTON, self.OnAnalogConfig, b)
        self.frame.Show()

    def SetID(self, evt):
        nodeid = int(self.nodeid.GetValue(),8)
        newnodeid = int(self.newnodeid.GetValue(),8)
        data = pack('HcBH',nodeid, 'C', 6, newnodeid)
        s.send(data)

    def OneWireOn(self, evt):
        nodeid = int(self.nodeid.GetValue(),8)
        data = pack('HcBB', nodeid, 'C', 12,1)
        s.send(data)

    def OneWireOff(self, evt):
        nodeid = int(self.nodeid.GetValue(),8)
        data = pack('HcBB', nodeid, 'C', 12,0)
        s.send(data)

    def OnAbout(self, event):
        dlg = AboutBox()
        dlg.ShowModal()
        dlg.Destroy()

    def OnAnalogConfig(self, event):
        nodeid = int(self.nodeid.GetValue(),8)
        btn = event.GetEventObject()
        pinid = int(btn.GetLabelText()[1:2])
        action = btn.GetLabelText()[4:5]

        if action == "n":
            action = 1
        else:
            action = 0

        data = pack('HcBh', nodeid, 'C', pinid+13,action)
        s.send(data)

    def OnPulseConfig(self, event):
        nodeid = int(self.nodeid.GetValue(),8)
        btn = event.GetEventObject()
        pinid = int(btn.GetLabelText()[1:2])
        action = btn.GetLabelText()[4:5]

        if action == "n":
            action = 1
        else:
            action = 0

        data = pack('HcBh', nodeid, 'C', pinid+8,action)
        s.send(data)

    def OnDhtOn(self, event):
        dlg = wx.TextEntryDialog(self.panel, 'Enter IO Pin numer:',"Pin:","", style=wx.OK)
        dlg.ShowModal()
        new_dht = int(dlg.GetValue())
        if new_dht == 0 or new_dht == 2 or new_dht == 3 or new_dht == 4 or new_dht == 6 or new_dht == 9 or new_dht == 10:
            data = pack('HcBh', nodeid, 'C', 22,new_dht)
            s.send(data)
        else:
            self.showMessageDlg("Wrong pin try again", "ERROR", wx.OK|wx.ICON_EXCLAMATION)

    def OnDhtOff(self, event):
        data = pack('HcBh', nodeid, 'C', 22,0)
        s.send(data)
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
