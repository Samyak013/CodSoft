import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    current = entry_var.get()
    if button_text == "=":
        try:
            result = str(eval(current))
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(current + button_text)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#2C3E50")

# Center the window on the screen
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 400
window_height = 500
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), justify='right', bd=10, relief=tk.RIDGE, bg="#ECF0F1", fg="#2C3E50")
entry.pack(fill=tk.BOTH, padx=10, pady=10)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '×'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

frame = tk.Frame(root, bg="#2C3E50")
frame.pack(pady=10)

for row in buttons:
    row_frame = tk.Frame(frame, bg="#2C3E50")
    row_frame.pack(fill=tk.BOTH, expand=True)
    for button in row:
        btn = tk.Button(row_frame, text=button, font=("Arial", 20), width=5, height=2, bg="#34495E", fg="white", bd=2, relief=tk.RAISED, command=lambda b=button: on_click(b.replace('×', '*')))
        btn.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

root.mainloop()
