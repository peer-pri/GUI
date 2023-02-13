from tkinter import *
import tkinter as tk
import customtkinter
from PIL import Image,ImageTk
import datetime
from pathlib import Path
import subprocess
import os
import sys
import platform






customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title("Application of Management")
root.geometry("1200x800")

BASEPATH = Path(__file__).parent



txt_label = tk.Label(root, font=("Arial", 20, 'bold'), foreground="white", background="DarkBlue", borderwidth=3, relief="ridge") 
txt_label.pack()  
txt_label.place(x=100, y=35)  
txt_label.config(text="Application List")


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



add_security_image = ImageTk.PhotoImage(Image.open("images/security.png").resize((30,30), Image.ANTIALIAS))
add_gallery_image = ImageTk.PhotoImage(Image.open("images/gallery.png").resize((30,30), Image.ANTIALIAS))
add_source_image = ImageTk.PhotoImage(Image.open("images/source.png").resize((30,30), Image.ANTIALIAS))
add_project_image = ImageTk.PhotoImage(Image.open("images/project.png").resize((30,30), Image.ANTIALIAS))
add_notes_image = ImageTk.PhotoImage(Image.open("images/notes.png").resize((30,30), Image.ANTIALIAS))
add_timetable_image = ImageTk.PhotoImage(Image.open("images/timetable.png").resize((30,30), Image.ANTIALIAS))
add_controlsystem_image = ImageTk.PhotoImage(Image.open("images/controlsystem.png").resize((30,30), Image.ANTIALIAS))
add_workbench_image = ImageTk.PhotoImage(Image.open("images/workbench.png").resize((30,30), Image.ANTIALIAS))





def start_programm1():
    import programm.security as security
    subprocess.run([BASEPATH / "programm/security.py"])

    


def start_programm2():
    import gallery
    subprocess.run([BASEPATH / "programm/gallery.py"])

def start_programm3():
    import source
    subprocess.run([BASEPATH / "programm/source.py"])

def start_programm4():
    import project
    subprocess.run([BASEPATH / "programm/project.py"])

def start_programm5():
    import notes
    subprocess.run([BASEPATH / "programm/notes.py"])

def start_programm6():
    import timetable
    subprocess.run([BASEPATH / "programm/timetable.py"])

def start_programm7():
    import controlsystem
    subprocess.run([BASEPATH / "programm/controlsystem.py"])

def start_programm8():
    import workbench
    subprocess.run([BASEPATH / "programm/workbench.py"])




button_1 = customtkinter.CTkButton(master=root, image=add_security_image, text="Open Security", width=220, height=60, compound="left", command=start_programm1)
button_1.place(x=490, y=120)

button_2 = customtkinter.CTkButton(master=root, image=add_gallery_image, text="Open Gallery", width=220, height=60, compound="left", command=start_programm2)
button_2.place(x=680, y=240)

button_3 = customtkinter.CTkButton(master=root, image=add_source_image, text="Open Source", width=220, height=60, compound="left", command=start_programm3)
button_3.place(x=820, y=360)

button_4 = customtkinter.CTkButton(master=root, image=add_project_image, text="Open Projects", width=220, height=60, compound="left", command=start_programm4)
button_4.place(x=680, y=480)

button_5 = customtkinter.CTkButton(master=root, image=add_notes_image, text="Open Notes", width=220, height=60, compound="left", command=start_programm5)
button_5.place(x=500, y=600)

button_6 = customtkinter.CTkButton(master=root, image=add_timetable_image, text="Open Timetable", width=220, height=60, compound="left", command=start_programm6)
button_6.place(x=320, y=480)

button_7 = customtkinter.CTkButton(master=root, image=add_controlsystem_image, text="Open Control System", width=220, height=60, compound="left", command=start_programm7)
button_7.place(x=180, y=360)

button_8 = customtkinter.CTkButton(master=root, image=add_workbench_image, text="Open Workbench", width=220, height=60, compound="left", command=start_programm8)
button_8.place(x=300, y=240)

root.mainloop()