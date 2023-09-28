import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=password)

# Create a Tkinter window
window = tk.Tk()
window.title("Password Generator")

# Label and Entry for password length
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Label to display the generated password
result_label = tk.Label(window, text="")
result_label.pack()

# Start the Tkinter main loop
window.mainloop()