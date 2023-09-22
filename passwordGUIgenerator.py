import tkinter as tk
import random
import string
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_password(length, complexity):
    if complexity == "Low":
        characters = string.ascii_letters
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "High":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        complexity = complexity_var.get()

        password = generate_password(length, complexity)
        result_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid length.")
        result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x400")
root.resizable(False, False)

# Load an icon
icon = Image.open("lock_icon.jpeg")
icon = ImageTk.PhotoImage(icon)
root.iconphoto(True, icon)

# Create and pack widgets
title_label = ttk.Label(root, text="Password Generator", font=("Helvetica", 16))
title_label.pack(pady=10)

length_label = ttk.Label(root, text="Enter Password Length:")
length_label.pack()

length_entry = ttk.Entry(root)
length_entry.pack()

complexity_label = ttk.Label(root, text="Select Complexity Level:")
complexity_label.pack()

complexity_var = tk.StringVar()
complexity_var.set("Medium")  # Default value

low_complexity_radio = ttk.Radiobutton(root, text="Low", variable=complexity_var, value="Low")
medium_complexity_radio = ttk.Radiobutton(root, text="Medium", variable=complexity_var, value="Medium")
high_complexity_radio = ttk.Radiobutton(root, text="High", variable=complexity_var, value="High")

low_complexity_radio.pack()
medium_complexity_radio.pack()
high_complexity_radio.pack()

generate_button = ttk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=10)

result_label = ttk.Label(root, text="", font=("Sans-serif", 14))
result_label.pack()

# Add an image or logo
image = Image.open("logo.png")
image = image.resize((100,100))

logo = ImageTk.PhotoImage(image)
logo_label = ttk.Label(root, image=logo)
logo_label.image = logo
logo_label.pack()

print("Vicky Kumar")

# Start the main loop
root.mainloop()
