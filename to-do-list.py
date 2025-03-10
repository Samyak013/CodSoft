import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Database Functions
def create_table():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      task TEXT NOT NULL,
                      status TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_task():
    task = task_entry.get()
    if task:
        conn = sqlite3.connect("todo.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (task, status) VALUES (?, ?)", (task, "Pending"))
        conn.commit()
        conn.close()
        task_entry.delete(0, tk.END)
        renumber_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def load_tasks():
    task_list.delete(*task_list.get_children())
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY id")
    tasks = cursor.fetchall()
    conn.close()
    for i, task in enumerate(tasks, start=1):
        task_list.insert("", "end", values=(i, task[1], task[2]))

def renumber_tasks():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY id")
    tasks = cursor.fetchall()
    cursor.execute("DELETE FROM tasks")
    for i, task in enumerate(tasks, start=1):
        cursor.execute("INSERT INTO tasks (id, task, status) VALUES (?, ?, ?)", (i, task[1], task[2]))
    conn.commit()
    conn.close()
    load_tasks()

def update_task():
    try:
        selected_item = task_list.selection()[0]
        task_index = task_list.item(selected_item)['values'][0]
        new_status = status_var.get()
        conn = sqlite3.connect("todo.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_index))
        conn.commit()
        conn.close()
        load_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to update!")

def delete_task():
    try:
        selected_item = task_list.selection()[0]
        task_index = task_list.item(selected_item)['values'][0]
        conn = sqlite3.connect("todo.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_index,))
        conn.commit()
        conn.close()
        renumber_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

# GUI Setup
root = tk.Tk()
root.title("To-Do List")
root.configure(bg="#2C3E50")
root.resizable(False, False)

frame = tk.Frame(root, bg="#34495E", padx=10, pady=10)
frame.pack(pady=10, fill=tk.BOTH, expand=True)

# Task Entry
task_entry = tk.Entry(frame, width=40, font=("Helvetica", 14))
task_entry.grid(row=0, column=0, padx=10, pady=10)
add_button = tk.Button(frame, text="Add Task", command=add_task, bg="#27AE60", fg="white", font=("Helvetica", 12), padx=10)
add_button.grid(row=0, column=1, padx=10, pady=10)

# Task List
task_list = ttk.Treeview(frame, columns=("#", "Task", "Status"), show="headings", height=10)
task_list.heading("#", text="#")
task_list.heading("Task", text="Task")
task_list.heading("Status", text="Status")
task_list.column("#", width=40, anchor="center")
task_list.column("Task", width=300)
task_list.column("Status", width=100, anchor="center")
task_list.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Update Status
status_var = tk.StringVar(value="Pending")
status_menu = ttk.Combobox(frame, textvariable=status_var, values=["Pending", "Completed"], state="readonly", font=("Helvetica", 12))
status_menu.grid(row=2, column=0, pady=10)
update_button = tk.Button(frame, text="Update", command=update_task, bg="#F39C12", fg="white", font=("Helvetica", 12), padx=10)
update_button.grid(row=2, column=1, pady=10)

# Delete Task
delete_button = tk.Button(frame, text="Delete", command=delete_task, bg="#E74C3C", fg="white", font=("Helvetica", 12), padx=10)
delete_button.grid(row=3, column=0, columnspan=2, pady=10)

# Load Tasks
create_table()
load_tasks()

# Adjust window size based on content
root.update_idletasks()
root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")

# Center window on screen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")

root.mainloop()
