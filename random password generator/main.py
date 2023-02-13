from tkinter import *
import random, string
import tkinter.messagebox as tmsg

# Initialize Window
root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("PASSWORD GENERATOR")

# Label for Title
Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
Label(root, text ='by @YourUsername', font ='arial 10').pack(side = BOTTOM)

# Select Password Length
pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()

# Function to Generate Password
pass_str = StringVar()
def generate_password():
    try:
        password_length = int(pass_len.get())
        if password_length < 4:
            tmsg.showerror("Error", "Password length should be at least 4.")
            return
        password = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, password_length))
        pass_str.set(password)
    except ValueError:
        tmsg.showerror("Error", "Please enter a valid integer for password length.")

# Button to Generate Password
Button(root, text = "GENERATE PASSWORD", command = generate_password).pack(pady=5)
Entry(root, textvariable=pass_str).pack()

# Function to Copy Password
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(pass_str.get())
    tmsg.showinfo("Success", "Password copied to clipboard!")

# Button to Copy Password
Button(root, text = 'COPY TO CLIPBOARD', command = copy_password).pack(pady=5)

# Start the main loop
root.mainloop()
