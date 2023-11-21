import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        # Creating GUI components
        self.task_entry = tk.Entry(self.master, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task, bg="lightblue", font ="bold")
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.master, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.remove_button = tk.Button(self.master, text="Remove Task", command=self.remove_task, bg="lightblue", font="bold")
        self.remove_button.grid(row=2, column=0, padx=10, pady=10)

        self.clear_button = tk.Button(self.master, text="Clear All", command=self.clear_tasks, bg="lightblue",font="bold")
        self.clear_button.grid(row=2, column=1, padx=10, pady=10)

        # Loading tasks from file
        self.load_tasks()

        # Binding double-click event to remove task
        self.task_listbox.bind("<Double-Button-1>", lambda event: self.remove_task())

        # Updating the task listbox
        self.update_task_listbox()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)  # Clear the entry field
            self.update_task_listbox()
            self.save_tasks()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.update_task_listbox()
            self.save_tasks()

    def clear_tasks(self):
        confirmed = messagebox.askyesno("Clear All Tasks", "Are you sure you want to clear all tasks?")
        if confirmed:
            self.tasks = []
            self.update_task_listbox()
            self.save_tasks()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            pass  # If the file doesn't exist, just ignore it

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
