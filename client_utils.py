from connect import connect_to_database
from tkinter import messagebox


def add_client_to_database(
    id_client_entry,
    nume_client_entry,
    prenume_client_entry,
    cnp_client_entry,
    telefon_client_entry,
):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        id_client_str = id_client_entry.get()
        nume_client = nume_client_entry.get()
        prenume_client = prenume_client_entry.get()
        cnp_client = cnp_client_entry.get()
        telefon_client = telefon_client_entry.get()

        try:
            id_client = int(id_client_str)
        except ValueError:
            messagebox.showerror("Error", "ID_client must be a valid integer")
            return

        insert_query = "INSERT INTO clienti (ID_client, nume, prenume, cnp, numar_telefon) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(
            insert_query,
            (id_client, nume_client, prenume_client, cnp_client, telefon_client),
        )

        connection.commit()

        cursor.close()
        connection.close()

        messagebox.showinfo("Success", "Client adaugat!")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")


def remove_client_from_database(id_client_delete_entry):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        id_client_str = id_client_delete_entry.get()

        try:
            id_client = int(id_client_str)
        except ValueError:
            messagebox.showerror("Error", "ID_client must be a valid integer")
            return

        delete_query = "DELETE FROM clienti WHERE ID_client = %s"
        cursor.execute(delete_query, (id_client,))

        connection.commit()

        cursor.close()
        connection.close()

        messagebox.showinfo("Success", "Client sters!")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")


def update_client_to_database(
    id_client_entry_update,
    nume_client_entry_update,
    prenume_client_entry_update,
    cnp_client_entry_update,
    telefon_client_entry_update,
):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        id_client_str = id_client_entry_update.get()
        nume_client = nume_client_entry_update.get()
        prenume_client = prenume_client_entry_update.get()
        cnp_client = cnp_client_entry_update.get()
        telefon_client = telefon_client_entry_update.get()

        try:
            id_client = int(id_client_str)
        except ValueError:
            messagebox.showerror("Error", "ID_client must be a valid integer")
            return

        update_query = "UPDATE clienti SET nume = %s, prenume = %s, cnp = %s, numar_telefon = %s WHERE ID_client = %s"
        cursor.execute(
            update_query,
            (nume_client, prenume_client, cnp_client, telefon_client, id_client),
        )

        connection.commit()

        cursor.close()
        connection.close()

        messagebox.showinfo("Success", "Client modificat!")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")


def view_client_from_database(tree):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        select_query = "SELECT * FROM clienti"
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
