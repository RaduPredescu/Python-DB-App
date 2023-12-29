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

        print("Client added to the database")
        messagebox.showinfo("Success", "Client added to the database")

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

        print("Client removed from the database")
        messagebox.showinfo("Success", "Client removed from the database")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")
