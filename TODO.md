# TODO
Place all TODOs in here
There may be todos inside any .py or .kv files
- 0.3 target version for this TODO
- Can you contribute to any of the projects this planner uses to help them and us run smoother and/or on more devices?
  - Kivy
  - Python
  - SQLite3

### CONTENTS
- [General](#general)
- [Save data](#save-data)
- [Desktop App](#desktop-app)
- [Python CLI](#python-cli)
- [Coding Style](#coding-style)
- [Todos](#todos)
- [Habits](#habits)
- [Timetable](#timetable)
- [Timer](#timer)
- [Checklists](#checklists)
- [Settings](#settings)
- [Linux](#linux)
- [OS X](#os-x)
- [Windows](#windows)
- [Android](#android)
- [iOS](#iOS)
- [Licensing](#licensing)

### General
- 1.0 Daily checkins  
	Choose from Morning, Evening (set times), neither or both  
		Format:  
			Daily habit review  
			Todos completed (for satisfaction) - soft maybe on this
			Upcoming tasks?
- 1.0 Figure out error handling / Exception best practice
- 0.5 separate concerns (kv, py files)
- 1.0 decide on file structure
- 1.0 Complete documentation for the project so far
- 1.0 Put versioning info in docs
- 1.0 Create the wiki (project outline, how-tos, etc.)
	- Installation guide
- 1.0 Create logo / notification / window icon
- 1.0 Make the GUI look pretty
- 1.0 In-package documentation solution?
- 1.0 Gamification (points, reward, punishment, stats)
	- habits gain stats until they have been completed regularly for 1 year, then they become a trophy and you are no longer reminded,  can rescind your trophy is you fall out of habit accidentally etc.
- 2.0 Rocket chat?
- SQLite to json converter?

### Save data
1.5 - Data syncs between installations on different platforms
	- Online userbase?
	- Database merging
	- Initial idea:
		Probably not scalable, but:
		- HTTP request on connection to service on home wifi network (e.g. 10.0.0.3 or 192.168.0.19)

### Desktop App
- Kivy settings setup script or instructions in docs
- 1.0 Daily checkins
- 0.5 Autostart / notification panel indicator icon thing
	- Ubuntu (test)
	- Unity
	- Windows
	- OS X
- 0.5 Decide: Make stuff undoable? 
- 1.0 Decide on input form layout
	- Description box that automatically resizes
	- Expandable checklist (sub-todos)
- 2.0 Print out progress log in other formats pdf, latex, png, svg?

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
- 0.5 Turn portrait
- Put build instructions in docs
- Make https://github.com/renpytom/rapt-pygame-example work in python 3.5 (is this still of interest?)
- 1.0 Generate apk that works

### iOS App
- Start iOS App

### Coding Style
- 1.0 Check out PEP8 and try to make code consistent
- 0.5 Decide how to use " or '
  - Current usage: "long string or reference (e.g. "filename.filetype")", 'tokenstring'

### Homepage
- Change name to Homepage (currently 'Today')
	- Maybe keep today
- Just generally make the GUI make sense
- Buttons have check-off button inside them
- Buttons reveal menu on click?
	- Add reminder
	- Delete item
	- Edit item
- Automatically generated todo list
	- sort todos by date / importance
- Optional timed day planner / daily check-in
	- e.g. plan 8 til 9 13 hrs
	- Choose from your todos
	- For each task, estimate how long you think it'll take
	- Use in-built timers to measure how long it really takes
	- Look at graphs of differences?
	- Think of ways that data could be presented / if useful
- Make a page w/ structure, this for home page?:
	- Today:
		Only must-dos dislpayed, once  enough have been checked off, top 3 most important due in the future
	- This week:
		Any due today but pushed off of Today by must-dos
		Any due this week in order of importance
	- This month:
		Calendar-style lay out with key dates highlighted
	- Next 3 months:
		PC view only?
	- This year:
		List of main goals
	- 5 years:
		Get dreamy

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
- Sort function

### Habits
Once reward/punishment system decided on, implement habits
Habits are like todos with habitica + / - system

### Calendar
- All (use calendar_ui, calendar_data)
- Events (similar to todos)
	- Make it so events can be linked to todos?
	- Link events to google calendar?
	- Push notification / reminders on platform
- Maybe something like a project plan assistant?

### Timetable
- Current status: A grid of textinputs
- Figure out implementation
	- Setup popup
		- How many (N) weeks to repeat?
		- How many days per week?
		- Starting on which day?
		- Length of periods (should be fully customisable)
			- base initial implementation on school 2 week
			- 2 periods - 15 min break - 1 period - lunch - 2 periods or something like that
		- How many periods per day?
	- Periods can be linked to todos or events / classes

### Timer
- 1.0 Fix crash when non-float put into countdown timer

### Checklists
- 1.0 Some kind of page / entity for things like shopping lists

### Settings
- Add more page transition options
	- Can you create your own novel page transitions?
- Colour / theme settings
- kivy.config settings management

### Linux
- Ubuntu desktop indicator
  - Change menu item "Today" to "Show"
  - Put in project documentation
  - currently uses /usr/share/icons/RPlanner.png, get it to use icon in folder or have install method or something

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
	- python
	- kivy
	- sqlite3
	- pygame
- Credit Derek Banas Kivy tutorial 5
- Make sure to go find and credit other people who's code you stole
- Calendar button / widget calendar_ui, calendar_data
