from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import copy

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    entry = f"{website} | {username} | {password}\n"

    empty_fields = len(website) < 1 or len(username) < 1 or len(password) < 1

    if empty_fields:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok_to_save = messagebox.askokcancel(
            title="website", message=f"These are the details entered: \n Username: {username} \n Password: {password} \n Save?")

        if is_ok_to_save:
            with open("day-29/data.txt", "a") as f:
                f.write(entry)
                # erase fields
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="day-29/logo.png")
canvas.create_image(100, 100, image=lock_image)

canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")


# Entries
website_entry = Entry(width=37)
username_entry = Entry(width=37)
username_entry.insert(0, "ferreiraplucas@gmail.com")
password_entry = Entry(width=21)
generate_password_button = Button(
    text="Generate Password", width=12, command=generate_password)
add_button = Button(text="Add", width=35, command=save)

# Grid
website_label.grid(column=0, row=1)
username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_entry.grid(column=1, row=1, columnspan=2)
username_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)
generate_password_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

website_entry.focus()

window.mainloop()
