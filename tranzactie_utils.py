from connect import connect_to_database
from tkinter import messagebox

def add_tranzactie_to_database(id_tranzactie_entry,id_client_tranzactie_entry,id_magazin_tranzactie_entry,suma_tranzactie_entry,data_tranzactie_entry):
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
            messagebox.showerror("Error", "ID_tranzactie must be a valid integer")
            return
        
        try:
            id_client = int(id_client_str)
        except ValueError:
            messagebox.showerror("Error", "ID_client must be a valid integer")
            return
        
        try:
            id_magazin = int(id_magazin_str)
        except ValueError:
            messagebox.showerror("Error", "ID_magazin must be a valid integer")
            return

        insert_query = "INSERT INTO tranzactii (ID_tranzactie, ID_client, ID_magazin, suma_tranzactie, data_tranzactie) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(
            insert_query,
            (id_tranzactie, id_client, id_magazin, suma_tranzactie, data_tranzactie),
        )

        connection.commit()

        cursor.close()
        connection.close()

        print("Tranzactie added to the database")
        messagebox.showinfo("Success", "Tranzactie added to the database")

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
            messagebox.showerror("Error", "ID_magazin must be a valid integer")
            return

        delete_query = "DELETE FROM tranzactii WHERE ID_tranzactie = %s"
        cursor.execute(delete_query, (id_tranzactie,))

        connection.commit()
        cursor.close()
        connection.close()

        print("Tranzactie removed from the database")
        messagebox.showinfo("Success", "Tranzactie removed from the database")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")