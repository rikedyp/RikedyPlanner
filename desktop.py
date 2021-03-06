#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen #, FadeTransition
from kivy.core.window import Window
from kivy.clock import Clock

#Contemplating whether to add pygame dependency, good for playing audio apparently
import pygame
from pygame.locals import *
import wave

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

class ButtonBox(BoxLayout):
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
				todoform.ids.difficulty.text = todoform.diffdict[todo[4]]
				todoform.ids.importance.text = todoform.impdict[todo[5]]
				todoform.ids.repeat.active = todo[6]
		switcher.current = "todoform"

class TodoCheck(CheckBox):
	pass

class TodayScreen(Screen):
	overdue = {}
	duetoday = {}
	thisweek = {}
	thismonth = {}
	def update(self):
		# TODO
			# Search bar where focus initiates ability to scroll through (or search through) all todos
			# Final design:
					# display only <= 3 non-must TODOs at a time except:
						# All must for this this week or today display at top
					# sub-sorted by importance
				# 1 Todos on front page:
				# 2 Overdue + 'ASAP' @ top in red
				# 3 Due today sorted by importance (green, orange)
				# 4 Due this week
				# 5 Has a due date
				# 6 No due date / 'Whenever'
		# Get save data
		file = Savedata()
		# Clear button widgets for update
		self.ids.todobuttonlist.clear_widgets()
		# Add a buttons for todos in database
		todos = file.sort('todos')
		if todos != None:
			for todo in todos:
				duedate = todo[3]
				# TODO - maybe do dates as list and unicode otherwise
				if duedate != None:
					# Dated todos
					today = file.get_today()
					today = str(today[0])+"."+str(today[1])+"."+str(today[2])
					if duedate == 'ASAP':
						todobuttontext = todo[1]
						todobutton = TodayButton(color = [1, 0.2, 0, 0.8], text = todobuttontext, todoid = int(todo[0]), size_hint = (1, None))
						self.ids.todobuttonlist.add_widget(todobutton)
					elif duedate < today:
						todobuttontext = todo[1]
						todobutton = TodayButton(color = [1, 0.6, 0, 0.8], text = todobuttontext, todoid = int(todo[0]), size_hint = (1, None))
						self.ids.todobuttonlist.add_widget(todobutton)
					elif duedate == today:
						todobuttontext = todo[1]
						todobutton = TodayButton(color = [0, 1, 0.3, 0.8], text = todobuttontext, todoid = int(todo[0]), size_hint = (1, None))
						self.ids.todobuttonlist.add_widget(todobutton)
					else:
						todobuttontext = todo[1]
						todobutton = TodayButton(color = [0, 0.8, 0.8, 0.8], text = todobuttontext, todoid = int(todo[0]), size_hint = (1, None))
						self.ids.todobuttonlist.add_widget(todobutton)
					# if duedate == 'Whenever':
					# 	print("Got whenever")
					# 	# put these last
					# 	todobuttontext = todo[1]
					# 	todobutton = TodayButton(color = [0, 0.8, 0.8, 0.8], text = todobuttontext, todoid = int(todo[0]), size_hint = (1, None))
					# 	self.ids.todobuttonlist.add_widget(todobutton, len(self.ids.todobuttonlist.children))
					# elif duedate == 'ASAP':
					# 	print("Got ASAP")
					# 	# put these first
					# 	todobuttontext = todo[1]
					# 	todobutton = TodayButton(color = [1, 0.2, 0.3, 0.8], text = todobuttontext, todoid = int(todo[0]), size_hint = (1, None))
					# 	self.ids.todobuttonlist.add_widget(todobutton)
					# else:			
		else:
			nonelabel = Label(text = "Nothing to do")
			self.ids.todobuttonlist.add_widget(nonelabel)


class TimeTable(Screen):
	N = NumericProperty(5) # N week timetable
	n = NumericProperty(8) # n periods per day

	def update(self):
		print("Timetable update")
		self.clear_widgets()
		Tweek = GridLayout(cols = self.N, spacing = 10, padding = 10, height = Window.height)
		for i in range(self.N):
			Tday = BoxLayout(orientation = 'vertical')
			for j in range(self.n):
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

class TimerPageManager(ScreenManager):
	pass

class TimerPage(Screen):
	pass

