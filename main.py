
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json
def random_pass():

#Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    pyperclip.copy(password)




    # Insert password into password_entry
    password_entry.delete(0, END)
    password_entry.insert(0, password)
#  FIND PASSWORD
def find_password():
    website = website_entry.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showerror("Error", "No data found.")
    else:
        if website in data:
             email = data[website]['email']
             password = data[website]['password']
             messagebox.showinfo('Password Found', f'Your Email {email} and password is: {password}')
        else:
            messagebox.showerror("Error", f"No details for {website} found.")


#  SAVE PASSWORD  #
# def add_data():
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     new_data = {website:{
#         "email": email,
#         "password": password,
#     }}
#
#     if len(website) == 0:
#         messagebox.showerror(title="Oops", message="Please dont leave the field empty")
#     elif len(password) == 0:
#         messagebox.showerror(title="Oops", message="Please dont leave the field empty")
#     else:
#             with open("data.json", "r") as data_file:
#                 data = json.load(data_file)
#                 data.update(new_data)
#
#             with open("data.json", "w") as data:
#                 json.dump(new_data, data ,indent=4)
#
#
#             clear_entry()
#             messagebox.showinfo(title="Success", message="Data added successfully")
def add_data():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if not website or not password:
        messagebox.showerror(title="Oops", message="Please don’t leave the fields empty")
    else:
        try:

            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:

            data = new_data
        else:

            data.update(new_data)
            print(data)

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        clear_entry()
        messagebox.showinfo(title="Success", message="Data added successfully")








def clear_entry():
    website_entry.delete(0, END)
    password_entry.delete(0, END)




#  UI SETUP  #
window = Tk()
window.title("Password manager ")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, )
logo_png = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=0, column=1)

website_label = Label( text="Website:")
website_label.grid(row=1, column=0)
email_label = Label( text="Email:")
email_label.grid(row=2, column=0)
password_label = Label( text="Password:")
password_label.grid(row=3, column=0)


website_entry = Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0, "shivam_237029@saitm.ac.in")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_pass_button = Button(text="Generate Password",command=random_pass)
generate_pass_button.grid(row=3, column=2)


search_button = Button(text="Search",width=13,command=find_password)
search_button .grid(row=1, column=3)

add_password_button = Button(text="Add Password",width=36,command=add_data)
add_password_button.grid(row=4, column=1,columnspan=2)






window.mainloop()