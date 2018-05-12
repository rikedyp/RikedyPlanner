# RikedyPlanner v0.2
# RikedyP's Organiser App

from desktop import *
from desktop_indicator import *

global show_window 
show_window = 0

if __name__ == "__main__":
    indicator_thread = Thread(target = Indicator().Indicate)
    indicator_thread.start()
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    desktopapp = DesktopApp()
    desktopapp.run()