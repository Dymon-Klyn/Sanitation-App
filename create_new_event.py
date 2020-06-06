def create():
    import tkMessageBox
    events = []
    i = 0
    while i == 0:
        count = int(simpledialog.askstring("Number of Events", "How many events would you like to create?", parent=main))
            if count == 0 :
                tkMessageBox.showinfo(title="Error", message="Enter a number larger than 0!")

    for i in range(count):
        events.append([simpledialog.askstring("Input", "New Task", parent= main)])

    return [events]