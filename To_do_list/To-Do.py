import customtkinter as ctk
import tkinter as tk  # Import tkinter for constants like END

root = ctk.CTk()  # Create a CTK window
root.geometry("800x800")  # Set initial size
root.title("To-Do List")  # Title of the app
root.configure(bg="#42a5f5", fg="#fff")  # Set background colour

task_frame = ctk.CTkFrame(root)
task_frame.grid(row=0, column=0, sticky="nsew")  # Use grid for task frame

# Adding visual cues:

# task_frame.configure(borderwidth=2, relief="groove")  # Add border to task frame
taskList = ctk.CTkFrame(task_frame, height=15)
taskList.grid(row=0, column=0, sticky="nsew")  # Use grid for task list
# taskList.configure(borderwidth=1, relief="solid")  # Add border to task list

task_label = ctk.CTkLabel(task_frame, text="Add Task:")
task_label.configure(font=("Arial", 14, "bold"))
task_label.grid(row=1, column=0, columnspan=2, sticky="nsew")  # Span across 2 columns

task_entry = ctk.CTkEntry(task_frame, width=40)
task_entry.grid(row=2, column=0, columnspan=2, sticky="nsew")  # Span across 2 columns


def add_task():
    task = task_entry.get()
    taskList.insert(tk.END, task)
    task_entry.delete(0, tk.END)

def remove_task():
    selected_task = taskList.get_selected()
    if selected_task:
        taskList.delete(taskList.index(selected_task))
    else:
        ctk.messagebox.showinfo("No Task Selected", "Please select a task to remove")

def mark_task():
    selected_task = taskList.get_selected()
    if selected_task:
        taskList.itemconfig(selected_task, fg="#a9a9a9", strikethrough=True)  # Mark as completed
    else:
        ctk.messagebox.showinfo("No Task Selected", "Please select a task to mark as complete.")

add_button = ctk.CTkButton(task_frame, text="Add", command=add_task)
add_button.grid(row=3, column=0, padx=20, pady=20)

remove_button = ctk.CTkButton(task_frame, text="Remove", command=remove_task)
remove_button.grid(row=3, column=1, padx=20, pady=20)

mark_button = ctk.CTkButton(task_frame, text="Mark as Complete", command=mark_task)
mark_button.grid(row=4, column=0, columnspan=2, padx=20, pady=20)  # Span across 2 columns

# root.mainloop()  # Start the main event loop
# # ... (rest of your grid layout code)

root.mainloop()  # Start the main event loop