class StopWatch(Screen):
	seconds = NumericProperty(0)
	minutes = NumericProperty(0)
	hours = NumericProperty(0)
	days = NumericProperty(0)
	def increment_seconds(self, interval):
		self.seconds += interval
	def increment_minutes(self, interval):
	    self.minutes += 1
	    self.seconds = 0
	def increment_hours(self, interval):
		self.hours += 1
		self.minutes = 0
		self.seconds = 0
	def start(self): 
	    Clock.unschedule(self.increment_seconds)
	    Clock.unschedule(self.increment_minutes)
	    Clock.unschedule(self.increment_hours)
	    Clock.schedule_interval(self.increment_hours, 3600)
	    Clock.schedule_interval(self.increment_seconds, 0.001)
	    Clock.schedule_interval(self.increment_minutes, 60)
	def stop(self):
	    Clock.unschedule(self.increment_seconds)
	    Clock.unschedule(self.increment_minutes)
	    Clock.unschedule(self.increment_hours)
	def reset(self):
		self.seconds = 0
		self.minutes = 0
		self.hours = 0
		self.days = 0

class Timer(Screen):
	
	#load a sound
	sound_path = "sofpad-undersampled.wav"
	sound = wave.open(sound_path)
	frequency = sound.getframerate()
	#init game engine with audio
	#pygame.init()    
	pygame.mixer.init(frequency=frequency)       
	pygame.mixer.music.load(sound_path)
	# Set up timer variables	
	oldtime = NumericProperty(0)
	time = NumericProperty(20)
	seconds = NumericProperty(0)
	minutes = NumericProperty(0)
	hours = NumericProperty(0)
	days = NumericProperty(0)
	def decrement_time(self, interval):
	    self.time -= interval
	    if self.time <= 0:
			self.time = 0
			self.stop()
			#playback
			pygame.mixer.music.play()
	def start(self): 
		self.time = float(self.ids.textbox.text)
		self.oldtime = self.time
		Clock.unschedule(self.decrement_time)
		Clock.schedule_interval(self.decrement_time, .1)
	def stop(self):
	    Clock.unschedule(self.decrement_time)
	    pygame.mixer.music.stop()

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
	# Importance, difficulty saved as int for easier sorting
	# Dicts here to restore semantic representation
	impdict = {0: 'Pipe dream', 1: 'Trivial', 2: 'No worries', 3: 'Ought to', 4: 'Got to', 5: 'Must'}
	diffdict = {0: 'Trivial', 1: 'Easy', 2: 'Medium', 3: 'Hard', 4: 'Punishing'}
	importance = NumericProperty(0)
	difficulty = NumericProperty(0)
	def save(self):
		# TODO: Can generalise to Event, reminder etc?
		# Convert difficulty, importance to integer
		if self.newtodo == 0:
			file = Savedata()
			# Create a new todo in database and retrieve its ID
			newtodoid = Todo().create()
			data = {
				'title': self.ids.title.text,
	            'description': self.ids.description.text,
	            'duedate': self.ids.datepicker.text,
	            'difficulty': self.difficulty, 
	            'importance': self.importance,
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
                'duedate': self.ids.datepicker.text, 
                'difficulty': self.difficulty, 
                'importance': self.importance,
                'repeat': self.ids.repeat.active
			}
			Todo().edit(self.editid, data)
		self.parent.current = "todayscreen"
	
	def delete(self):
		printstring = "Todo " + str(self.editid) + "deleted."
		print(printstring)
		Todo().delete(self.editid)
		self.parent.current = "todayscreen"

	def set_date(self, date):
		# TODO - change active button on calendar
		if date == "today":
			today_list = cal_data.today_date_list()
			self.ids.datepicker.text = str(today_list[0])+"."+str(today_list[1])+"."+str(today_list[2])
		if date == "whenever":
			self.ids.datepicker.text = "Whenever"
		if date == "asap":
			self.ids.datepicker.text = "ASAP"

	def select_imp(self, importance):
		if importance == 'Pipe dream':
			self.importance = 5
		elif importance == 'Trivial':
			self.importance = 4
		elif importance == 'No worries':
			self.importance = 3
		elif importance == 'Ought to':
			self.importance = 2
		elif importance == 'Got to':
			self.importance = 1
		elif importance == 'Must':
			self.importance = 0

	def select_diff(self, difficulty):
		if difficulty == 'Trivial':
			self.difficulty = 4
		elif difficulty == 'Easy':
			self.difficulty = 3
		elif difficulty == 'Medium':
			self.difficulty = 2
		elif difficulty == 'Hard':
			self.difficulty = 1
		elif difficulty == 'Punishing':
			self.difficulty = 0

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
