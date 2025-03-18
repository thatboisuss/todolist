
import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("350x450")
        self.root.configure(bg="#e0e0e0")
        
        self.tasks = []
        
        # Main Page
        self.main_frame = tk.Frame(self.root, bg="#e0e0e0")
        self.main_frame.pack(fill="both", expand=True)
        
        # Entry box for new task
        self.task_entry = tk.Entry(self.main_frame, width=30, font=("Arial", 12))
        self.task_entry.pack(pady=10)
        
        # Add task button
        self.add_task_btn = tk.Button(self.main_frame, text="Add Task", command=self.add_task, bg="#5cb85c", fg="white", font=("Arial", 10))
        self.add_task_btn.pack(pady=5)
        
        # View tasks button
        self.view_tasks_btn = tk.Button(self.main_frame, text="View Tasks", command=self.show_tasks_page, bg="#0275d8", fg="white", font=("Arial", 10))
        self.view_tasks_btn.pack(pady=5)
        
        # Tasks Page
        self.tasks_frame = tk.Frame(self.root, bg="#e0e0e0")
        
        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.tasks_frame, width=40, height=10, font=("Arial", 12))
        self.task_listbox.pack(pady=10)
        
        # Delete task button
        self.delete_task_btn = tk.Button(self.tasks_frame, text="Delete Task", command=self.delete_task, bg="#d9534f", fg="white", font=("Arial", 10))
        self.delete_task_btn.pack(pady=5)
        
        # Rename task button
        self.rename_task_btn = tk.Button(self.tasks_frame, text="Rename Task", command=self.rename_task, bg="#f0ad4e", fg="white", font=("Arial", 10))
        self.rename_task_btn.pack(pady=5)
        
        # Back to main page button
        self.back_btn = tk.Button(self.tasks_frame, text="Back", command=self.show_main_page, bg="#5bc0de", fg="white", font=("Arial", 10))
        self.back_btn.pack(pady=5)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def show_tasks_page(self):
        self.main_frame.pack_forget()
        self.tasks_frame.pack(fill="both", expand=True)
        self.update_task_listbox()
    
    def show_main_page(self):
        self.tasks_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
    
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")
    
    def rename_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task_name = self.task_entry.get()
            if new_task_name:
                self.tasks[selected_task_index[0]] = new_task_name
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a new task name.")
        else:
            messagebox.showwarning("Warning", "You must select a task to rename.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()