import tkinter as tk
from tkinter import filedialog
import PyPDF2

# Define a function to handle the file selection


def select_file():

    file_path = filedialog.askopenfilename(
        initialdir='/', title='Select a file', filetypes=[('PDF files', '*.pdf')])

    try:
        with open(file_path, 'rb') as file:
            print({file_path})
    except:
        print(f"Error: Invalid PDF file selected ({file_path})")


# Create a Tkinter window
window = tk.Tk()

# Create a button widget that triggers the select_file() function when clicked
button = tk.Button(window, text='Select a file', command=select_file)
button.pack()

# Run the Tkinter event loop
window.mainloop()
