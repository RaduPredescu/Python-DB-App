from connect import connect_to_database
from tkinter import messagebox


def add_tranzactie_to_database(
    id_tranzactie_entry,
    id_client_tranzactie_entry,
    id_magazin_tranzactie_entry,
    suma_tranzactie_entry,
    data_tranzactie_entry,
):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        id_tranzactie_str = id_tranzactie_entry.get()
        id_client_str = id_client_tranzactie_entry.get()
        id_magazin_str = id_magazin_tranzactie_entry.get()
        suma_tranzactie = suma_tranzactie_entry.get()
        data_tranzactie = data_tranzactie_entry.get()

        try:
            id_tranzactie = int(id_tranzactie_str)
        except ValueError:
            messagebox.showerror("Error", "ID tranzactie trebuie sa fie numar intreg")
            return

        try:
            id_client = int(id_client_str)
        except ValueError:
            messagebox.showerror("Error", "ID client trebuie sa fie numar intreg")
            return

        try:
            id_magazin = int(id_magazin_str)
        except ValueError:
            messagebox.showerror("Error", "ID magazin trebuie sa fie numar intreg")
            return

        insert_query = "INSERT INTO tranzactii (ID_tranzactie, ID_client, ID_magazin, suma_tranzactie, data_tranzactie) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(
            insert_query,
            (id_tranzactie, id_client, id_magazin, suma_tranzactie, data_tranzactie),
        )

        connection.commit()

        cursor.close()
        connection.close()

        messagebox.showinfo("Success", "Tranzactie adaugata!")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")


def remove_tranzactie_from_database(id_tranzactie_delete_entry):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        id_tranzactie_str = id_tranzactie_delete_entry.get()

        try:
            id_tranzactie = int(id_tranzactie_str)
        except ValueError:
            messagebox.showerror("Error", "ID magazin trebuie sa fie numar intreg")
            return

        delete_query = "DELETE FROM tranzactii WHERE ID_tranzactie = %s"
        cursor.execute(delete_query, (id_tranzactie,))

        connection.commit()
        cursor.close()
        connection.close()

        messagebox.showinfo("Success", "Tranzactie stearsa!")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")


def update_tranzactie_to_database(
    id_tranzactie_entry_update,
    id_client_tranzactie_entry_update,
    id_magazin_entry_update,
    suma_tranzactie_entry_update,
    data_tranzactie_entry_update,
):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        id_tranzactie_str = id_tranzactie_entry_update.get()
        id_client_str = id_client_tranzactie_entry_update.get()
        id_magazin_str = id_magazin_entry_update.get()
        suma_tranzactie = suma_tranzactie_entry_update.get()
        data_tranzactie = data_tranzactie_entry_update.get()

        try:
            id_tranzactie = int(id_tranzactie_str)
        except ValueError:
            messagebox.showerror("Error", "ID tranzactie trebuie sa fie numar intreg")
            return

        try:
            id_magazin = int(id_magazin_str)
        except ValueError:
            messagebox.showerror("Error", "ID magazin trebuie sa fie numar intreg")
            return

        try:
            id_client = int(id_client_str)
        except ValueError:
            messagebox.showerror("Error", "ID client trebuie sa fie numar intreg")
            return

        update_query = "UPDATE tranzactii SET ID_client = %s, ID_magazin = %s, suma_tranzactie = %s, data_tranzactie = %s WHERE ID_tranzactie = %s"
        cursor.execute(
            update_query,
            (id_client, id_magazin, suma_tranzactie, data_tranzactie, id_tranzactie),
        )

        connection.commit()

        cursor.close()
        connection.close()

        messagebox.showinfo("Success", "Tranzactie modificata!")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")


def view_tranzactii_from_database(tree):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        select_query = "SELECT * FROM tranzactii"
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
