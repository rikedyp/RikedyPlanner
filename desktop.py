# RikedyPlanner Desktop Application
# Python 2.7.12
# Kivy 1.10.0
# SQLite3

# TODO:
#	Checkbox for duedate for YYYY.MM.DD or ASAP (top of pile) or None (no due date)

# Make sure min kivy version
import kivy
kivy.require('1.10.0')

# Import kivy modules
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen #, FadeTransition
from kivy.core.window import Window

# Calendar widget + date picker
from calendar_ui import CalendarWidget, DatePicker, cal_data
# Save and load data methods
from savedata import *

from datetime import datetime

# Declare classes for kivy
class Switcher(ScreenManager):
	pass

class MainMenu(BoxLayout):
	pass

class TodayButton(Button):
	todoid = NumericProperty()
	def on_press(self):
		# Load Todo whose ID was clicked
		file = Savedata()
		# Retrieve dict of todos containing id, title, description, 
		# duedate, difficulty, importance, repeat
		todos = file.list('todos')
		switcher = self.parent.parent.parent.parent
		todoform = self.parent.parent.parent.parent.ids.todoform
		# Let TodoForm know to edit existing todo
		todoform.newtodo = 1
		# Get todo ID from button and set TodoForm edit ID
		todoform.editid = self.todoid
		# Load todo data into TodoForm form elements
		for todo in todos:
			if self.todoid == todo[0]:
				print("Today Todo Clicked")
				todoform.ids.title.text = todo[1]
				todoform.ids.description.text = todo[2]
				todoform.ids.datepicker.text = str(todo[3])
				todoform.ids.difficulty.text = str(todo[4])
				todoform.ids.importance.text = str(todo[5])
				todoform.ids.repeat.active = todo[6]
		switcher.current = "todoform"

class TodayScreen(Screen):

	def update(self):
		# Get save data
		file = Savedata()
		# Clear button widgets for update
		self.ids.todobuttonlist.clear_widgets()
		# Add a buttons for todos in database
		for todo in file.list('todos'):
			todobutton = TodayButton(text = todo[1], todoid = todo[0], size_hint = (1, None))
			self.ids.todobuttonlist.add_widget(todobutton)
		self.sort()

	def sort(self):
		# Load from database
		file = Savedata()
		# Dict to sort todos
		todosort = {}
		todosorted = {}
		today = cal_data.today_date_list()
		todaydate = str(today[0])+"."+str(today[1])+"."+str(today[2])
		# List by item type
		for todo in file.list('todos'):
			# {date: todoid}
			todosort[todo[3]] = todo[0]
		# Sort todos by date 
		for date in sorted(todosort.iterkeys()):
			todosorted[date] = todosort[date]
		print(todosorted)
		# Put todos into 'past', 'today', 'future'
		for date in todosorted:
			print(date)
			print(todaydate)
			if date == todaydate:
				print("Today--")
		# Create a dict of todo[0]: todo[3]
		# Sort dict
		# Retrieve todos in order
		# Today
		today = datetime.now().strftime("%d.%m.%Y")
			# Overdue (earliest first)
			# Due today
			# Due soon
		return(todosort)

class Timetable(Screen):
	N = NumericProperty(5) # N week timetable
	n = NumericProperty(8) # n periods per day

	def update(self):
		print("Timetable update")
		self.clear_widgets()
		Tweek = GridLayout(cols = self.N, spacing = 10, padding = 10, height = Window.height)
		for i in range(self.N):
			string = "i " + str(i)
			print(string)
			Tday = BoxLayout(orientation = 'vertical')
			for j in range(self.n):
				string = "j " + str(j)
				print(string)
				string = "Period " + str(j)
				Tperiod = TextInput(text = string, size_hint_y = 0.2)
				Tday.add_widget(Tperiod)
			Tweek.add_widget(Tday)
		self.add_widget(Tweek)

	# Load a timetable
	#	Add timetable table to savedata.py
	# If timetable doesn't exist, create timetable from popup wizard
	# Choose N weeks, N days / week starting on ***day, N Periods / day
	# Click on period to get popup 
		# Name period (e.g.)
		# Choose a todo or school class
		# Events automatically enter TT

class Timer(Screen):
	Timeleft = 0
	def run_timer(self):
		print("run timer")
		pass
	def run_stopwatch(self):
		print("run stopwatch")

class SettingsPage(Screen):
	def change_transition(self, choice):
		if choice == "Fade":
			self.parent.transition = kivy.uix.screenmanager.FadeTransition()
		elif choice == "Slide down":
			self.parent.transition = kivy.uix.screenmanager.SlideTransition(direction = "down")
		elif choice == "Slide right":
			self.parent.transition = kivy.uix.screenmanager.SlideTransition(direction = "right")
		elif choice == "Wipe":
			self.parent.transition = kivy.uix.screenmanager.WipeTransition()
		else:
			print("Bad transition choice")

class TodoForm(Screen):
	# Is a new todo being created? New = 0, Edit old = 1
	newtodo = NumericProperty(0)
	# ID of todo to be edited
	editid = NumericProperty(0)

	def save(self):
		# TODO: Can generalise to Event, reminder etc?
		if self.newtodo == 0:
			file = Savedata()
			# Create a new todo in database and retrieve its ID
			newtodoid = Todo().create()
			data = {
				'title': self.ids.title.text,
	            'description': self.ids.description.text,
	            'duedate': self.ids.datepicker.text, # Gotta work out python datetime methods
	            'difficulty': self.ids.difficulty.text,
	            'importance': self.ids.importance.text,
	            'repeat': self.ids.repeat.active
			}
			Todo().edit(newtodoid, data)
			printstring = "New Todo " + str(self.editid) + " saved"
		else:
			printstring = "Todo " + str(self.editid) + "saved."
			print(printstring)
			data = {
				'title': self.ids.title.text,
                'description': self.ids.description.text,
                'duedate': self.ids.datepicker.text, # Gotta work this out next
                'difficulty': self.ids.difficulty.text,
                'importance': self.ids.importance.text,
                'repeat': self.ids.repeat.active
			}
			Todo().edit(self.editid, data)
		self.parent.current = "todayscreen"
	
	def delete(self):
		printstring = "Todo " + str(self.editid) + "deleted."
		print(printstring)
		Todo().delete(self.editid)
		self.parent.current = "todayscreen"

	def set_today(self):
		# TODO - change active button on calendar
		today_list = cal_data.today_date_list()
		self.ids.datepicker.text = str(today_list[0])+"."+str(today_list[1])+"."+str(today_list[2])

class Scroller(ScrollView):
	pass

class ScreenLayout(BoxLayout):

	def __init__(self, **kwargs):
		super(ScreenLayout, self).__init__(**kwargs)
		self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
		self._keyboard.bind(on_key_down = self._on_keyboard_down)

	def _keyboard_closed(self):
		self._keyboard.unbind(on_key_down=self._on_keyboard_down)
		self._keyboard = None

	def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
		if keycode[1] == 'a':
			#print(DesktopApp)
			print("a")
		if keycode[1] == 'escape':
			DesktopApp().hide()
		return True

class DesktopApp(App):

	def build(self):
		Window.borderless = False
		Window.bind(on_request_close = self.hide)
		return ScreenLayout()

	def show(self):
		Window.hide()
		Window.show()

	def hide(self, _ = None, source = None):
		Window.hide()
		return True

if __name__ == "__main__":
	DesktopApp().run()