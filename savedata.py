# Save data class
# Class to create, update and delete sqlite3 entries
# savefile.db contains full user save file
# A save file will contain:
#	Current + completed todos
#		Todos contain sub-todos [using checklists]
#	Current reminders [delete old]
#	Current + past events
#	Habit tracking data (good/bad habits with date tags)
#	Current checklists (shopping / todo lists)

import sys
import json
import uuid
import sqlite3 

class Savedata():

	# On new instance of Savedata
	def __init__(self):
		self.load()

	# Attempt to load database for use
	def load(self):
		# TODO: maybe include changeable default path
		#		save + recover duedate as python datetime
		try:
			# Load or create database file
			db = sqlite3.connect('savefile.db')
			# Get cursor objects
			cursor = db.cursor()
			# Check if tables exist and, if not, create
			cursor.execute('''
				CREATE TABLE IF NOT EXISTS
				todos(id INTEGER PRIMARY KEY, title TEXT,
				description TEXT, duedate TEXT, repeat INTEGER,
				repinfo TEXT, difficulty TEXT,
				importance TEXT, completed INTEGER)
			''')
			cursor.execute('''
				CREATE TABLE IF NOT EXISTS
				events(id INTEGER PRIMARY KEY, title TEXT,
				description TEXT, duedate TEXT, location TEXT)
			''')
			db.commit()
			cursor.execute('''
				SELECT title, description, duedate from todos
			''')
		except Exception as e:
			# Roll back changes if something goes wrong
			db.rollback()
			raise e
		finally:
			# Close the database connection
			db.close()

	def list(self, thing):
		all_rows = None
		data = {}
		if thing == 'todos':
			db = sqlite3.connect('savefile.db')
			cursor = db.cursor()
			cursor.execute('''SELECT id, title, description, duedate, 
				difficulty, importance, repeat FROM todos''')
			all_rows = cursor.fetchall()
			# for row in all_rows:
			# 	data[row[0]] = [row[1], row[2], row[3], row[4]]
		elif thing == 'events':
			db = sqlite3.connect('savefile.db')
			cursor = db.cursor()
			cursor.execute('''SELECT id, title, duedate FROM events''')
			all_rows = cursor.fetchall()		
		else:
			print("not listable item")
		return all_rows

	def save(self, thing = None):
		# method to save data to file
		# What if no data sent?
		# Save a specific item?
		pass

	def delete(self, delkey):
		printstring = "Deleting: " + self.data['todos'][delkey]['title']
		print (printstring)
		del self.data['todos'][delkey]
		self.save()
		self.load()
		# del self.data[todos][delid]

    
