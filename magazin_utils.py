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


def remove_magazin_from_database(id_magazin_delete_entry):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        id_magazin_str = id_magazin_delete_entry.get()

        try:
            id_magazin = int(id_magazin_str)
        except ValueError:
            messagebox.showerror("Error", "ID_magazin must be a valid integer")
            return

        delete_query = "DELETE FROM magazine WHERE ID_magazin = %s"
        cursor.execute(delete_query, (id_magazin,))

        connection.commit()
        cursor.close()
        connection.close()

        print("Client removed from the database")
        messagebox.showinfo("Success", "Client removed from the database")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")


def update_magazin_to_database(
    id_magazin_entry_update,
    nume_magazin_entry_update,
    locatie_magazin_entry_update,
    tip_magazin_entry_update,
):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        id_magazin_str = id_magazin_entry_update.get()
        nume_magazin = nume_magazin_entry_update.get()
        locatie_magazin = locatie_magazin_entry_update.get()
        tip_magazin = tip_magazin_entry_update.get()

        try:
            id_magazin = int(id_magazin_str)
        except ValueError:
            messagebox.showerror("Error", "ID_client must be a valid integer")
            return

        update_query = "UPDATE magazine SET nume_magazin = %s, locatie = %s, tip_produse = %s WHERE ID_magazin = %s"
        cursor.execute(
            update_query,
            (nume_magazin, locatie_magazin, tip_magazin, id_magazin),
        )

        connection.commit()

        cursor.close()
        connection.close()

        print("Magazin modified from database")
        messagebox.showinfo("Success", "Magazin modified from database")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")


def view_magazin_from_database(tree):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        select_query = "SELECT * FROM magazine"
        cursor.execute(select_query)

        rows = cursor.fetchall()

        for item in tree.get_children():
            tree.delete(item)

        for row in rows:
            tree.insert("", "end", values=row)

        cursor.close()
        connection.close()

    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")
