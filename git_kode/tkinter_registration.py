from pydantic import BaseModel # pip install pydantic
from pydantic import ValidationError # pip install pydantic
from pydantic import EmailStr # pip install email-validator

import os

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from tkinter.messagebox import showwarning

from tinydb import TinyDB # pip install tinydb

# Create a datafolder to store the flat-file database in.
try:
    os.mkdir('data')
except FileExistsError as e:
    print(e)
# Initialize the database.
db = TinyDB('data/tinydb.json')

class Deltager(BaseModel):
    navn: str
    antall: int
    epost: EmailStr


def write_entry(deltager: Deltager):
    db_item = {'navn': deltager.navn, 'antall': deltager.antall, 'epost': deltager.epost}
    db.insert(db_item)


# You can use this function to get a CLI-version of the registration app.
def cli_example():
    try:
        deltager_navn = input("Navn: ")
        deltager_antall = input("Antall: ")
        deltager_epost = input("E-post: ")
        deltager_a = Deltager(navn=deltager_navn, antall=deltager_antall, epost=deltager_epost)
        write_entry(deltager_a)
    except ValidationError as e:
        print(e)


# This function handle all aspect of retrieving values from the registration form, validate the fields and register them if valid.
def gui_example():
    deltager_navn = ent_navn.get()
    deltager_antall = ent_antall.get()
    deltager_epost = ent_epost.get()  
    try:
        deltager_a = Deltager(navn=deltager_navn, antall=deltager_antall, epost=deltager_epost)
        write_entry(deltager_a)
        showinfo(title="Registrert", message="Du er registrert")
        ent_navn.delete(0, tk.END)
        ent_antall.delete(0, tk.END)
        ent_epost.delete(0, tk.END)
    except ValidationError as e:
        showwarning(title="Valideringsfeil", message="%s" % e)

    
# Everything happen on a window.
window = tk.Tk()
# Almost boilerplate layoutcode.
frm_top = tk.Frame()
frm_top.grid(row=0, column=0, columnspan=2)
frm_left = tk.Frame()
frm_left.grid(row=1, column=0)
frm_right = tk.Frame()
frm_right.grid(row=1, column=1)
frm_bottom = tk.Frame()
frm_bottom.grid(row=2, column=0, columnspan=2)

lbl_greeting = tk.Label(master=frm_top, text="Registration form: Juleavslutning 5")
lbl_greeting.pack()

lbl_navn = tk.Label(master=frm_left, text="Navn: ")
ent_navn = tk.Entry(master=frm_right, width=50)
lbl_navn.pack()
ent_navn.pack()

lbl_antall = tk.Label(master=frm_left, text="Antall: ")
ent_antall = tk.Entry(master=frm_right, width=50)
lbl_antall.pack()
ent_antall.pack()

lbl_epost = tk.Label(master=frm_left, text="E-post: ")
ent_epost = tk.Entry(master=frm_right, width=50)
lbl_epost.pack()
ent_epost.pack()

btn_submit = tk.Button(master=frm_bottom, text="Submit", command=gui_example)
btn_submit.pack()

window.mainloop()