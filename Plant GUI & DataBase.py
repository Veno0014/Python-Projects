import tkinter as tk
from tkinter import messagebox
import sqlite3

# Creating Database
def plant_db():
    conn = sqlite3.connect("plant_users.db")
    c = conn.cursor()
    # Creating plant user's database
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT,
        password TEXT
    )""")

    # Entering default user's login into the database
    c.execute("SELECT * FROM users WHERE username = 'PlantLover'")
    if not c.fetchone():
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('PlantLover', 'ILovePlants'))
        conn.commit()
    conn.close()

# Checks Credentials against table
def verify():
    usrname = entry_usrname.get()
    passwd = entry_passwd.get()

    conn = sqlite3.connect("plant_users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (usrname, passwd))
    result = c.fetchone()
    conn.close()

    #Messagebox actvates as per user login
    if result:
        messagebox.showinfo("Login Successful", f"Welcome to Plant Database, {usrname}")
        login.destroy()
        plantdb_login()
    else:
        messagebox.showerror("Login Failed", "Please enter the correct details")

# Interface After login
def plantdb_login():
    plant_database_login = tk.Tk()
    plant_database_login.title("Welcome to plant Database")
    plant_database_login.geometry("800x800")

    #Some Data
    tk.Label(plant_database_login, text="Welcome to the Plant Database", font=("Arial", 12)).pack(pady=20)
    tk.Label(plant_database_login, text = "Daffodile, 2meters, endangered").pack(pady=20)
    tk.Label(plant_database_login, text = "Marigold, 0.2meters, endangered").pack(pady=20)

    plant_database_login.mainloop()

#Login before interface
def interface():
    global login, entry_usrname, entry_passwd

    login = tk.Tk()
    login.title("Plant Database")
    login.geometry("400x400")

    tk.Label(login, text="Username:").pack(pady=12)
    entry_usrname = tk.Entry(login)
    entry_usrname.pack(pady=12)

    tk.Label(login, text="Password:").pack(pady=12)
    entry_passwd = tk.Entry(login, show='*')
    entry_passwd.pack(pady=7)

    # When button is clicked, to access the verify function
    login_btn = tk.Button(login, text="Login", command=verify)
    login_btn.pack(pady=7)

    login.mainloop()

# The application to run
plant_db()
interface()
