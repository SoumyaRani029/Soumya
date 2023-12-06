
import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password(length=12):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine character sets
    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    # Ensure the password length is at least 8 characters
    length = max(length, 8)

    # Generate a strong password
    password = random.sample(lowercase_letters, 1) + \
               random.sample(uppercase_letters, 1) + \
               random.sample(digits, 1) + \
               random.sample(symbols, 1) + \
               random.sample(all_characters, length - 4)

    # Shuffle the password characters
    random.shuffle(password)

    # Convert the list to a string
    password = ''.join(password)

    return password

def generate_passwords(num_passwords, length):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

def generate_password_button_clicked():
    password_length = int(length_entry.get())
    num_passwords = int(num_passwords_entry.get())
    
    passwords = generate_passwords(num_passwords, password_length)
    
    # Display generated passwords
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    for idx, password in enumerate(passwords, start=1):
        result_text.insert(tk.END, f"Password {idx}: {password}\n")
    result_text.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Password Length Label and Entry
length_label = ttk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10, sticky="E")
length_entry = ttk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)
length_entry.insert(0, "12")

# Number of Passwords Label and Entry
num_passwords_label = ttk.Label(root, text="Number of Passwords:")
num_passwords_label.grid(row=1, column=0, padx=10, pady=10, sticky="E")
num_passwords_entry = ttk.Entry(root)
num_passwords_entry.grid(row=1, column=1, padx=10, pady=10)
num_passwords_entry.insert(0, "1")

# Generate Password Button
generate_button = ttk.Button(root, text="Generate Passwords", command=generate_password_button_clicked)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result Text
result_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)
result_text.grid(row=3, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
