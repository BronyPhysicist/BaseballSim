import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler():

    def on_window_close(self, *args):
    	Gtk.main_quit(*args)

builder = Gtk.Builder()
builder.add_from_file("map_window.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()