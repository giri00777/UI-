import tkinter as tk
from tkinter import ttk


class EmployeeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Data")
        width, height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry('%dx%d+0+0' % (width, height))
        self.tree = ttk.Treeview(root, columns=('ID', 'Name', 'Position'))
        self.tree.heading('#0', text='ID', anchor='center')
        self.tree.heading('#1', text='Name', anchor='center')
        self.tree.heading('#2', text='Position', anchor='center')
        self.tree.column('#0', width=50, anchor='center')
        self.tree.column('#1', width=150, anchor='center')
        self.tree.column('#2', width=150, anchor='center')
        self.tree.pack(expand=True, fill=tk.BOTH)

        self.load_data()

    def load_data(self):
        employees = [
            {'id': 1, 'name': 'Giri', 'position': 'Manager'},
            {'id': 2, 'name': 'Hari', 'position': 'Developer'},
            {'id': 3, 'name': 'Gita', 'position': 'Designer'},
            {'id': 4, 'name': 'Gokul', 'position': 'Tester'},
        ]

        for employee in employees:
            self.tree.insert('', 'end', text=employee['id'],
                             values=(employee['name'], employee['position']))


def main():
    root = tk.Tk()
    app = EmployeeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
