
from tkinter import *
from tkinter import messagebox
from pyperclip import copy
import json

# Initialize the main window
window = Tk()
window.title("Password Manager")
window.config(padx=550, pady=150)

# Importing modules for password generation
from random import randint, choice, shuffle

# Lists of characters to be used in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Function to generate a random password
def password_generator():
    letter_list = [choice(letters) for i in range(randint(8, 10))]
    symbols_list = [choice(symbols) for i in range(randint(2, 4))]
    numbers_list = [choice(numbers) for i in range(randint(2, 4))]

    passwordlist = letter_list + symbols_list + numbers_list
    shuffle(passwordlist)
    password = "".join(passwordlist)

    # Insert generated password into the password field and copy to clipboard
    password_field.insert(0, password)
    copy(password)


# Function to save the user input
def save_input():
    website = website_field.get()
    username = username_field.get()
    password = password_field.get()
    new_data = {
        website: {
            "Email": username,
            "Password": password
        }
    }

    # Validate user input
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty.")
    else:
        user_input = messagebox.askokcancel(title=website,
                                            message=f"These are the details you entered:\nUsername/Email: {username}\nPassword: {password}\nIs it okay to save?")

        if user_input:
            try:
                with open("data.json", "r") as data_created:
                    data = json.load(data_created)
            except FileNotFoundError:
                with open("data.json", "w") as first_data:
                    json.dump(new_data, first_data, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                password_field.delete(0, END)
                website_field.delete(0, END)


# Function to find website credentials
def find_website():
    web = website_field.get()
    try:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=f"Search Result for {web}", message="Data does not exist.")
    else:
        if web in data:
            email = data[web]["Email"]
            password = data[web]["Password"]
            messagebox.showinfo(title=f"Search Result for {web}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details exist for {web}.")


# Setting up the UI
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="mypass_logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website label and input field
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_field = Entry(width=35)
website_field.grid(row=1, column=1, columnspan=2)
website_field.focus()

# Username/Email label and input field
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
username_label.config(pady=6)

username_field = Entry(width=35)
username_field.grid(row=2, column=1, columnspan=2)
username_field.insert(0, "alemayehuyared9@gmail.com")

# Password label and input field
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_label.config(pady=6)

password_field = Entry(width=35)
password_field.grid(row=3, column=1)

# Buttons for generating password, adding data, and searching
generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(row=4, column=1)

add_button = Button(text="Add", width=30, command=save_input)
add_button.grid(row=5, column=1, columnspan=2)

search_btn = Button(text="Search", command=find_website)
search_btn.grid(row=1, column=3)

# Run the main loop
window.mainloop()
