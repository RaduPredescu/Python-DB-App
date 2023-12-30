import tkinter as tk
from tkinter import Label, Entry, Button
from client_utils import add_client_to_database, remove_client_from_database,update_client_to_database

root = tk.Tk()
root.title("Database App")


def remove_client():
    remove_client_from_database(id_client_delete_entry)


def add_client():
    add_client_to_database(
        id_client_entry,
        nume_client_entry,
        prenume_client_entry,
        cnp_client_entry,
        telefon_client_entry,
    )


def update_client():
    update_client_to_database(
        id_client_entry_update,
        nume_client_entry_update,
        prenume_client_entry_update,
        cnp_client_entry_update,
        telefon_client_entry_update,
    )


Label(root, text="ID_client:").grid(row=0, column=0)
id_client_entry = Entry(root)
id_client_entry.grid(row=0, column=1)

Label(root, text="Nume:").grid(row=1, column=0)
nume_client_entry = Entry(root)
nume_client_entry.grid(row=1, column=1)

Label(root, text="Prenume:").grid(row=2, column=0)
prenume_client_entry = Entry(root)
prenume_client_entry.grid(row=2, column=1)

Label(root, text="CNP:").grid(row=3, column=0)
cnp_client_entry = Entry(root)
cnp_client_entry.grid(row=3, column=1)

Label(root, text="Telefon:").grid(row=4, column=0)
telefon_client_entry = Entry(root)
telefon_client_entry.grid(row=4, column=1)


add_button = Button(root, text="Add Client to Database", command=add_client)
add_button.grid(row=5, column=1)


Label(root, text="ID_client to Remove:").grid(row=6, column=0)
id_client_delete_entry = Entry(root)
id_client_delete_entry.grid(row=6, column=1)

remove_button = Button(root, text="Remove Client from Database", command=remove_client)
remove_button.grid(row=7, column=1)

Label(root, text="ID_client to update: ").grid(row=0, column=2)
id_client_entry_update = Entry(root)
id_client_entry_update.grid(row=0, column=3)

Label(root, text="Nume to update: ").grid(row=1, column=2)
nume_client_entry_update = Entry(root)
nume_client_entry_update.grid(row=1, column=3)

Label(root, text="Prenume to update: ").grid(row=2, column=2)
prenume_client_entry_update = Entry(root)
prenume_client_entry_update.grid(row=2, column=3)

Label(root, text="CNP to update: ").grid(row=3, column=2)
cnp_client_entry_update = Entry(root)
cnp_client_entry_update.grid(row=3, column=3)

Label(root, text="Telefon to update: ").grid(row=4, column=2)
telefon_client_entry_update = Entry(root)
telefon_client_entry_update.grid(row=4, column=3)

add_button = Button(root, text="Update client", command=update_client)
add_button.grid(row=5, column=3)

root.mainloop()
