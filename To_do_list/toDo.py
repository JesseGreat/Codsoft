import customtkinter as ctk
import tkinter as tk  # Import tkinter for constants like END

root = ctk.CTk()  # Create a CTK window
root.geometry("400x400")  # Set initial size
root.title("To-Do List")  # Title of the app
root.configure(bg="#42a5f5", fg="#fff")  # Set background colour

task_frame = ctk.CTkFrame(root)
task_frame.pack(pady=20)

task_list = ctk.CTkFrame(task_frame, height=15)
task_list.pack(side="left", fill='both', expand=True)

task_label = ctk.CTkLabel(root, text="Add Task:")
task_label.configure(font=("Arial", 14, "bold"))
task_label.pack()

task_entry = ctk.CTkEntry(root, width=40)
task_entry.pack()

def add_task():
    task = task_entry.get()
    task_list.insert(tk.END, task)
    task_entry.delete(0, tk.END)

def remove_task():
    selected_task = task_list.get_selected()
    if selected_task:
        task_list.delete(task_list.index(selected_task))
    else:
        ctk.messagebox.showinfo("No Task Selected", "Please select a task to remove")

def mark_task():
    selected_task = task_list.get_selected()
    if selected_task:
        task_list.itemconfig(selected_task, fg="#a9a9a9", strikethrough=True)  # Mark as completed
    else:
        ctk.messagebox.showinfo("No Task Selected", "Please select a task to mark as complete.")

add_button = ctk.CTkButton(root, text="Add", command=add_task)
# add_button.grid(row=0, column=0, padx=20, pady=20)
add_button.pack()
remove_button = ctk.CTkButton(root, text="Remove", command=remove_task)
# remove_button.grid(row=0, column=1, padx=20, pady=20)
remove_button.pack()  #  display the remove button
mark_button = ctk.CTkButton(root, text="Mark as Complete", command=mark_task)
# mark_button.grid(row=0, column=2, padx=20, pady=20)
mark_button.pack()  #  display the mark button

root.mainloop()  # Start the main event loop