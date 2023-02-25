from tkinter import simpledialog

# Create Popup

def popup(text):
    answer = simpledialog.askstring("input string", text)
    return answer