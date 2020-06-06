def create():
    import ctypes

    events = []
    i = 0
    count=0
    while count == 0:
        count = int(simpledialog.askstring("Number of Events", "How many events would you like to create?", parent=main))
        if count == 0:
            ctypes.windll.user32.MessageBoxW(0, "Enter a number larger than 0.", "Error",1)

    for i in range(count):
        events.append([simpledialog.askstring("Input", "New Task", parent=main)])
    return [events]