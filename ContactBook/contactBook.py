import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        ctk.set_appearance_mode('dark')
        self.root.title("Contact Book")
        
        self.contacts = []

        # Create main frame
        self.main_frame = ctk.CTkFrame(root)
        self.main_frame.pack()

        # Create left frame for adding contacts
        self.left_frame = ctk.CTkFrame(self.main_frame)
        self.left_frame.pack(side=ctk.LEFT, padx=20)

        # Create right frame for listing contacts and other functionalities
        self.right_frame = ctk.CTkFrame(self.main_frame)
        self.right_frame.pack(side=ctk.RIGHT, padx=20)

        # Create and configure visual elements in the left frame
        ctk.CTkLabel(self.left_frame, text="Name:", font=("Times", 20, "italic", "bold")).grid(row=0, column=0)
        self.name_entry = ctk.CTkEntry(self.left_frame, font=("Arial black", 15, "bold"))
        self.name_entry.grid(row=0, column=1, pady=10)

        ctk.CTkLabel(self.left_frame, text="Phone:", font=("Times", 20, "italic", "bold")).grid(row=1, column=0)
        self.phone_entry = ctk.CTkEntry(self.left_frame, font=("Arial black", 15, "bold"))
        self.phone_entry.grid(row=1, column=1, pady=10)

        ctk.CTkLabel(self.left_frame, text="Email:", font=("Times", 20, "italic", "bold")).grid(row=2, column=0)
        self.email_entry = ctk.CTkEntry(self.left_frame, font=("Arial black", 15, "bold"))
        self.email_entry.grid(row=2, column=1, pady=10)

        ctk.CTkLabel(self.left_frame, text="Address:", font=("Times", 20, "italic", "bold")).grid(row=3, column=0)
        self.address_entry = ctk.CTkEntry(self.left_frame, font=("Arial black", 15, "bold"))
        self.address_entry.grid(row=3, column=1, pady=10)

        self.add_button = ctk.CTkButton(self.left_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=1, columnspan=2, pady=10)

        # Create and configure visual elements in the right frame
        self.search_entry = ctk.CTkEntry(self.right_frame, width=30)  # Adjust width as needed
        self.search_entry.grid(row=0, column=0, padx=5, pady=5, columnspan=2, sticky="ew")

        self.search_button = ctk.CTkButton(self.right_frame, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        self.contact_listbox = tk.Listbox(self.right_frame, height=30, width=60, font=("Arial black", 11, "bold"))
        self.contact_listbox.grid(row=1, column=0, pady=10, columnspan=2)

        self.view_button = ctk.CTkButton(self.right_frame, text="View Contacts", command=self.view_contacts, width=5)
        self.view_button.grid(row=3, column=0, padx=(0, 5), pady=(5, 0), sticky="ew")  # Adjusted padx and sticky

        self.update_button = ctk.CTkButton(self.right_frame, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=3, column=1, padx=(0, 5), pady=(5, 0), sticky="ew")  # Adjusted padx and sticky

        self.delete_button = ctk.CTkButton(self.right_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=3, column=2, pady=(5, 0), sticky="ew")  # Adjusted sticky





    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not name or not phone:
            messagebox.showerror("Error", "Please enter name and phone number.")
            return

        contact_info = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nAddress: {address}"
        self.contacts.append(contact_info)
        self.contact_listbox.insert(ctk.END, name)

    def view_contacts(self):
        selected_index = self.contact_listbox.curselection()
        if not selected_index:
            messagebox.showinfo("Info", "Please select a contact to view.")
            return

        contact_info = self.contacts[selected_index[0]]
        messagebox.showinfo("Contact Information", contact_info)

    def search_contact(self):
        query = self.search_entry.get().lower()
        matching_contacts = [contact for contact in self.contacts if query in contact.lower()]

        self.contact_listbox.delete(0, ctk.END)
        for contact in matching_contacts:
            self.contact_listbox.insert(ctk.END, contact.split('\n')[0])  # Display only names

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if not selected_index:
            messagebox.showinfo("Info", "Please select a contact to update.")
            return

        current_contact_info = self.contacts[selected_index[0]]
        updated_contact_info = simple_input("Update contact information:", current_contact_info)

        self.contacts[selected_index[0]] = updated_contact_info
        self.view_contacts()

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if not selected_index:
            messagebox.showinfo("Info", "Please select a contact to delete.")
            return

        confirmed = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this contact?")
        if confirmed:
            self.contacts.pop(selected_index[0])
            self.contact_listbox.delete(selected_index)
            messagebox.showinfo("Info", "Contact deleted successfully.")

def simple_input(prompt, default=""):
    return simpledialog.askstring("Input", prompt, initialvalue=default)

if __name__ == "__main__":
    root = ctk.CTk()
    app = ContactBookApp(root)
    root.mainloop()
