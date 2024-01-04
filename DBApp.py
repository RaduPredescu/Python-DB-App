import tkinter as tk
from tkinter import Label, Entry, Button
from client_utils import (
    add_client_to_database,
    remove_client_from_database,
    update_client_to_database,
    view_client_from_database,
)
from tkinter import ttk
from magazin_utils import (
    add_magazin_to_database,
    remove_magazin_from_database,
    update_magazin_to_database,
    view_magazin_from_database,
)
from tranzactie_utils import (
    add_tranzactie_to_database,
    remove_tranzactie_from_database,
    update_tranzactie_to_database,
    view_tranzactii_from_database,
)

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
    view_client_from_database(tree_client)


def remove_magazin():
    remove_magazin_from_database(id_magazin_delete_entry)


def add_magazin():
    add_magazin_to_database(
        id_magazin_entry, nume_magazin_entry, locatie_magazin_entry, tip_magazin_entry
    )


def update_magazin():
    update_magazin_to_database(
        id_magazin_entry_update,
        nume_magazin_entry_update,
        locatie_magazin_entry_update,
        tip_magazin_entry_update,
    )


def view_magazin():
    view_magazin_from_database(tree_magazin)


def remove_tranzactie():
    remove_tranzactie_from_database(id_tranzactie_delete_entry)


def add_tranzactie():
    add_tranzactie_to_database(
        id_tranzactie_entry,
        id_client_tranzactie_entry,
        id_magazin_tranzactie_entry,
        suma_tranzactie_entry,
        data_tranzactie_entry,
    )


def update_tranzactie():
    update_tranzactie_to_database(
        id_tranzactie_entry_update,
        id_client_tranzactie_entry_update,
        id_magazin_tranzactie_entry_update,
        suma_tranzactie_entry_update,
        data_tranzactie_entry_update,
    )


def view_tranzactii():
    view_tranzactii_from_database(tree_tranzactie)


# adaugare client
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


add_button_client = Button(
    root, text="Adaugare client in baza de date", command=add_client
)
add_button_client.grid(row=5, column=1)


# stergere client
Label(root, text="ID_client de sters:").grid(row=6, column=0)
id_client_delete_entry = Entry(root)
id_client_delete_entry.grid(row=6, column=1)

remove_button_client = Button(
    root, text="Sterge client din baza de date", command=remove_client
)
remove_button_client.grid(row=7, column=1)


# update client
Label(root, text="ID_client de inlocuit: ").grid(row=0, column=2)
id_client_entry_update = Entry(root)
id_client_entry_update.grid(row=0, column=3)

Label(root, text="Nume de inlocuit: ").grid(row=1, column=2)
nume_client_entry_update = Entry(root)
nume_client_entry_update.grid(row=1, column=3)

Label(root, text="Prenume de inlocuit: ").grid(row=2, column=2)
prenume_client_entry_update = Entry(root)
prenume_client_entry_update.grid(row=2, column=3)

Label(root, text="CNP de inlocuit: ").grid(row=3, column=2)
cnp_client_entry_update = Entry(root)
cnp_client_entry_update.grid(row=3, column=3)

Label(root, text="Telefon de inlocuit: ").grid(row=4, column=2)
telefon_client_entry_update = Entry(root)
telefon_client_entry_update.grid(row=4, column=3)

update_button_client = Button(
    root, text="Inlocuieste client in baza de date", command=update_client
)
update_button_client.grid(row=5, column=3)


# vizualizare client
view_button_client = Button(root, text="Vezi Clienti", command=view_client)
view_button_client.grid(row=7, column=3)

tree_client = ttk.Treeview(
    root,
    columns=("ID_client", "Nume", "Prenume", "CNP", "Telefon"),
    show="headings",
    height=3,
)
view_client_from_database(tree_client)

tree_client.grid(row=10, column=0, columnspan=5)

tree_client.heading("ID_client", text="ID_client")
tree_client.heading("Nume", text="Nume")
tree_client.heading("Prenume", text="Prenume")
tree_client.heading("CNP", text="CNP")
tree_client.heading("Telefon", text="Telefon")


# adaugare magazin
Label(root, text="ID_magazin: ").grid(row=11, column=0)
id_magazin_entry = Entry(root)
id_magazin_entry.grid(row=11, column=1)

Label(root, text="Nume magazin: ").grid(row=12, column=0)
nume_magazin_entry = Entry(root)
nume_magazin_entry.grid(row=12, column=1)

Label(root, text="Locatie: ").grid(row=13, column=0)
locatie_magazin_entry = Entry(root)
locatie_magazin_entry.grid(row=13, column=1)

Label(root, text="Tip produse: ").grid(row=14, column=0)
tip_magazin_entry = Entry(root)
tip_magazin_entry.grid(row=14, column=1)

add_button_magazin = Button(
    root, text="Adaugare magazin in baza de date", command=add_magazin
)
add_button_magazin.grid(row=15, column=1)


# stergere magazin
Label(root, text="ID_magazin de sters: ").grid(row=16, column=0)
id_magazin_delete_entry = Entry(root)
id_magazin_delete_entry.grid(row=16, column=1)

remove_button_magazin = Button(
    root, text="Sterge magazin din baza de date", command=remove_magazin
)
remove_button_magazin.grid(row=17, column=1)


# update magazin
Label(root, text="ID_magazin de inlocuit: ").grid(row=11, column=2)
id_magazin_entry_update = Entry(root)
id_magazin_entry_update.grid(row=11, column=3)

