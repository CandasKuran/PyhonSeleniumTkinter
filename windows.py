from msilib.schema import BBControl
from tkinter import *
import tkinter as tk
from turtle import color, width



window = tk.Tk()
window.geometry('400x400')
window.resizable(False, False)
window.title("Resauax social")


twitter_button = tk.Button(
    window,
    # command=(exemple.logintwitter),
    width=20,
    height=3,
    fg=("white"),
    bg=("blue"),
    font=(""),
    text="twitter",
)
twitter_button.pack()

instagram_button = tk.Button(
    window,
    width=20,
    height=3,
    text="instagram",
    
)




instagram_button.pack()





window.mainloop()