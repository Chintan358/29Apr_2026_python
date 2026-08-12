import tkinter as tk
from tkinter import messagebox

# ==========================
# Functions
# ==========================
def register():
    username = txt_username.get()
    email = txt_email.get()
    phone = txt_phone.get()

    if username == "" or email == "" or phone == "":
        messagebox.showwarning("Validation", "All fields are required!")
        return

    messagebox.showinfo(
        "Registration Successful",
        f"Username : {username}\nEmail : {email}\nPhone : {phone}"
    )

    txt_username.delete(0, tk.END)
    txt_email.delete(0, tk.END)
    txt_phone.delete(0, tk.END)

# ==========================
# Main Window
# ==========================
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("500x450")
root.resizable(False, False)
root.configure(bg="#EAF4FF")

# ==========================
# Header
# ==========================
header = tk.Frame(root, bg="#1565C0", height=80)
header.pack(fill="x")

title = tk.Label(
    header,
    text="Student Registration",
    font=("Segoe UI", 22, "bold"),
    bg="#1565C0",
    fg="white"
)
title.pack(pady=20)

# ==========================
# Form Frame
# ==========================
form_frame = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="solid"
)
form_frame.place(x=50, y=110, width=400, height=280)

# Username
lbl_username = tk.Label(
    form_frame,
    text="Username",
    font=("Segoe UI", 11, "bold"),
    bg="white"
)
lbl_username.place(x=30, y=30)

txt_username = tk.Entry(
    form_frame,
    font=("Segoe UI", 12),
    bd=2
)
txt_username.place(x=30, y=55, width=320)

# Email
lbl_email = tk.Label(
    form_frame,
    text="Email",
    font=("Segoe UI", 11, "bold"),
    bg="white"
)
lbl_email.place(x=30, y=100)

txt_email = tk.Entry(
    form_frame,
    font=("Segoe UI", 12),
    bd=2
)
txt_email.place(x=30, y=125, width=320)

# Phone
lbl_phone = tk.Label(
    form_frame,
    text="Phone",
    font=("Segoe UI", 11, "bold"),
    bg="white"
)
lbl_phone.place(x=30, y=170)

txt_phone = tk.Entry(
    form_frame,
    font=("Segoe UI", 12),
    bd=2
)
txt_phone.place(x=30, y=195, width=320)

# Register Button
btn_register = tk.Button(
    form_frame,
    text="Register",
    font=("Segoe UI", 12, "bold"),
    bg="#1565C0",
    fg="white",
    activebackground="#0D47A1",
    activeforeground="white",
    cursor="hand2",
    command=register
)
btn_register.place(x=120, y=235, width=150, height=35)

# Footer
footer = tk.Label(
    root,
    text="Student Management System",
    bg="#EAF4FF",
    fg="gray",
    font=("Segoe UI", 9)
)
footer.pack(side="bottom", pady=10)

root.mainloop()