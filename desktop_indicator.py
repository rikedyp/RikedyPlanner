#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This code is ripped from an example for a tutorial on Ubuntu Unity/Gnome AppIndicators:
# http://candidtim.github.io/appindicator/2014/09/13/ubuntu-appindicator-step-by-step.html

import os
import signal
import json
import time

from urllib2 import Request, urlopen, URLError

import gi
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify

from threading import Thread
from desktop import *

APPINDICATOR_ID = 'RikedyPlanner_Indicator'
APPINDICATOR_ICON = os.path.abspath('RPlanner.png')
#show_window = 0
from kivy.config import Config
Config.set('kivy', 'exit_on_escape', 'true')
#Config.set('log_level', 'trace', None)
Config.set('kivy', 'log_level', 'warning')
class Indicator():
    def Indicate(self):
        indicator = appindicator.Indicator.new(APPINDICATOR_ID, APPINDICATOR_ICON, appindicator.IndicatorCategory.SYSTEM_SERVICES)
        indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        indicator.set_menu(self.build_menu())
        notify.init(APPINDICATOR_ID)
        gtk.main()

    def build_menu(self):
        menu = gtk.Menu()
        item_today = gtk.MenuItem('Show')
        item_today.connect('activate', self.showToday)
        menu.append(item_today)
        item_joke = gtk.MenuItem('Joke')
        item_joke.connect('activate', self.joke)
        menu.append(item_joke)
        item_quit = gtk.MenuItem('Quit')
        item_quit.connect('activate', self.quit)
        menu.append(item_quit)
        menu.show_all()
        return menu

    def showToday(self, _):
        DesktopApp().show()

    def fetch_joke(self):
        # TODO - get broader joke API 
        request = Request("http://api.icndb.com/jokes/random?firstName=Hardeep&lastName=Sidhu")
        response = urlopen(request)
        joke = json.loads(response.read())['value']['joke']
        return joke

    def joke(self, _):
        notify.Notification.new("Joke", self.fetch_joke(), None).show()

    def quit(self, _):
        notify.uninit()
        DesktopApp().stop()
        gtk.main_quit()

if __name__ == "__main__":
    indicator_thread = Thread(target = Indicator().Indicate)
    indicator_thread.start()
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    desktopapp = DesktopApp()
    desktopapp.run()
