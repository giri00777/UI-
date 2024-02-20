import customtkinter as ctk
from tkinter import messagebox, Toplevel, PhotoImage
from PIL import Image, ImageTk
import mysql.connector
import os
import re


class LoginApplication:
    def __init__(self, root):
        self.username_label = None
        self.root = root
        self.root.configure(background='orange')
        self.root.title("Login")

        width, height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry('%dx%d+0+0' % (width, height))
        img_background_path = r"C:\Users\91638\Downloads\neon-sign-background-isolated\9305945.png"
        original_image = PhotoImage(file=img_background_path)
        resized_image = original_image.subsample(int(original_image.width() / width),
                                                 int(original_image.height() / height))
        background_label = ctk.CTkLabel(self.root, text="", image=resized_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame = ctk.CTkFrame(self.root, width=400, height=300, fg_color="#25AFBB")
        self.frame.place(relx=0.380, rely=0.2)

        self.widget()

    def widget(self):
        heading_label = ctk.CTkLabel(self.root, text="Login System", font=("Times new roman", 40, "bold"))
        heading_label.pack(pady=20)
        self.username_label = ctk.CTkLabel(self.frame, text=" Username", font=("Poppins", 15, "bold"))
        self.username_label.place(relx=0.1, rely=0.110)
        self.username_entry = ctk.CTkEntry(self.frame, placeholder_text="Enter username", width=200, height=30,
                                           font=("Poppins", 12))
        self.username_entry.place(relx=0.375, rely=0.100)
        self.password_label = ctk.CTkLabel(self.frame, text=" Password", font=("Poppins", 15, "bold"))
        self.password_label.place(relx=0.1, rely=0.300)
        self.password_entry = ctk.CTkEntry(self.frame, show="*", placeholder_text="Enter password", width=200,
                                           height=30)
        self.password_entry.place(relx=0.375, rely=0.300)

        self.login_button = ctk.CTkButton(self.frame, text="Login", command=self.login, cursor="hand2", width=70,
                                          fg_color="#11335F", hover_color="red", corner_radius=3, border_width=1)
        self.login_button.place(relx=0.450, rely=0.550)
        self.signup_button = ctk.CTkButton(self.frame, text="Signup", command=self.signup_1, cursor="hand2", width=40,
                                           fg_color="#00626A")
        self.signup_button.place(relx=0.450, rely=0.8)

        self.back_button = ctk.CTkButton(self.root, text="Back", command=self.go_back, cursor="hand2",
                                         fg_color="#265DA2")
        self.back_button.place(relx=0.460, rely=0.750)

        self.sign_label = ctk.CTkLabel(self.frame, text="Do you have account ?")
        self.sign_label.place(relx=0.1, rely=0.8)

    def login(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        try:
            query = "SELECT * FROM login WHERE username = %s AND password = %s"
            cursor.execute(query, (entered_username, entered_password))
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Login Successful", "Welcome, " + entered_username + "!")
                self.adm1()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    def signup_1(self):
        SignupWindow(self.root)

    def go_back(self):
        print("Back")

    def adm1(self):
        self.root.withdraw()
        os.system("python employee.py")
        self.root.deiconify()


class SignupWindow:
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("Sign Up")
        self.root.geometry("600x500")

        self.create_widgets()

    def create_widgets(self):
        self.name_label = ctk.CTkLabel(self.root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.name_entry = ctk.CTkEntry(self.root, placeholder_text="Enter name", width=200)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.email_label = ctk.CTkLabel(self.root, text="Email:")
        self.email_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.email_entry = ctk.CTkEntry(self.root, placeholder_text="Enter your e-mail", width=200)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)

        self.phone_label = ctk.CTkLabel(self.root, text="Phone:")
        self.phone_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.phone_entry = ctk.CTkEntry(self.root, placeholder_text="Enter your Phonenumber", width=200)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=10)

        self.password_label = ctk.CTkLabel(self.root, text="Password:")
        self.password_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.password_entry = ctk.CTkEntry(self.root, show="*", placeholder_text="Enter your password", width=200)
        self.password_entry.grid(row=3, column=1, padx=10, pady=10)

        self.signup_button = ctk.CTkButton(self.root, text="Sign Up", command=self.signup)
        self.signup_button.grid(row=4, column=1, pady=20)

    def signup(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phoneno = self.phone_entry.get()
        password = self.password_entry.get()

        try:
            query = "INSERT INTO login (username, Email, Phone, password) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, email, phoneno, password))
            db.commit()
            messagebox.showinfo("Sign Up Successful", "Account created successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")


if __name__ == "__main__":
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="scratch"
    )
    cursor = db.cursor()
    root = ctk.CTk()
    app = LoginApplication(root)
    root.mainloop()
    cursor.close()
    db.close()
