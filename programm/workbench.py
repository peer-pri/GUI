from tkinter import *
import tkinter as tk
import customtkinter
from PIL import Image,ImageTk
import datetime
from pathlib import Path
import subprocess



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title("Application of Management")
root.geometry("1200x800")


txt_label = tk.Label(root, font=("Arial", 20, 'bold'), foreground="white", background="DarkBlue", borderwidth=3, relief="ridge") 
txt_label.pack()  
txt_label.place(x=100, y=35)  
txt_label.config(text="Application Workbench")


def update_datetime(clock_label, date_label):
    now = datetime.datetime.now()
    clock_label['text'] = f"{now:%H:%M:%S}"
    date_label['text'] = f"{now:%d/%m/%Y}"
    clock_label.after(200, update_datetime, clock_label, date_label)


clock_label = tk.Label(root, font=("Arial", 20, 'bold'), borderwidth=3, relief="ridge")
clock_label.pack()
clock_label.place(x=984, y= 45)
date_label = tk.Label(root, font=("Arial", 20, 'bold'), borderwidth=3, relief="ridge")
date_label.pack()
date_label.place(x=950, y=5)
update_datetime(clock_label, date_label)



root.mainloop()