# TODO
Place all TODOs in here
### CONTENTS
- [General](#general)
- [Save data](#save-data)
- [Desktop App](#desktop-app)
- [Python CLI](#python-cli)
- [Coding Style](#coding-style)
- [Todos](#todos)
- [Timetable](#timetable)
- [Timer](#timer)
- [Settings](#settings)
- [Linux](#linux)
- [OS X](#os-x)
- [Windows](#windows)
- [Android](#android)
- [iOS](#iOS)
- [Licensing](#licensing)

### General
- Complete documentation for the project so far
- Get todos from app
- Put versioning info in docs 
- Fill up with TODOs from other files
- There may be todos inside any .py or .kv files
- Can you contribute to any of the projects this planner uses to help them and us run smoother and/or on more devices?
  - Kivy
  - Python
  - SQLite3
- Create the wiki (project outline, how-tos, etc.)
	- Installation guide
- Commit guide in the README?
- Create logo / notification / window icon
- Make the GUI look pretty
- In-package documentation solution?
- Gamification (points, reward, punishment, stats)
	- habits gain stats until they have been completed regularly for 1 year, then they become a trophy and you are no longer reminded,  can rescind your trophy is you fall out of habit accidentally etc.
- Rocket chat?
- SQLite to json converter?

### Save data
- Data syncs between installations on different platforms
	- Online userbase?
	- Database merging
	- Initial idea:
		Probably not scalable, but:
		- HTTP request on connection to service on home wifi network (e.g. 10.0.0.3 or 192.168.0.19)
- Try to keep stuff backwards compatible

### Desktop App
- Daily checkins
- Autostart / notification panel indicator icon thing
	- Ubuntu (test)
	- Unity
	- Windows
	- OS X
- Make stuff undoable?
- Print out progress log in other formats pdf, latex, png, svg?

### Python CLI
Started working on a python command line interface 
- TODOs
	- Sort / list todos [todo menu]
	- Edit todo
	- Delete todo
- EVENTs
	- Create event
	- Edit event
	- Delete event
	- Sort / list / review events
- REMINDERs
	- Create reminder (standalone OR from event / todo)
	- Edit reminder
	- Delete reminder
	- Sort / list reminders
- HABITs

### Android App
- 0.3 Turn portrait
- Put build instructions in docs
- Make https://github.com/renpytom/rapt-pygame-example work in python 3.5 (is this still of interest?)
- 0.3 Generate apk that works 

### iOS App

- Start iOS App

### Coding Style
- Check out PEP8 and try to make code consistent
- Decide how to use " or '
  - Current usage: "long string or reference (e.g. "filename.filetype")", 'tokenstring'

### Homepage
- Change name to Homepage (currently 'Today')
- Automatically generated todo list
	- sort todos by date / importance
- Optional timed day planner 
	- e.g. plan 8 til 9 13 hrs
	- For each task, estimate how long you think it'll take
	- Use in-built timers to measure how long it really takes
	- Look at graphs of differences?
	- Think of ways that data could be presented / if useful

### Todos
- Set up repeat / reminders feature
  - Repeating todos auto generate reminders, deleting a todo deletes associated reminders
  - How far in the future? How to make sure new reminders are generated (cannot create / delete infinite reminders)
- Checklist of sub-tasks, progress indicator on Today page
- Make + Todo form look pretty
- Date
	- Due date / ASAP / Whenever
	- Cannot set or confirm-dialogue past date
- Bool for overdue todo
- Delete confirmation popup
- Implement reminders
	- How to save, trigger?
	- Notifications?

### Calendar
- All (use calendar_ui, calendar_data)

### Timetable

### Timer

### Settings

### Linux
- Ubuntu desktop indicator
  - Put in project documentation

### OS X

### Windows

### Android
- Put in docs
- Installation
  - Use python-for-android / buildozer
  - Make it portrait
- Try to make installation keep only necessary deps
	- Try to reduce apk size

### iOS
- Check kivy documentation

### Licensing
- Determine which license / notice files need to be included in the project (e.g. MIT)
