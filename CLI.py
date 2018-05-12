# Command Line Interface for RikedyP's Organiser App [Todoer/ Thing doer]
import sys
import json
from savedata import *

class CLI():
    def __init__(self):
        print("Welcome to RikedyP Organiser Command Line Interface")
        # Load or create new save data savefile.json
        savefile = Savedata()
        self.menu(savefile)

    def menu(self, savefile):
        # Display no. of todos / events
        printstring = str(len(savefile.keys['todokeys'])) + " todos found."
        print(printstring)
        printstring = str(len(savefile.keys['eventkeys'])) + " events found"
        print(printstring)
        # List today's Todos + Events

        # Present menu options
        printstring = "Menu:\nCreate Todo [0]\nCreate Event [1]\nQuit [q]\n"
        choiceid = input(printstring)
        print(choiceid)
        if choiceid == '0':
            print("Input new todo details (all fields optional)")
            todo = Todo()
            todo.data['title'] = input("Title: ")
            todo.data['description'] = input("Description: ")
            todo.data['date'] = input("Due date: ")
            todo.data['difficulty'] = input("Difficulty: ")
            todo.data['importance'] = input("importance: ")
            savefile.save(todo)
        elif choiceid == '1':
            print("Input new event details (all fields optional")
            event = Event()
            event.data['title'] = input("Title: ")
            event.data['description'] = input("Description: ")
            event.data['date'] = input("Date: ")
            event.data['time'] = input("Time: ")
            event.data['location'] = input("Location: ")
            savefile.save(event)
        elif choiceid == 'q':
            sys.exit()
        else:
            self.menu(savefile)
    def edit(self):
        pass

if __name__ == "__main__":
    print("RUNNING CLI.py")
    CLI()