from date import Day
from date import Month
from date import Date

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import calendar as cal

class Handler():
    builder = Gtk.Builder()
    builder.add_from_file("calendar.glade")

    start_cur_month = cal.start_date

    def on_window_closed(self, *args):
    	Gtk.main_quit(*args)

    def on_prev_clicked(self, button):
    	start_new_month = Date.prev_month(self.start_cur_month)
    	cal.render_calendar(start_new_month, builder)
    	self.start_cur_month = start_new_month

    def on_next_clicked(self, button):
    	start_new_month = Date.next_month(self.start_cur_month)
    	cal.render_calendar(start_new_month, builder)
    	self.start_cur_month = start_new_month

builder = Gtk.Builder()
builder.add_from_file("calendar.glade")
builder.connect_signals(Handler())

cal.render_calendar(cal.start_date, builder)

window = builder.get_object("window1")
window.show_all()

Gtk.main()