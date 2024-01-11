import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

task_counter = 1  # Initialize task counter

def add_task(event=None):  # Accept an event argument for key binding
    global task_counter  # Use the global task counter variable
    task = task_entry.get()
    if task:
        task_text = f"{task_counter}. {task}"  # Include the task number
        task_list.insert(tk.END, task_text)
        task_entry.delete(0, tk.END)
        task_counter += 1  # Increment the task counter
# Bind the Enter key to the add_task function


def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        confirmed = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this task?")
        if confirmed:
            task_list.delete(selected_task)
    else:
        messagebox.showinfo("No Task Selected", "Please select a task to remove")
        

def complete_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_item = task_list.get(selected_task)
        task_list.itemconfig(selected_task, {'bg': 'yellow', 'fg': 'black'})
        task_list.selection_clear(selected_task)

def delete_all_tasks():
    confirmed = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete all tasks?")
    if confirmed:
        task_list.delete(0, tk.END)

        
# Create main window
root = ctk.CTk()
root.geometry("1000x800")  # Adjusted the initial window size
root.title("To-Do List")
root.configure(bg="#42a5f5", fg="#fff")
root.bind("<Return>", add_task)

# Create main frame with a 2-column grid
main_frame = ctk.CTkFrame(root)
main_frame.grid(row=0, column=0, sticky="nsew")

# Allow main_frame to expand
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create left and right frames
left_frame = tk.Frame(main_frame, bg="#2196F3")
right_frame = ctk.CTkFrame(main_frame)
left_frame.grid(row=0, column=0, sticky="nsew")
right_frame.grid(row=0, column=1, sticky="nsew")

# Allow left and right frames to expand
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

# Label on the left frame
# label_todo = ctk.CTkLabel(left_frame, text="TO-DO List", font=("Arial", 20, "bold"))
# label_todo.pack(pady=50)
label_todo = ctk.CTkLabel(left_frame, text="TO-DO List", font=("Arial", 20, "bold"))
label_todo.place(anchor="center", relx=0.5, rely=0.5)  # Center horizontally and vertically

# Configure background and foreground colors for the right frame
# right_frame.configure(bg="#42a5f5", fg="#fff")

# Create and configure visual cues
task_entry = ctk.CTkEntry(right_frame, width=50, font=("Arial black", 15, "bold"))  # Adjust font size 
task_entry.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

# Create task list frame on the right frame
task_list = tk.Listbox(right_frame, height=30, width=70, font=("Arial black", 11, "bold"))  # Adjust font size 
task_list.grid(row=0, column=0, sticky="nsew")


# Position the frames
left_frame.grid(row=0, column=0, sticky="nsew")
right_frame.grid(row=0, column=1, sticky="nsew")


# Create buttons with associated functions
add_button = ctk.CTkButton(right_frame, text="Add", command=add_task, font=("Arial", 20, "bold"))
add_button.grid(row=2, column=0, sticky="nsew", padx=20, pady=5)

remove_button = ctk.CTkButton(right_frame, text="Remove Task", command=remove_task, font=("Arial", 20, "bold"))
remove_button.grid(row=3, column=0, sticky="nsew", padx=20, pady=5)

mark_button = ctk.CTkButton(right_frame, text="Task Complete", command=complete_task, font=("Arial", 20, "bold"))
mark_button.grid(row=4, column=0, sticky="nsew", padx=20, pady=5)

delete_all_button = ctk.CTkButton(right_frame, text="Delete All Tasks", command=delete_all_tasks, font=("Arial", 20, "bold"))
delete_all_button.grid(row=5, column=0, sticky="nsew", padx=20, pady=5)  # Adjust placement as needed

# Start the main event loop
root.mainloop()