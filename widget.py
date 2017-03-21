#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        #self.set_decorated(False)
        self.set_default_size(400, 600)
        self.set_opacity(0.5)

        self.label = Gtk.Label("test")
        self.add(self.label)

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        #self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hello World")

win = MyWindow()
#win.GtkWindowSetDecorate(selfe, False)
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
