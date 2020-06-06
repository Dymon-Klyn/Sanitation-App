# Tool to reenter society after COVID-19
# Make a GUI
# Make a nice GUI a very nice GUI

# We need a JSON File to keep track of the lists
import json
import ctypes
import tkinter as tk
from tkinter import simpledialog

# Look of the GUI
"""
|     Welcome Back      |
-------------------------
|     upcoming ....     |
|     events completed  |
|     curfew in...      |
|     create new     +  |
"""

#JSON Functions
def move_data(data, event, old, new):
    data[new].append(event)
    data[old].remove(event)

def write_to_json(data, event, type):
    data[type].append(event)

def delete_event(data, event, type):
    data[type].remove(event)

def save_data(data):
    with open("data.txt", "w") as outfile:
        json.dump(data, outfile)

def load_json_data():
    with open("data.txt") as json_file:
        data = json.load(json_file)
    return data

data = load_json_data()


# Functions for the buttons go here
def create():
    answer = simpledialog.askstring("Input", "New Task", parent= main)
    # Json file should be here {upcoming:"answer"}

    # Displays the info on upcoming
    write_to_json(data, answer, "events")
    save_data(data)
    # Displays the info on upcoming
    listbox.insert("end", answer)

def remove():
    event = listbox.get("active")
    listbox.delete(listbox.index("active"))
    move_data(data, event, "events", "completed")
    save_data(data)
    ctypes.windll.user32.MessageBoxW(0, "Please remember to wear a mask and wash your hands now that you are completed with the task!", "Reminder", 0)
    listbox1.insert("end", event)

def clear():
    listbox1.delete(0, "end")
    data["completed"] = []
    save_data(data)



# This can be changed as we go along
title = "Sanitation Alert"
color = "red"

root = tk.Tk()
root.title(title)
root.resizable(False, False)
root.configure()
# Main Frame
main = tk.Frame(root, width = 70, height = 400 )

# Welcome Frame
welcome_frame = tk.Frame(main, width = 70, height = 60)
welcome_label = tk.Label(welcome_frame, text = "WELCOME BACK!", font = ("Times New Roman", 50))

spacer1 = tk.Frame(main, width = 70, height = 20)

# Upcoming Frame
upcoming_frame = tk.Frame(main, width = 70, height = 50, bg = color)
scrollbar = tk.Scrollbar(upcoming_frame, orient="vertical")
listbox = tk.Listbox(upcoming_frame, width = 80, height = 5, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
for item in data["events"]:
    listbox.insert("end", item)


listbox_remove_butt = tk.Button(upcoming_frame, text = "Complete Task",
font = ("Times New Roman", 12), command = remove)


spacer2 = tk.Frame(main, width = 70, height = 20)

# Events Frame
events_frame = tk.Frame(main, width = 70, height = 50, bg = "#A4F178")
scrollbar1 = tk.Scrollbar(events_frame, orient="vertical")
listbox1 = tk.Listbox(events_frame, width = 80, height = 5, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
for item in data["completed"]:
    listbox1.insert("end", item)

listbox1_remove_butt = tk.Button(events_frame, text = "Clear",
font = ("Times New Roman", 12), command = clear)


spacer3 = tk.Frame(main, width = 70, height = 20)

# Curfew Frame
curfew_frame = tk.Frame(main, width = 70, height = 50, bg = "#EFED85")

spacer4 = tk.Frame(main, width = 70, height = 20)

# Create Frame
create_frame = tk.Frame(main, width = 70, height = 40)
create_butt = tk.Button(create_frame, text = "Create New                                               +",
font = ("Times New Roman", 25), command = create)


# Place all widgets on screen
main.pack(fill="both", expand = True, padx = 30, pady = 30)

welcome_frame.pack(fill = "x")
welcome_label.grid(row = 0, column = 0)

spacer1.pack(fill = "x")

upcoming_frame.pack(fill = "x")
listbox.grid(row = 0, column = 0)
scrollbar.grid(row = 0, column = 1)
listbox_remove_butt.grid(row = 0, column = 2)


spacer2.pack(fill = "x")

events_frame.pack(fill = "x")
listbox1.grid(row = 0, column = 0)
scrollbar1.grid(row = 0, column = 1)
listbox1_remove_butt.grid(row = 0, column = 2)

spacer3.pack(fill = "x")

curfew_frame.pack(fill = "x")

spacer4.pack(fill = "x")

create_frame.pack(fill = "x")
create_butt.grid(row = 0, column = 0)


root.mainloop()
