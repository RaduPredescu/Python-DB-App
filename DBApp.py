import tkinter as tk
from tkinter import Label, Entry, Button,Listbox
from client_utils import add_client_to_database, remove_client_from_database,update_client_to_database,view_client_from_database
from tkinter import ttk
from magazin_utils import add_magazin_to_database,remove_magazin_from_database,update_magazin_to_database

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

def view_client():
    view_client_from_database(tree)

def remove_magazin():
    remove_magazin_from_database(id_magazin_delete_entry)

def add_magazin():
    add_magazin_to_database(id_magazin_entry,nume_magazin_entry,locatie_magazin_entry,tip_magazin_entry)

def update_magazin():
    update_magazin_to_database(id_magazin_entry_update,nume_magazin_entry_update,locatie_magazin_entry_update,tip_magazin_entry_update)

#adaugare client
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


add_button_client = Button(root, text="Add Client to Database", command=add_client)
add_button_client.grid(row=5, column=1)


#stergere client
Label(root, text="ID_client to Remove:").grid(row=6, column=0)
id_client_delete_entry = Entry(root)
id_client_delete_entry.grid(row=6, column=1)

remove_button_client = Button(root, text="Remove Client from Database", command=remove_client)
remove_button_client.grid(row=7, column=1)


#update client
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

update_button_client = Button(root, text="Update Client", command=update_client)
update_button_client.grid(row=5, column=3)


#vizualizare client
view_button_client = Button(root, text="View Client", command=view_client)
view_button_client.grid(row=7, column=3)

tree = ttk.Treeview(root, columns=("ID_client", "Nume", "Prenume", "CNP", "Telefon"), show="headings", height=5)
tree.grid(row=10, column=0, columnspan=5)

tree.heading("ID_client", text="ID_client")
tree.heading("Nume", text="Nume")
tree.heading("Prenume", text="Prenume")
tree.heading("CNP", text="CNP")
tree.heading("Telefon", text="Telefon")



#adaugare magazin
Label(root,text="ID_magazin: ").grid(row=11,column=0)
id_magazin_entry = Entry(root)
id_magazin_entry.grid(row=11,column=1)

Label(root,text="Nume magazin: ").grid(row=12,column=0)
nume_magazin_entry = Entry(root)
nume_magazin_entry.grid(row=12,column=1)

Label(root,text="Locatie: ").grid(row=13,column=0)
locatie_magazin_entry = Entry(root)
locatie_magazin_entry.grid(row=13,column=1)

Label(root,text="Tip produse: ").grid(row=14,column=0)
tip_magazin_entry = Entry(root)
tip_magazin_entry.grid(row=14,column=1)

add_button_magazin= Button(root, text="Add Magazin to Database", command=add_magazin)
add_button_magazin.grid(row=15, column=1)


#stergere magazin
Label(root,text="ID_magazin to Remove: ").grid(row=16,column=0)
id_magazin_delete_entry = Entry(root)
id_magazin_delete_entry.grid(row=16,column=1)

remove_button_magazin = Button(root,text="Remove Magazin from Database",command=remove_magazin)
remove_button_magazin.grid(row=17,column=1)


#update magazin
Label(root,text="ID_magazin to update: ").grid(row=11,column=2)
id_magazin_entry_update = Entry(root)
id_magazin_entry_update.grid(row=11,column=3)

Label(root,text="Nume magazin to update: ").grid(row=12,column=2)
nume_magazin_entry_update = Entry(root)
nume_magazin_entry_update.grid(row=12,column=3)

Label(root,text="Locatie to update: ").grid(row=13,column=2)
locatie_magazin_entry_update = Entry(root)
locatie_magazin_entry_update.grid(row=13,column=3)

Label(root,text="Tip produse to update: ").grid(row=14,column=2)
tip_magazin_entry_update = Entry(root)
tip_magazin_entry_update.grid(row=14,column=3)

update_button_magazin = Button(root, text="Update Magazin to Database", command=update_magazin)
update_button_magazin.grid(row=15, column=3)


root.mainloop()