Label(root, text="Nume magazin de inlocuit: ").grid(row=12, column=2)
nume_magazin_entry_update = Entry(root)
nume_magazin_entry_update.grid(row=12, column=3)

Label(root, text="Locatie de inlocuit: ").grid(row=13, column=2)
locatie_magazin_entry_update = Entry(root)
locatie_magazin_entry_update.grid(row=13, column=3)

Label(root, text="Tip produse de inlocuit: ").grid(row=14, column=2)
tip_magazin_entry_update = Entry(root)
tip_magazin_entry_update.grid(row=14, column=3)

update_button_magazin = Button(
    root, text="Inlocuieste magazin in baza de date", command=update_magazin
)
update_button_magazin.grid(row=15, column=3)


# vizualizare magazin
view_button_magazin = Button(root, text="Vezi Magazine", command=view_magazin)
view_button_magazin.grid(row=17, column=3)

tree_magazin = ttk.Treeview(
    root,
    columns=("ID_magazin", "Nume magazin", "Locatie magazin", "Tip magazin"),
    show="headings",
    height=3,
)
view_magazin_from_database(tree_magazin)
tree_magazin.grid(row=18, column=0, columnspan=5)

tree_magazin.heading("ID_magazin", text="ID_magazin")
tree_magazin.heading("Nume magazin", text="Nume magazin")
tree_magazin.heading("Locatie magazin", text="Locatie magazin")
tree_magazin.heading("Tip magazin", text="Tip magazin")


# adaugare tranzactie
Label(root, text="ID_tranzactie: ").grid(row=19, column=0)
id_tranzactie_entry = Entry(root)
id_tranzactie_entry.grid(row=19, column=1)

Label(root, text="ID_client pentru tranzactie: ").grid(row=20, column=0)
id_client_tranzactie_entry = Entry(root)
id_client_tranzactie_entry.grid(row=20, column=1)

Label(root, text="ID_magazin pentru tranzactie: ").grid(row=21, column=0)
id_magazin_tranzactie_entry = Entry(root)
id_magazin_tranzactie_entry.grid(row=21, column=1)

Label(root, text="Suma tranzactie: ").grid(row=22, column=0)
suma_tranzactie_entry = Entry(root)
suma_tranzactie_entry.grid(row=22, column=1)

Label(root, text="Data tranzactie: ").grid(row=23, column=0)
data_tranzactie_entry = Entry(root)
data_tranzactie_entry.grid(row=23, column=1)

add_button_tranzactie = Button(
    root, text="Adaugare tranzactie in baza de date", command=add_tranzactie
)
add_button_tranzactie.grid(row=24, column=1)


# stergere tranzactie
Label(root, text="ID_tranzactie de sters: ").grid(row=25, column=0)
id_tranzactie_delete_entry = Entry(root)
id_tranzactie_delete_entry.grid(row=25, column=1)

remove_button_tranzactie = Button(
    root, text="Sterge tranzactie din baza de date", command=remove_tranzactie
)
remove_button_tranzactie.grid(row=26, column=1)


# update tranzactie
Label(root, text="ID_tranzactie de inlocuit: ").grid(row=19, column=2)
id_tranzactie_entry_update = Entry(root)
id_tranzactie_entry_update.grid(row=19, column=3)

Label(root, text="ID_client pentru tranzactie de inlocuit: ").grid(row=20, column=2)
id_client_tranzactie_entry_update = Entry(root)
id_client_tranzactie_entry_update.grid(row=20, column=3)

Label(root, text="ID_magazin pentru tranzactie de inlocuit: ").grid(row=21, column=2)
id_magazin_tranzactie_entry_update = Entry(root)
id_magazin_tranzactie_entry_update.grid(row=21, column=3)

Label(root, text="Suma tranzactie de inlocuit: ").grid(row=22, column=2)
suma_tranzactie_entry_update = Entry(root)
suma_tranzactie_entry_update.grid(row=22, column=3)

Label(root, text="Data tranzactie de inlocuit: ").grid(row=23, column=2)
data_tranzactie_entry_update = Entry(root)
data_tranzactie_entry_update.grid(row=23, column=3)

update_button_tranzactie = Button(
    root, text="Inlocuieste tranzactie in baza de date", command=update_tranzactie
)
update_button_tranzactie.grid(row=24, column=3)


# vizualizare tranzactii
view_button_tranzactie = Button(root, text="Vezi Tranzactii", command=view_tranzactii)
view_button_tranzactie.grid(row=26, column=3)

tree_tranzactie = ttk.Treeview(
    root,
    columns=(
        "ID_tranzactie",
        "ID_client",
        "ID_magazin",
        "suma_tranzactie",
        "data_tranzactie",
    ),
    show="headings",
    height=3,
)
view_tranzactii_from_database(tree_tranzactie)
tree_tranzactie.grid(row=27, column=0, columnspan=5)

tree_tranzactie.heading("ID_tranzactie", text="ID_tranzactie")
tree_tranzactie.heading("ID_client", text="ID_client")
tree_tranzactie.heading("ID_magazin", text="ID_magazin")
tree_tranzactie.heading("suma_tranzactie", text="suma_tranzactie")
tree_tranzactie.heading("data_tranzactie", text="data_tranzactie")

Label(root, text="Copyright © 2023 Radu Predescu").grid(row=28, column=10)

root.mainloop()
