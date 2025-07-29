import tkinter as tk
from tkinter import messagebox, ttk

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ContactBook Management")
        self.root.configure(bg="#f0f0f0")
        self.contacts = []
        self.selected_index = None

        # Create UI elements
        self.create_widgets()
        self.populate_sample_data()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="ContactBook Management", font=("Arial", 18, "bold"), bg="#222", fg="white", pady=10)
        title.pack(fill=tk.X)

        # Form Frame
        form_frame = tk.Frame(self.root, bg="#f0f0f0", pady=10)
        form_frame.pack(side=tk.TOP, fill=tk.X, padx=20)

        labels = ["Store Name", "Phone Number", "Email", "Address"]
        self.entries = {}

        for i, label in enumerate(labels):
            tk.Label(form_frame, text=label, font=("Arial", 11), bg="#f0f0f0").grid(row=i, column=0, sticky=tk.W, pady=5)
            entry = tk.Entry(form_frame, width=35, font=("Arial", 11))
            entry.grid(row=i, column=1, pady=5, padx=10)
            self.entries[label] = entry

        # Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#f0f0f0", pady=10)
        btn_frame.pack(side=tk.TOP, fill=tk.X)

        btn_style = {"bg": "#222", "fg": "white", "activebackground": "#444", "font": ("Arial", 11, "bold"), "width": 15, "height": 1}

        self.add_btn = tk.Button(btn_frame, text="Add Contact", command=self.add_contact, **btn_style)
        self.add_btn.pack(side=tk.LEFT, padx=10)

        self.update_btn = tk.Button(btn_frame, text="Update Contact", command=self.update_contact, **btn_style)
        self.update_btn.pack(side=tk.LEFT, padx=10)

        self.delete_btn = tk.Button(btn_frame, text="Delete Contact", command=self.delete_contact, **btn_style)
        self.delete_btn.pack(side=tk.LEFT, padx=10)

        self.reset_btn = tk.Button(btn_frame, text="Reset Fields", command=self.reset_form, **btn_style)
        self.reset_btn.pack(side=tk.LEFT, padx=10)

        # Contacts Table
        self.tree = ttk.Treeview(self.root, columns=labels, show='headings', selectmode='browse')
        for col in labels:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.tree.bind('<<TreeviewSelect>>', self.on_contact_select)

    def populate_sample_data(self):
        sample = {
            "Store Name": "Example Store",
            "Phone Number": "1234567890",
            "Email": "example@store.com",
            "Address": "123 Example St"
        }
        self.contacts.append(sample)
        self.refresh_tree()

    def refresh_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for idx, contact in enumerate(self.contacts):
            values = (contact["Store Name"], contact["Phone Number"], contact["Email"], contact["Address"])
            self.tree.insert('', 'end', iid=idx, values=values)

    def add_contact(self):
        data = {key: entry.get().strip() for key, entry in self.entries.items()}
        if not all(data.values()):
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return
        if not data["Phone Number"].isdigit():
            messagebox.showwarning("Input Error", "Phone Number must be digits only.")
            return
        self.contacts.append(data)
        self.refresh_tree()
        self.reset_form()

    def update_contact(self):
        if self.selected_index is None:
            messagebox.showwarning("Selection Error", "Select a contact to update.")
            return
        data = {key: entry.get().strip() for key, entry in self.entries.items()}
        if not all(data.values()):
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return
        if not data["Phone Number"].isdigit():
            messagebox.showwarning("Input Error", "Phone Number must be digits only.")
            return
        self.contacts[self.selected_index] = data
        self.refresh_tree()
        # Note: No reset after update

    def delete_contact(self):
        if self.selected_index is None:
            messagebox.showwarning("Selection Error", "Select a contact to delete.")
            return
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?")
        if confirm:
            del self.contacts[self.selected_index]
            self.refresh_tree()
            self.reset_form()

    def reset_form(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.selected_index = None
        self.tree.selection_remove(self.tree.selection())

    def on_contact_select(self, event):
        selected = self.tree.selection()
        if selected:
            idx = int(selected[0])
            self.selected_index = idx
            contact = self.contacts[idx]
            for key, entry in self.entries.items():
                entry.delete(0, tk.END)
                entry.insert(0, contact[key])

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.geometry("700x450")
    root.mainloop()
