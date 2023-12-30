from connect import connect_to_database
from tkinter import messagebox

def add_magazin_to_database(
    id_magazin_entry,
    nume_magazin_entry,
    locatie_magazin_entry,
    tip_magazin_entry,
):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        id_magazin_str = id_magazin_entry.get()
        nume_magazin = nume_magazin_entry.get()
        locatie_magazin = locatie_magazin_entry.get()
        tip_magazin = tip_magazin_entry.get()

        try:
            id_magazin = int(id_magazin_str)
        except ValueError:
            messagebox.showerror("Error", "ID_magazin must be a valid integer")
            return

        insert_query = "INSERT INTO magazine (ID_magazin, nume_magazin, locatie, tip_produse) VALUES (%s, %s, %s, %s)"
        cursor.execute(
            insert_query,
            (id_magazin, nume_magazin, locatie_magazin, tip_magazin),
        )

        connection.commit()

        cursor.close()
        connection.close()

        print("Magazin added to the database")
        messagebox.showinfo("Success", "Magazin added to the database")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")
