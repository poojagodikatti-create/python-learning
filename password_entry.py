import tkinter as tk
from tkinter import messagebox

# Function to check login credentials
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Successful", f"Welcome {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")


# Main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")
root.configure(bg="lightblue")


# Username label and entry
label_username = tk.Label(
    root,
    text="Username:",
    font=("Arial", 12),
    bg="lightblue"
)
label_username.pack(pady=5)

entry_username = tk.Entry(root, width=25)
entry_username.pack(pady=5)


# Password label and entry
label_password = tk.Label(
    root,
    text="Password:",
    font=("Arial", 12),
    bg="lightblue"
)
label_password.pack(pady=5)

entry_password = tk.Entry(root, width=25, show="*")
entry_password.pack(pady=5)


# Login button
login_button = tk.Button(
    root,
    text="Login",
    command=login,
    bg="blue",
    fg="white",
    width=10
)
login_button.pack(pady=10)


# Run the GUI loop
root.mainloop()