from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital Clock")


def time():
    time_nums = strftime("%H:%M:%S %p")
    label.config(text=time_nums)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 80),
              background="black",
              foreground="cyan",)

label.pack(anchor="center")
time()

mainloop()


