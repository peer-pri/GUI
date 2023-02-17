import os
from time import sleep 
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter import filedialog


def key_delete():
    root = Tk()

    # This is the section of code which creates the main window
    root.geometry('389x114')
    root.configure(background='#F0F8FF')
    root.title('key devalued')


    # This is the section of code which creates the a label
    Label(root, text='The key for your file is devalued.', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=76, y=27)


    # This is the section of code which creates the a label
    Label(root, text='You can delete the key now!', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=98, y=63)


    root.mainloop()

def encrypt_done():
    root = Tk()

    # This is the section of code which creates the main window
    root.configure(background='#F0F8FF')
    root.title('encrypted')


    # This is the section of code which creates the a label
    Label(root, text='The selected file is encrypted!', bg='#F0F8FF', font=('arial', 12, 'normal')).pack()


    # This is the section of code which creates the a label
    Label(root, text='The key to decrypt the file is there, where the encrypted file is.', bg='#F0F8FF', font=('arial', 12, 'normal')).pack()


    root.mainloop()

def encrypt(): # Your file will be encrypted
    file = filedialog.askopenfilename(title='Select a file')
    have_to_encrypt = open(file, "rb").read()
    size = len(have_to_encrypt)

    progessBar['value'] = 20
    root.update_idletasks()

    key = os.urandom(size)

    progessBar['value'] = 40
    root.update_idletasks()

    with open(f'{file}.key', "wb") as key_out:
        key_out.write(key)
    progessBar['value'] = 60
    root.update_idletasks()

    encrypted = bytes(a ^ b for (a, b) in zip(have_to_encrypt, key))

    progessBar['value'] = 80
    root.update_idletasks()

    with open(file, "wb") as encrypted_out:
        encrypted_out.write(encrypted)

    progessBar['value'] = 100
    root.update_idletasks()

    encrypt_done()


def decrypt(): # Your file will be decryptet
    filename = filedialog.askopenfilename(title='Select the encrypted file')
    key = filedialog.askopenfilename(title='Select the key for the encrypeted file')
    file = open(filename, "rb").read()

    progessBar['value'] = 30
    root.update_idletasks()

    key = open(key, "rb").read()
    decrypted = bytes(a ^ b for (a, b) in zip(file, key))

    progessBar['value'] = 60
    root.update_idletasks()

    with open(filename, "wb") as decrypted_out:
        decrypted_out.write(decrypted)
    
    progessBar['value'] = 100
    root.update_idletasks()

    # call the done/key delete window
    key_delete()
    



# This is a function which increases the progress bar value by the given increment amount
def makeProgress():
	progessBar['value']=progessBar['value'] + 1
	root.update_idletasks()



root = Tk()

# This is the section of code which creates the main window
root.geometry('297x119')
root.configure(background='#F0F8FF')
root.title('SafeFiler')


# This is the section of code which creates a button
Button(root, text='Encrypt', bg='#F0F8FF', font=('arial', 12, 'normal'), command=encrypt).place(x=22, y=26)


# This is the section of code which creates a button
Button(root, text='Decrypt', bg='#F0F8FF', font=('arial', 12, 'normal'), command=decrypt).place(x=121, y=26)


# This is the section of code which creates a color style to be used with the progress bar
progessBar_style = ttk.Style()
progessBar_style.theme_use('clam')
progessBar_style.configure('progessBar.Horizontal.TProgressbar', foreground='#F0F8FF', background='#F0F8FF')


# This is the section of code which creates a progress bar
progessBar=ttk.Progressbar(root, style='progessBar.Horizontal.TProgressbar', orient='horizontal', length=252, mode='determinate', maximum=100, value=1)
progessBar.place(x=21, y=82)


root.mainloop()
