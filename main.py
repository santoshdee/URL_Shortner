from tkinter import *
from PIL import Image
from PIL import ImageTk
import clipboard
import validators
from pyshorteners import Shortener

def Clear():
    e.delete(0, "end")
    l.config(text="")

def Copy():
    clipboard.copy(l.cget("text"))
    c = Label(win, text="Copied", font=(20))  # new label
    c.pack()
    win.after(2000, c.destroy)  # msg displayed will be destroyed after 2000msec

def Paste():
    e.delete(0, "end")
    e.insert(0, clipboard.paste())


def Shorten():
    link = e.get()
    valid = validators.url("https://" + link)  # checks whether the input link is valid or not
    if valid == True:
        short = Shortener().tinyurl.short(link)
        l.config(text=short)
    else:
        l.config(text="Invalid address")


# creating a window
win = Tk()
# title for the window
win.title("URL Shortener")
# specifying the geometry as per the needs
win.geometry("700x200")   # width x height

# creating widgets inside the window
# required boxes or widgets --> input box, output box,
# 4 buttons --> paste button, copy button, shorten button, clear button

# Input box
e = Entry(win, font=(20))
e.place(relwidth=.6, relx=.2, rely=.2)

# Working on paste image
paste = Image.open("paste.png")
resized_paste = paste.resize((20,20))
new_paste = ImageTk.PhotoImage(resized_paste)

# Paste button
paste_button = Button(win, image=new_paste, command=Paste)
paste_button.place(relx=.16, rely=.2)

# Shorten button
short_button = Button(win, text="Shorten", command=Shorten)
short_button.place(relx=.4, rely=.35)

# Clear button
# Command tells the functionality of the clear button (tells what the clear button has to do)
clear_button = Button(win, text="Clear", command=Clear)
clear_button.place(relx=.5, rely=.35)

# Output box
l = Label(win, bg="White", font=(20), relief="sunken")
l.place(relwidth=.6, relx=.2, rely=.55)

# Working on copy image
copy = Image.open("copy.png")
resized_copy = copy.resize((20,20))
new_copy = ImageTk.PhotoImage(resized_copy)

# Copy button
copy_button = Button(win, image=new_copy, command=Copy)
copy_button.place(relx=.16, rely=.55)

win.mainloop()
