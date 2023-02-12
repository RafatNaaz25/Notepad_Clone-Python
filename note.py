import tkinter as tk
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file:
        text = text_widget.get(1.0, tk.END)
        file.write(text)
        file.close()

def open_file():
    file = filedialog.askopenfile(mode='r', defaultextension=".txt")
    if file:
        text = file.read()
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.INSERT, text)
        file.close()

app = tk.Tk()
app.title("Notepad")

text_widget = tk.Text(app)
text_widget.pack()

save_button = tk.Button(app, text="Save", command=save_file)
save_button.pack()

open_button = tk.Button(app, text="Open", command=open_file)
open_button.pack()

app.mainloop()
