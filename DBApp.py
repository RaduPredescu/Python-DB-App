import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
import mysql.connector

def connect_to_database():
    # Replace 'your_username', 'your_password', and 'your_database_name' with your actual MySQL credentials
    username = 'root'
    password = 'Mercedes22012002!'
    database_name = 'proiect'

    # Connect to MySQL database
    connection = mysql.connector.connect(
        host='localhost',
        user=username,
        password=password,
        database=database_name
    )

    return connection

def add_to_database():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Get data from entry fields
        ID_client = id.get()
        nume = nume_entry.get()
        prenume = prenume_entry.get()
        cnp = cnp_entry.get()
        telefon = telefon_entry.get()

        # Execute an SQL query to insert data into the 'Clienti' table
        insert_query = "INSERT INTO Clienti (ID_client,nume, prenume, cnp, telefon) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (ID_client,nume, prenume, cnp, telefon))

        # Commit the changes to the database
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Print a message to the console
        print("Client added to the database")
        messagebox.showinfo("Success", "Client added to the database")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")

def remove_from_database():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Get data from entry field (ID_client)
        client_id = id_entry.get()

        # Execute an SQL query to delete data from the 'Clienti' table
        delete_query = "DELETE FROM Clienti WHERE ID_client = %s"
        cursor.execute(delete_query, (client_id,))

        # Commit the changes to the database
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Print a message to the console
        print("Client removed from the database")
        messagebox.showinfo("Success", "Client removed from the database")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Database App")

# Create and place labels, entry fields, and buttons for adding
Label(root, text="Nume:").grid(row=0, column=0)
Label(root, text="Prenume:").grid(row=1, column=0)
Label(root, text="CNP:").grid(row=2, column=0)
Label(root, text="Telefon:").grid(row=3, column=0)

nume_entry = Entry(root)
nume_entry.grid(row=0, column=1)
prenume_entry = Entry(root)
prenume_entry.grid(row=1, column=1)
cnp_entry = Entry(root)
cnp_entry.grid(row=2, column=1)
telefon_entry = Entry(root)
telefon_entry.grid(row=3, column=1)

add_button = Button(root, text="Add Client to Database", command=add_to_database)
add_button.grid(row=4, column=1)

# Create and place labels, entry field, and button for removing
Label(root, text="ID_client to Remove:").grid(row=5, column=0)
id_entry = Entry(root)
id_entry.grid(row=5, column=1)

remove_button = Button(root, text="Remove Client from Database", command=remove_from_database)
remove_button.grid(row=6, column=1)

# Start the main loop
root.mainloop()
