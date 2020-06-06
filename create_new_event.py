def create():
    events = []
    i = 0
    choice = "Y"
    count = int(simpledialog.askstring("Number of Events", "How many events would you like to create?", parent=main))
    for i in range(count):
        events.append([simpledialog.askstring("Input", "New Task", parent= main)])
    print(events)