from connect import connect_to_database
from tkinter import messagebox

def drop_table(
        
):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        kill_query = "DROP DATABASE proiect;"
        cursor.execute(
            kill_query,
        )

        connection.commit()

        cursor.close()
        connection.close()

        messagebox.showinfo("Success", "Baza de date daramata!")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")
