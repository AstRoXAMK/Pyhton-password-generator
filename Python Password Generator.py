import random as r
import string as s
from tkinter import *
import os

root =  Tk()
root.title("Simple password generator")
root.iconbitmap("./icon/cigarette.ico")
root.geometry("400x375")

# $ -- START OF FUNCTIONS -- $ #
# * -- Check password for integer number -- * #
def password_checker():
    try:
        int(password_amount.get())
        int(password_number.get())
        result.config(text=f"New file by name new_passwords has been created in the program folder")
        checkbox_btn_check()
        password_check.config(state=DISABLED)
    except ValueError:
        result.config(text = f"{password_amount.get()} or {password_number.get()} is not an integer number")

# * -- Check checkboxes for values -- * #
def checkbox_btn_check():

    if check_number.get() == 0 and check_symbols.get() == 1:
        for i in range(int(password_number.get())):
            generate_strong_password(int(password_amount.get()), int(password_number.get()), False, True)
    elif check_number.get() == 1 and check_symbols.get() == 0:
        for i in range(int(password_number.get())):
            generate_strong_password(int(password_amount.get()), int(password_number.get()), True, False)
    elif check_number.get() == 1 and check_symbols.get() == 1:
        for i in range(int(password_number.get())):
            generate_strong_password(int(password_amount.get()), int(password_number.get()), True, True)
    else:
        for i in range(int(password_number.get())):
            generate_strong_password(int(password_amount.get()), int(password_number.get()), False, False)

# * -- Generates Passwords -- * #
def generate_strong_password(amount: int, char_count: int, gate1: bool, gate2: bool):
    special_symbols = "!?=+-()#"
    passwords = []
    for i in range(amount):
        password =[]
        for j in range (char_count):
            if gate1 == True and gate2 == False:
                symbols = s.ascii_letters + s.digits
                password.append(r.choice(symbols))
            elif gate2 == True and gate1 == False:
                symbols = s.ascii_letters + special_symbols
                password.append(r.choice(symbols))
            elif gate1 == True and gate2 == True:
                symbols = s.ascii_letters + special_symbols + s.digits
                password.append(r.choice(symbols))
            else:
                password.append(r.choice(s.ascii_letters))
        passwords.append(''.join(password))
    write_into_file(passwords)

# * -- Create and write into new file -- * #
def write_into_file(passwords: list):
    dir_path = r"./passwords"
    file_name = "new_passwords"
    file_path = os.path.join(dir_path, file_name)

    if not os.path.exists (dir_path):
        os.makedirs(dir_path)
    
    with open (file_path, 'w') as f:
        for password in passwords:
            f.write(f"{password}\n\n")

# $ -- END OF FUNCTIONS -- $ #

# $ -- START OF WIDGETS -- $ #
# * -- Create Widgets -- * #
password_lenght = Label(root, text="Enter passwords lenght: ")
password_number = Entry(root)
password_amount_label = Label(root, text="Enter amount of passwords wanted: ")
password_amount = Entry(root)
password_check = Button(root, text="Create passwords", command=password_checker, state=NORMAL)
result = Label(root, text='')
quit_btn = Button(root, text="Exit program", command=root.quit)

# * -- Create checkboxes -- * #
check_number = IntVar()
check_symbols = IntVar()

checkbox_number = Checkbutton(root, text = "Add numbers to passwords: ", variable=check_number)
checkbox_symbols = Checkbutton(root, text = "Add symbols to passwords: ", variable=check_symbols)

# * -- Unpacks Widgets onto window -- * #
password_amount_label.pack(pady=15)
password_amount.pack(pady=5)
password_lenght.pack(pady=15)
password_number.pack(pady=5)

checkbox_number.pack(pady=5)
checkbox_symbols.pack(pady=5)

password_check.pack(pady=10)
result.pack(pady=10)
quit_btn.pack()

# * -- Orders the widgets to TAB order -- * #
new_order = (
    password_amount_label,
    password_amount,
    password_lenght,
    password_number,
    checkbox_number,
    checkbox_symbols,
    password_check,
    result,
    quit_btn
)

for widget in new_order:
    widget.lift()

# $ -- END OF WIDGETS -- $ #

# $ -- RUN APP -- $ #
if __name__ == "__main__":
    root.mainloop()