# Tool to reenter society after COVID-19

# We need a JSON File to keep track of the lists
import json
import time
import ctypes
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from datetime import datetime

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


class Clock():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(curfew_frame3,text="", font=('Helvetica', 20), fg='red')
        self.label.grid(row = 1, column =0, pady =(0,0))
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        hour = time.strftime("%H")
        minute = time.strftime("%M")
        self.label.configure(text=f"  {hour} :  {minute}")
        self.root.after(1000, self.update_clock)

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
    messagebox.showinfo("Reminder", "Please remember to wear a mask and wash your hands now that you are completed with the task!")
    #ctypes.windll.user32.MessageBoxW(0, "Please remember to wear a mask and wash your hands now that you are completed with the task!", "Reminder", 0)
    listbox1.insert("end", event)

def clear():
    listbox1.delete(0, "end")
    data["completed"] = []
    save_data(data)

def set_curfew():
        curfew = simpledialog.askstring("Input", "When does curfew start?", parent= main)
        time_of_day = simpledialog.askstring("Input", "AM or PM?", parent= main)
        print(f"Curfew starts in {curfew} {time_of_day}")

        newWindow = tk.Toplevel(curfew_frame3)
        # try and except for curfew format

        app=Clock()


def clear_curfew():
    pass

# This can be changed as we go along
title = "Sanitation Alert"


root = tk.Tk()
root.title(title)
root.resizable(False, False)
root.configure()
# Main Frame
main = tk.Frame(root, width = 70, height = 400 )

# Welcome Frame
welcome_frame = tk.Frame(main, width = 70, height = 60)
welcome_label = tk.Label(welcome_frame, text = "      WELCOME BACK!", font = ("Times New Roman", 50))

spacer1 = tk.Frame(main, width = 70, height = 40)
upcoming_label = tk.Label(spacer1, text = "Upcoming Events:", font = ("Times New Roman", 15))

# Upcoming Frame
upcoming_frame = tk.Frame(main, width = 70, height = 50)
upcoming_frame1 = tk.Frame(upcoming_frame, width = 20, height = 50)
upcoming_frame2 = tk.Frame(upcoming_frame, width = 50, height = 50)
scrollbar = tk.Scrollbar(upcoming_frame2, orient="vertical")
listbox = tk.Listbox(upcoming_frame2, width = 80, height = 5, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
for item in data["events"]:
    listbox.insert("end", item)


listbox_remove_butt = tk.Button(upcoming_frame1, text = "Complete Task",
font = ("Times New Roman", 12), command = remove)


spacer2 = tk.Frame(main, width = 70, height = 40)
events_label = tk.Label(spacer2, text = "Events Completed:", font = ("Times New Roman", 15))

# Events Frame
events_frame = tk.Frame(main, width = 70, height = 50)
events_frame1 = tk.Frame(events_frame, width = 20, height = 50)
events_frame2 = tk.Frame(events_frame, width = 50, height = 50)
scrollbar1 = tk.Scrollbar(events_frame2, orient="vertical")
listbox1 = tk.Listbox(events_frame2, width = 80, height = 5, yscrollcommand=scrollbar1.set)
scrollbar.config(command=listbox1.yview)
for item in data["completed"]:
    listbox1.insert("end", item)

listbox1_remove_butt = tk.Button(events_frame1, text = "Clear",
font = ("Times New Roman", 12), command = clear, width = 12)


spacer3 = tk.Frame(main, width = 70, height = 50)
curfew_label = tk.Label(spacer3, text = "Curfew:", font = ("Times New Roman", 15))

# Curfew Frame
curfew_frame = tk.Frame(main, width = 70, height = 50)
curfew_frame1 = tk.Frame(curfew_frame, width = 20, height = 50)
curfew_frame2 = tk.Frame(curfew_frame, width = 50, height = 50)
curfew_frame3 = tk.Frame(curfew_frame, width = 50, height = 50)

set_curfew_butt = tk.Button(curfew_frame1, text = "Set",
font = ("Times New Roman", 12), command = set_curfew, width = 12)

clear_curfew_butt = tk.Button(curfew_frame1, text = "Clear",
font = ("Times New Roman", 12), command = clear_curfew, width = 12)

curfew_label1 = tk.Label(curfew_frame2, text = "Curfew starts in :", font = ("Times New Roman", 15))
curfew_label2 = tk.Label(curfew_frame3, text = "Hours  :  Minutes", font = ("Times New Roman", 8))

# Create Frame
create_frame = tk.Frame(main, width = 70, height = 40)
create_butt = tk.Button(create_frame, text = "Create New Event                                             +",
font = ("Times New Roman", 25), command = create, width = 40)


# Place all widgets on screen
main.pack(fill="both", expand = True, padx = 30, pady = 30)

welcome_frame.pack(fill = "x")
welcome_label.grid(row = 0, column = 0)

spacer1.pack(fill = "x")
upcoming_label.grid(row = 0, column = 0)

upcoming_frame.pack(fill = "x")
upcoming_frame1.grid(row = 0, column = 0)
upcoming_frame2.grid(row = 0, column = 1)
listbox.grid(row = 0, column = 0)
scrollbar.grid(row = 0, column = 1, ipady = 28)
listbox_remove_butt.grid(row = 0, column = 2, padx = (0, 10))


spacer2.pack(fill = "x")
events_label.grid(row = 0, column = 0)

events_frame.pack(fill = "x")
events_frame1.grid(row = 0, column = 0)
events_frame2.grid(row = 0, column = 1)
listbox1.grid(row = 0, column = 0)
scrollbar1.grid(row = 0, column = 1, ipady = 28)
listbox1_remove_butt.grid(row = 0, column = 2, padx = (0, 10))

spacer3.pack(fill = "x")
curfew_label.grid(row = 0, column = 0)

curfew_frame.pack(fill = "x")
curfew_frame1.grid(row = 0, column = 0)
curfew_frame2.grid(row = 0, column = 1)
curfew_frame3.grid(row = 0, column = 2)
set_curfew_butt.grid(row = 0, column = 0, padx = (0, 10), pady = (0,10))
clear_curfew_butt.grid(row = 1, column = 0, padx = (0, 10), pady = (0,10))
curfew_label1.grid(row =0, column = 0, padx = (20,0))
curfew_label2.grid(row =0, column = 0, padx = (20,0), pady = (0,0))

spacer3.pack(fill = "x")

create_frame.pack(fill = "x")
create_butt.grid(row = 0, column = 0)


root.mainloop()
