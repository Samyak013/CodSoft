import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def generate_password():
    try:
        length = int(length_var.get())
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4 characters for better security.")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter a valid number.")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#2C3E50")  # Dark blue background for a modern look
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="🔐 Secure Password Generator", font=("Arial", 16, "bold"), fg="#ECF0F1", bg="#2C3E50")
title_label.pack(pady=10)

# Length Input Frame
frame = tk.Frame(root, bg="#2C3E50")
frame.pack(pady=10)
length_label = tk.Label(frame, text="Password Length:", font=("Arial", 12), fg="#ECF0F1", bg="#2C3E50")
length_label.pack(side=tk.LEFT, padx=5)
length_var = tk.StringVar()
length_entry = ttk.Entry(frame, textvariable=length_var, font=("Arial", 12))
length_entry.pack(side=tk.LEFT, padx=5)

# Style Configuration
style = ttk.Style()
style.configure("TButton", font=("Arial", 12, "bold"), padding=10)
style.configure("TButton", background="#3498DB", foreground="white")

# Generate Button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12, "bold"), bg="#3498DB", fg="white", activebackground="#2980B9", activeforeground="white", relief="flat", padx=10, pady=5)
generate_btn.pack(pady=10)

# Password Display
password_var = tk.StringVar()
password_entry = ttk.Entry(root, textvariable=password_var, font=("Arial", 14), state='readonly', justify='center')
password_entry.pack(pady=10, fill=tk.BOTH, padx=20)

# Copy to Clipboard Function
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Success", "Password copied to clipboard!")

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12, "bold"), bg="#27AE60", fg="white", activebackground="#1E8449", activeforeground="white", relief="flat", padx=10, pady=5)
copy_btn.pack(pady=5)

# Adjust window size dynamically
root.update_idletasks()
root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")

# Center the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - root.winfo_width()) // 2
y_position = (screen_height - root.winfo_height()) // 2
root.geometry(f"{root.winfo_width()}x{root.winfo_height()}+{x_position}+{y_position}")

root.mainloop()
