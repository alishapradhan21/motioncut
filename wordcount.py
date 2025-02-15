import tkinter as tk
from tkinter import messagebox

def count_words(text):
    """
    Counts the number of words in the given text.
    A word is defined as a sequence of characters separated by whitespace.

    Args:
        text (str): The input text to count words in.

    Returns:
        int: The number of words in the text.
    """
    # Split the text into words using whitespace as the delimiter
    words = text.split()
    return len(words)

def on_count_button_click():
    """
    Handles the button click event to count words in the input text.
    """
    user_input = text_input.get("1.0", tk.END).strip()

    # Error handling for empty input
    if not user_input:
        messagebox.showerror("Error", "No text entered. Please try again.")
        return

    # Count the words in the input text
    word_count = count_words(user_input)

    # Display the result
    result_label.config(text=f"Word Count: {word_count}")

def create_gui():
    """
    Creates the GUI for the Word Counter application.
    """
    # Create the main window
    root = tk.Tk()
    root.title("Word Counter")

    # Create a text input widget
    global text_input
    text_input = tk.Text(root, height=10, width=50)
    text_input.pack(pady=10)

    # Create a button to count words
    count_button = tk.Button(root, text="Count Words", command=on_count_button_click)
    count_button.pack(pady=5)

    # Create a label to display the result
    global result_label
    result_label = tk.Label(root, text="Word Count: 0", font=("Helvetica", 12))
    result_label.pack(pady=10)

    # Run the main event loop
    root.mainloop()

# Entry point of the program
if __name__ == "__main__":
    create_gui()

