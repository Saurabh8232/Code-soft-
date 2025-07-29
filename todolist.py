import tkinter as tk
from tkinter import messagebox, simpledialog
import os

TASKS_FILE = "tasks.txt"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.configure(bg='#121212') 

        self.tasks = []

        # Task entry label & input
        self.task_label = tk.Label(root, text="Enter the Task:", bg='#121212', fg='white', font=("Arial", 12))
        self.task_label.pack(pady=5)

        self.task_entry = tk.Entry(root, width=50, font=("Arial", 12), bg='white', fg='black')
        self.task_entry.pack(pady=5)

        # Frame to hold top buttons
        button_frame = tk.Frame(root, bg='#121212')
        button_frame.pack(pady=10)

        # Button Style
        btn_bg = '#03dac6'  
        btn_fg = '#000000'  

        self.add_task_button = tk.Button(button_frame, text="Add Task", command=self.add_task, bg=btn_bg, fg=btn_fg, width=12)
        self.add_task_button.grid(row=0, column=0, padx=5)

        self.edit_task_button = tk.Button(button_frame, text="Edit Task", command=self.edit_task, bg=btn_bg, fg=btn_fg, width=12)
        self.edit_task_button.grid(row=0, column=1, padx=5)

        self.mark_done_button = tk.Button(button_frame, text="Mark as Done", command=self.mark_done, bg=btn_bg, fg=btn_fg, width=12)
        self.mark_done_button.grid(row=0, column=2, padx=5)

        self.delete_task_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task, bg=btn_bg, fg=btn_fg, width=12)
        self.delete_task_button.grid(row=0, column=3, padx=5)

        self.delete_all_tasks_button = tk.Button(button_frame, text="Delete All", command=self.delete_all_tasks, bg=btn_bg, fg=btn_fg, width=12)
        self.delete_all_tasks_button.grid(row=0, column=4, padx=5)

        self.save_task_button = tk.Button(button_frame, text="Save Tasks", command=self.save_tasks, bg=btn_bg, fg=btn_fg, width=12)
        self.save_task_button.grid(row=0, column=5, padx=5)

        self.load_task_button = tk.Button(button_frame, text="Load Tasks", command=self.load_tasks, bg=btn_bg, fg=btn_fg, width=12)
        self.load_task_button.grid(row=0, column=6, padx=5)

        # Task list box
        self.task_listbox = tk.Listbox(root, width=90, height=15, font=("Arial", 12), bg='#1f1f1f', fg='white', selectbackground='#03dac6', selectforeground='black')
        self.task_listbox.pack(pady=20)

        # Exit button at the bottom
        self.exit_button = tk.Button(root, text="Exit", command=root.quit, bg=btn_bg, fg=btn_fg, width=20)
        self.exit_button.pack(pady=10)

        # Load tasks on startup
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def edit_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            current_task = self.tasks[index]
            new_task = simpledialog.askstring("Edit Task", "Update the selected task:", initialvalue=current_task)
            if new_task:
                self.tasks[index] = new_task
                self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to edit.")

    def mark_done(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.tasks[index]
            if not task.startswith("✓ "):
                self.tasks[index] = "✓ " + task
                self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as done.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def delete_all_tasks(self):
        if messagebox.askyesno("Confirmation", "Delete all tasks?"):
            self.tasks.clear()
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        with open(TASKS_FILE, "w") as f:
            for task in self.tasks:
                f.write(task + "\n")
        messagebox.showinfo("Saved", "Tasks saved successfully!")

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                self.tasks = [line.strip() for line in f.readlines()]
            self.update_task_list()

# Start App
root = tk.Tk()
app = ToDoApp(root)
root.geometry("1200x600")  
root.mainloop()
