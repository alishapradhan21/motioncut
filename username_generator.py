import tkinter as tk
from tkinter import messagebox
import random

# Predefined lists of adjectives and nouns
adjectives = ["Pretty", "Cute", "Sweet", "Lovely", "Silly", "Charming", "Loyal", "Simple"]
nouns = ["Alisha", "Dev", "Sonali", "Baby", "Phoenix", "Bisnu", "Anni", "Anjali"]
special_characters = ["!", "@", "#", "$", "%", "&", "*"]

def generate_username():
    try:
        num_usernames = int(num_usernames_entry.get())
        include_numbers = include_numbers_var.get()
        include_special = include_special_var.get()

        usernames = []
        for _ in range(num_usernames):
            adjective = random.choice(adjectives)
            noun = random.choice(nouns)
            username = f"{adjective}{noun}"

            if include_numbers:
                username += str(random.randint(10, 99))

            if include_special:
                username += random.choice(special_characters)

            usernames.append(username)

        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "\n".join(usernames))

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of usernames.")

def save_usernames():
    usernames = output_text.get(1.0, tk.END).strip()
    if not usernames:
        messagebox.showwarning("No Usernames", "No usernames to save. Please generate some first.")
        return

    with open("usernames.txt", "w") as file:
        file.write(usernames)
    messagebox.showinfo("Saved", "Usernames saved to usernames.txt")

# Set up the main window
root = tk.Tk()
root.title("Random Username Generator")
root.geometry("500x500")
root.resizable(False, False)

# Widgets for user inputs
frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Number of Usernames:").grid(row=0, column=0, padx=5, pady=5)
num_usernames_entry = tk.Entry(frame)
num_usernames_entry.grid(row=0, column=1, padx=5, pady=5)

include_numbers_var = tk.BooleanVar()
include_numbers_check = tk.Checkbutton(frame, text="Include Numbers", variable=include_numbers_var)
include_numbers_check.grid(row=1, column=0, columnspan=2, pady=5)

include_special_var = tk.BooleanVar()
include_special_check = tk.Checkbutton(frame, text="Include Special Characters", variable=include_special_var)
include_special_check.grid(row=2, column=0, columnspan=2, pady=5)

# Buttons for actions
generate_button = tk.Button(root, text="Generate Usernames", command=generate_username)
generate_button.pack(pady=10)

save_button = tk.Button(root, text="Save Usernames", command=save_usernames)
save_button.pack(pady=5)

# Output display
output_text = tk.Text(root, height=15, width=50)
output_text.pack(pady=10)

# Run the main loop
root.mainloop()

    



