import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.phone} - {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        return f"Contact {contact.name} added successfully!"

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return f"Contact {name} removed successfully!"
        return f"Contact {name} not found."

    def list_contacts(self):
        if not self.contacts:
            return "No contacts found."
        return "\n".join(str(contact) for contact in self.contacts)

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contact_book = ContactBook()

        self.name_label = tk.Label(root, text="Name")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(root, text="Phone")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(root, text="Email")
        self.email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, columnspan=2)

        self.remove_button = tk.Button(root, text="Remove Contact", command=self.remove_contact)
        self.remove_button.grid(row=4, column=0, columnspan=2)

        self.list_button = tk.Button(root, text="List Contacts", command=self.list_contacts)
        self.list_button.grid(row=5, column=0, columnspan=2)

        self.output_text = tk.Text(root, height=10, width=40)
        self.output_text.grid(row=6, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if name and phone and email:
            contact = Contact(name, phone, email)
            message = self.contact_book.add_contact(contact)
            self.output_text.insert(tk.END, message + "\n")
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    def remove_contact(self):
        name = self.name_entry.get()
        if name:
            message = self.contact_book.remove_contact(name)
            self.output_text.insert(tk.END, message + "\n")
        else:
            messagebox.showwarning("Input Error", "Name field is required.")

    def list_contacts(self):
        contacts = self.contact_book.list_contacts()
        self.output_text.insert(tk.END, contacts + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
