import json
from random import shuffle, randint, choice
from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty Field", message="Please complete the field")
    else:
        try:
            with open("data.json", "r") as data_files:
                data = json.load(data_files)
        except FileNotFoundError:
            with open("data.json", "w") as data_files:
                json.dump(new_data, data_files, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_files:
                json.dump(data, data_files, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website = Label(text="Website")
website.grid(row=1, column=0)
email_user = Label(text="Email/Username")
email_user.grid(row=2, column=0)
password = Label(text="Password")
password.grid(row=3, column=0)

# Entries
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
web_entry.focus()
email_user_entry = Entry(width=35)
email_user_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_user_entry.insert(0, "rachmat.fadlin@gmail.com")
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

# Button
gen_pass = Button(text="Generate Password", command=password_generator)
gen_pass.grid(row=3, column=2, sticky="EW")
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
