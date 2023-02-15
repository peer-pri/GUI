import os
from time import sleep
from subprocess import call
import tkinter


def encrypt(file): # Your file will be encryptet
    have_to_encrypt = open(file, "rb").read()
    size = len(have_to_encrypt)
    key = os.urandom(size)
    with open(f'{file}.key', "wb") as key_out:
        key_out.write(key)
    encryptet = bytes(a ^ b for (a, b) in zip(have_to_encrypt, key))
    with open(file, "wb") as encryptet_out:
        encryptet_out.write(encryptet)
    print('The selected file is encryptet! The key to decrypt the file is there, where the encryptet file is.')
    sleep(3)

def decrypt(filename, key): # Your file will be decryptet
    file = open(filename, "rb").read()
    key = open(key, "rb").read()
    decrypted = bytes(a ^ b for (a, b) in zip(file, key))
    with open(filename, "wb") as decrypted_out:
        decrypted_out.write(decrypted)
    sleep(1)
    print('')
    print('The key for your file is devalued, you can delet the key now!')
    print('')
    sleep(2)
    startq = input('Do you want to go to the startpage? (y/n): ')
    if startq == 'y':
        freshConsole()
        call(['python', 'safefiler.py'])
    if startq == 'n':
        print('')
        print('Bye!')
        sleep(1)

# the Def for the other files to clear the console
def freshConsole():
    clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clear()

def aboutq():
    freshConsole()
    print("""

This Program stays under the MIT Licens!


Created by zlELo

Developer on GitHub: github.com/zlElo
Developer Homepage: zlelo.github.io

    """)

    back_quest = input('Do you want to go back to the Startpage? (y/n): ')

    if back_quest == 'y':
        freshConsole()
        call(['python', 'safefiler.py'])
    elif back_quest == 'n':
        print('Have a nice day, Bye!')
        sleep(0.5)
        quit()

# The startpage
print("""
                       _____       ____     _______ __         
                      / ___/____ _/ __/__  / ____(_) /__  _____
                      \__ \/ __ `/ /_/ _ \/ /_  / / / _ \/ ___/
                     ___/ / /_/ / __/  __/ __/ / / /  __/ /    
                    /____/\__,_/_/  \___/_/   /_/_/\___/_/     
                    by zlElo

Welcome to SafeFiler, your program to encrypt and decrypt important files
secure and fast!


You have this functions:

- encrypt, encrypt files with a very high security (command: encrypt)
- decrypt, decrypt the encrpyted file with the generated key (command: decrypt)

More:

- About (command: about)
- Close the program (command: bye)

""")


# start of name process
file_size = os.path.getsize('name.txt')
if file_size == 0:
    entered_name = input('Hey, you are new here. Pleas enter your Name: ')
    file1 = open("name.txt", "w") 
    file1.write(entered_name)
    file1.close()

f = open('name.txt', 'r')
contents = f.read()
name = contents
# End of name process


start = input(f'Hello {name}, what do you want to do?: ')
if start == 'encrypt':
    file = input('Pleas Enter the Path to the file: ')
    encrypt(file)
if start == 'decrypt':
    filename = input('Pleas Enter the Path to the file: ')
    key = input('Pleas Enter the Path of the key for the file: ')
    decrypt(filename, key)
if start == 'about':
    aboutq()
if start == 'bye':
    print('Bye!')
    quit()
