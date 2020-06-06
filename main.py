
# Tool to reenter society after COVID-19
# Make a GUI
# Make a nice GUI a very nice GUI

# We need a JSON File to keep track of the lists
import json
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
    write_to_json(data, answer, "events")
    save_data(data)
    # Displays the info on upcoming
    listbox.insert("end", answer)

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
listbox = tk.Listbox(upcoming_frame, width = 80, height = 5)
for item in data["events"]:
    listbox.insert("end", item)

spacer2 = tk.Frame(main, width = 70, height = 20)

# Events Frame
events_frame = tk.Frame(main, width = 70, height = 50, bg = "#A4F178")

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
listbox.pack()

spacer2.pack(fill = "x")

events_frame.pack(fill = "x")

spacer3.pack(fill = "x")

curfew_frame.pack(fill = "x")

spacer4.pack(fill = "x")

create_frame.pack(fill = "x")
create_butt.grid(row = 0, column = 0)


root.mainloop()
