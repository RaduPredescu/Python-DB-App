import tkinter as tk
from tkinter import Label, Entry, Button
from client_utils import add_client_to_database, remove_client_from_database

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


# Create and place labels, entry field, and button for removing
Label(root, text="ID_client to Remove:").grid(row=6, column=0)
id_client_delete_entry = Entry(root)
id_client_delete_entry.grid(row=6, column=1)

remove_button = Button(root, text="Remove Client from Database", command=remove_client)
remove_button.grid(row=7, column=1)

# # Start the main loop
root.mainloop()