class Todo():
	# Class for creating and editing todos
	# Has:
	#	Unique id number Todo.id 
	#	Dictionary self.data
	def __init__(self):
		pass # Are inits always needed?
			
	def create(self):
		# Create a new todo and save to database
		try:
			db = sqlite3.connect('savefile.db')
			cursor = db.cursor()
			cursor.execute('''
				INSERT INTO todos(title, description, duedate, repeat, repinfo,
				difficulty, importance, completed)
				VALUES(:title, :description, :duedate, :repeat, :repinfo, :difficulty,
				:importance, :completed)''',
				{'title': "New todo", 'description': None,
				'duedate': None, 'repeat': 0, 'repinfo': None, 'difficulty': None,
				'importance': None, 'completed': 0})
			db.commit()
			return cursor.lastrowid
		except Exception as e:
			db.rollback()
			raise e
		finally:
			db.close()

	def edit(self, id, dict):
		# Edit a todo(id) using a dict of as many entries as you would like to change, all the rest will be left alone
		# TODO thing, value to dict
		# for thing in dict:
		# 	if thing = blah
		#	insert blah to table
		try:
			db = sqlite3.connect('savefile.db')
			cursor = db.cursor()
			for thing in dict:
				value = dict[thing]
				if thing == 'title':
					cursor.execute('''
						UPDATE todos SET title = ? WHERE id = ? ''',
						(value, id))
					db.commit()
				elif thing == 'description':
					cursor.execute('''
						UPDATE todos SET description = ? WHERE id = ? ''',
						(value, id))
					db.commit()
				elif thing == 'duedate':
					cursor.execute('''
						UPDATE todos SET duedate = ? WHERE id = ? ''',
						(value, id))
					db.commit()
				elif thing == 'repeat':
					cursor.execute('''
						UPDATE todos SET repeat = ? WHERE id = ? ''',
						(value, id))
					db.commit()
				elif thing == 'repinfo':
					cursor.execute('''
						UPDATE todos SET repinfo = ? WHERE id = ? ''',
						(value, id))
					db.commit()
				elif thing == 'difficulty':
					cursor.execute('''
						UPDATE todos SET difficulty = ? WHERE id = ? ''',
						(value, id))
					db.commit()
				elif thing == 'importance':
					cursor.execute('''
						UPDATE todos SET importance = ? WHERE id = ? ''',
						(value, id))
					db.commit()
				elif thing == 'completed':
					cursor.execute('''
						UPDATE todos SET completed = ? WHERE id = ? ''',
						(value, id))
					db.commit()
				else:
					print("Error! Invalid thing to edit (Savedata.Todo)")
		except Exception as e:
			db.rollback()
			raise e
		finally:
			db.close()

	def delete(self, id):
		# Delete a todo
		try:
			db = sqlite3.connect('savefile.db')
			cursor = db.cursor()
			cursor.execute('''DELETE FROM todos WHERE id = ? ''',
				(id,))
			db.commit()
		except Exception as e:
			db.rollback()
			raise e
		finally:
			db.close()

	def sort(self):
		# Sort todos by:
		#	ignore completed
		#	duedate (closest today)
		# 	importance (highest)
		# 	difficulty (highest)
		#	include all duedate = today
		#		+ other sorted
		#	return top3/today for display
		pass
	# Set reminder
	def set_reminder(self):
		pass

class Event():
	# Might get dangerous using this name
	def __init__(self):
		pass
	def create(self):
		# Create a new todo and save to database
		try:
			db = sqlite3.connect('savefile.db')
			cursor = db.cursor()
			cursor.execute('''
				INSERT INTO events(title, description, duedate,
				location)
				VALUES(:title, :description, :duedate, :location)''',
				{'title': "New event", 'description': None,
				'duedate': None, 'location': None})
			db.commit()
		except Exception as e:
			db.rollback()
			raise e
		finally:
			db.close()

	def edit(self, id, thing, value):
		# Edit a todo(id) and change the value of thing
		try:
			db = sqlite3.connect('savefile.db')
			cursor = db.cursor()
			if thing == 'title':
				cursor.execute('''
					UPDATE events SET title = ? WHERE id = ? ''',
					(value, id))
				db.commit()
			elif thing == 'description':
				cursor.execute('''
					UPDATE events SET description = ? WHERE id = ? ''',
					(value, id))
				db.commit()
			elif thing == 'duedate':
				cursor.execute('''
					UPDATE events SET duedate = ? WHERE id = ? ''',
					(value, id))
				db.commit()
			elif thing == 'location':
				cursor.execute('''
					UPDATE events SET location = ? WHERE id = ? ''',
					(value, id))
				db.commit()
			else:
				print("Error! Invalid thing to edit (Savedata.Event)")
		except Exception as e:
			db.rollback()
			raise e
		finally:
			db.close()

	def delete(self, id):
		# Delete a todo
		try:
			db = sqlite3.connect('savefile.db')
			cursor = db.cursor()
			cursor.execute('''DELETE FROM events WHERE id = ? ''',
				(id,))
			db.commit()
		except Exception as e:
			db.rollback()
			raise e
		finally:
			db.close()

	def sort(self):
		# Sort todos by:
		#	ignore completed
		#	duedate (closest today)
		# 	importance (highest)
		# 	difficulty (highest)
		#	include all duedate = today
		#		+ other sorted
		#	return top3/today for display
		pass
	# Set reminder
	def set_reminder(self):
		pass

class Reminder():

	def __init__(self, item = None):
		if item == None:
			# Create standalone reminder
			pass
		else:
			# Create reminder associated with Todo or Event
			pass
			
class Habit():

	# Variables
	def __init__(self):
		pass

class Checklist():
	def __init__(self):
		pass

if __name__ == "__main__":
	print("Cannot run this file (please read the docs)")
	sys.exit()