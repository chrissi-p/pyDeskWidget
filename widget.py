#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import cairo


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        print(self.get_type_hint())
        #self.set_type_hint(Gdk.WindowTypeHint.DOCK)
        self.set_name('myWindow')

        self.set_keep_below(True)
        self.set_default_size(800, 500)

        self.screen = self.get_screen()
        self.visual = self.screen.get_rgba_visual()
        if self.visual != None and self.screen.is_composited():
            self.set_visual(self.visual)

        self.set_app_paintable(True)


        self.label = Gtk.Label("Das ist ein etwas längerer Text. Und gleich mal schaun, ob zeilenumbruch geht.")
        self.label.set_name('myLabel')
        self.label.set_line_wrap(True)
        self.add(self.label)

        self.style_provider = Gtk.CssProvider()

        css = open('style.css', 'rb') # rb needed for python 3 support
        css_data = css.read()
        css.close()

        self.style_provider.load_from_data(css_data)

        Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        self.style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        self.connect("draw", self.area_draw)

    def area_draw(self, widget, cr):
        cr.set_source_rgba(.8, .8, .8, 0.2)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)

win = MyWindow()

win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
